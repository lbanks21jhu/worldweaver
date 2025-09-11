"""Generation pipeline utilities for planning, generating, evaluating, and linking storylets.

This module provides a light-weight, fast pipeline intended for use in both
development and test environments. It defers creative heavy-lifting to the
LLM helper in `src/services/llm_service.py`, which already includes fast-path
fallbacks to avoid network calls when running tests.

Design goals:
- Keep interfaces simple and string-friendly to make it easy to plug into tools.
- Be resilient: accept either plain text or JSON strings where appropriate.
- Optimize for speed: use local heuristics and the LLM service's fast path.
"""

from __future__ import annotations

from typing import Any, Dict, List
import json
import os
import re

from .llm_service import llm_suggest_storylets


def _extract_keywords(text: str, k: int = 5) -> List[str]:
    """Extract simple keywords from text using frequency of alphanumeric words.

    This is intentionally fast and dependency-free. It favors nouns-like tokens
    by filtering stop-y words and short tokens. Not perfect, but good enough for
    planning prompts.
    """
    if not text:
        return []

    tokens = re.findall(r"[a-zA-Z][a-zA-Z\-']{2,}", text.lower())
    stop = {
        "the",
        "and",
        "but",
        "with",
        "from",
        "into",
        "over",
        "under",
        "for",
        "that",
        "this",
        "your",
        "their",
        "his",
        "her",
        "you",
        "they",
        "she",
        "he",
        "are",
        "was",
        "were",
        "have",
        "has",
        "had",
        "there",
        "then",
        "here",
        "into",
        "onto",
        "about",
        "also",
        "more",
        "very",
    }
    freq: Dict[str, int] = {}
    for t in tokens:
        if t in stop:
            continue
        freq[t] = freq.get(t, 0) + 1

    return [w for w, _ in sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]]


class StoryletPlanner:
    """Plan storylet prompts from a corpus of story text.

    Given a block of story text, produce `n` compact prompt strings that can
    guide the generator toward different facets of the story (locations, items,
    stakes). This uses a quick keyword extraction heuristic for speed.
    """

    def __init__(self, n: int = 3):
        self.n = max(1, int(n))

    def plan(self, story: str) -> List[str]:
        """Return `n` high-signal prompts derived from `story`.

        Each prompt encodes a focus area (theme, conflict, or location) to
        encourage varied storylet generation.
        """
        keywords = _extract_keywords(story, k=8) or ["adventure", "discovery", "tension"]
        # Form prompts that emphasize different combinations of keywords
        prompts: List[str] = []
        for i in range(self.n):
            # rotate keywords to get variety without heavy computation
            focus = keywords[i % len(keywords)] if keywords else f"focus{i+1}"
            extra = ", ".join(keywords[:3]) if keywords else "exploration, choice, consequence"
            prompts.append(
                f"Create a coherent, choice-driven storylet centered on '{focus}' with related elements: {extra}."
            )
        return prompts


class StoryletGenerator:
    """Generate storylets using the LLM helper, with fast fallbacks.

    The generator consumes a prompt string (typically from the planner),
    extracts lightweight themes, and calls `llm_suggest_storylets` which has
    built-in fast modes for tests and offline development.
    """

    def __init__(self, model_name: str = "gpt-4o"):
        self.model_name = model_name

    def _themes_from_prompt(self, prompt: str) -> List[str]:
        return _extract_keywords(prompt, k=4) or ["adventure", "choice", "progress"]

    def generate(self, storylet_prompt: str) -> str:
        """Generate a single storylet as a JSON string.

        Returns a compact JSON string with keys: title, text_template,
        requires, choices, weight. This string form keeps the interface simple
        for callers that store or transmit storylets as text blobs.
        """
        themes = self._themes_from_prompt(storylet_prompt)
        # Minimal bible helps nudge continuity while remaining fast
        bible = {
            "creative_direction": storylet_prompt,
            "story_coherence": {
                "maintain_established_facts": True,
                "logical_cause_and_effect": True,
            },
        }
        storylets = llm_suggest_storylets(1, themes, bible) or []
        storylet: Dict[str, Any]
        if storylets:
            storylet = storylets[0]
        else:
            # Local fallback if upstream returned nothing for any reason
            storylet = {
                "title": "A Small Turning",
                "text_template": "You make a small but meaningful choice.",
                "requires": {},
                "choices": [{"label": "Continue", "set": {}}],
                "weight": 1.0,
            }
        return json.dumps(storylet, ensure_ascii=False)


class StoryletEvaluator:
    """Score storylet quality with fast heuristics.

    The evaluator parses a JSON string (if possible) and applies simple
    structural and readability heuristics to produce a score in [0, 1].
    """

    def __init__(self, model_name: str = "gpt-4o"):
        self.model_name = model_name

    def _score_structural(self, s: Dict[str, Any]) -> float:
        score = 0.0
        # Required fields present
        required = ["title", "text_template", "choices"]
        score += sum(1 for k in required if s.get(k)) / len(required) * 0.5
        # Choices quality: at least 2 choices gets full marks for this slice
        choices = s.get("choices") or []
        if isinstance(choices, list):
            if len(choices) >= 2:
                score += 0.25
            elif len(choices) == 1:
                score += 0.15
        # Text length and variables usage hint at richness
        text = str(s.get("text_template") or "")
        if len(text) >= 60:
            score += 0.15
        elif len(text) >= 30:
            score += 0.1
        # Light coherence check: presence of set/require patterns
        has_require = bool(s.get("requires"))
        sets_var = any((c.get("set") for c in choices if isinstance(c, dict)))
        if has_require and sets_var:
            score += 0.1
        return min(score, 1.0)

    def evaluate(self, storylet: str) -> float:
        """Return a quality score in [0, 1] for the given storylet string.

        Accepts either a JSON-encoded storylet or a plain text string.
        """
        try:
            data = json.loads(storylet)
            if isinstance(data, dict):
                return self._score_structural(data)
        except Exception:
            pass
        # Plain text fallback: basic readability/length heuristic
        length = len(storylet or "")
        if length >= 80:
            return 0.6
        if length >= 40:
            return 0.45
        return 0.3


class StoryletLinker:
    """Establish lightweight linkage between storylets.

    Takes a list of JSON strings representing storylets, ensures each storylet
    offers a forward navigation choice to the next one by setting a `location`
    (if present) or adding a neutral `continue` choice. Returns a JSON string
    with a `storylets` array containing potentially updated storylets.
    """

    def link(self, storylets: List[str]) -> str:
        parsed: List[Dict[str, Any]] = []
        for s in storylets:
            try:
                obj = json.loads(s)
                if isinstance(obj, dict):
                    parsed.append(obj)
            except Exception:
                # Wrap raw text into a minimal storylet
                parsed.append(
                    {
                        "title": "Untitled",
                        "text_template": str(s),
                        "requires": {},
                        "choices": [{"label": "Continue", "set": {}}],
                        "weight": 1.0,
                    }
                )

        # Best-effort forward linkage based on `requires.location` and choice `set.location`
        def _required_location(sl: Dict[str, Any]) -> str | None:
            req = sl.get("requires") or {}
            return req.get("location") if isinstance(req, dict) else None

        locations = [_required_location(sl) for sl in parsed]

        for i in range(len(parsed) - 1):
            cur = parsed[i]
            nxt = parsed[i + 1]
            target_loc = _required_location(nxt)
            # Ensure there is a choice that leads toward the next storylet
            choices = cur.get("choices") or []
            has_forward = any(
                isinstance(c, dict)
                and isinstance(c.get("set"), dict)
                and (
                    ("location" in c["set"] and c["set"]["location"] == target_loc)
                    or (target_loc is None and c["set"] == {})
                )
                for c in choices
            )
            if not has_forward:
                label = (
                    f"Proceed to {target_loc}" if target_loc else "Continue onward"
                )
                set_obj = {"location": target_loc} if target_loc else {}
                choices.append({"label": label, "set": set_obj})
                cur["choices"] = choices

        return json.dumps({"storylets": parsed}, ensure_ascii=False)
