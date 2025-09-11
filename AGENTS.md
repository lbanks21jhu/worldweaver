# Repository Guidelines

## Project Structure & Module Organization
- `src/` — application code (FastAPI app, services, DB, models). Key: `main.py`, `src/api/*`, `src/services/*`, `src/database.py`, `src/models/*`.
- `tests/` — pytest suites: `api/`, `integration/`, `contract/`, `core/`, `database/`, `diagnostic/`.
- `specs/` — architecture, testing strategy, and OpenAPI contracts in `specs/001-plan/contracts/*.openapi.yaml`.
- `scripts/` and `py_scripts/` — dev utilities (feature scaffolding, seeding, debugging).
- `db/`, `templates/`, `twine_resources/`, `reports/` — data helpers, templates, research, and artifacts.
- Principles and backlog: see `memory/constitution.md` and `tasks/backlog.md`.

## Build, Test, and Development Commands
- Create env + install: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Run API locally: `uvicorn main:app --reload`
- Run tests: `pytest -q` (subset: `pytest tests/api/test_author_validation.py -q` or `pytest -k "spatial and not navigation" -q`).
- Optional tools: `black .` for formatting, `flake8` for linting (install if needed).
- Database: set `DW_DB_PATH` (SQLite). Defaults: `worldweaver.db`; tests prefer `test_database.db`. Example: `DW_DB_PATH=/tmp/ww.db uvicorn main:app --reload`.

## Coding Style & Naming Conventions
- Python 3.11+, 4-space indentation; use type hints and docstrings.
- Names: files/modules `snake_case.py`; functions/vars `snake_case`; classes `CamelCase`.
- Routing lives in `src/api/*`; business logic in `src/services/*`; schemas in `src/models/*`.
- Keep route handlers thin; isolate side effects; write pure helpers where practical.

## Testing Guidelines
- Frameworks: `pytest`, `pytest-asyncio`, `httpx` for API tests.
- Place tests under `tests/`; files `test_*.py`; descriptive test names.
- Avoid test coupling: seed data per test/fixture; don’t depend on prior runs.
- Target coverage for new/changed code and add regression tests for fixed bugs.

## Commit & Pull Request Guidelines
- Commits: imperative mood with optional scope (e.g., `api:`, `services:`, `spec:`). Keep summaries concise; link issues.
- PRs: clear description, rationale, and testing notes. Include sample requests/responses for API changes. Update `specs/` and OpenAPI contracts when endpoints change.
- Keep PRs small and focused; include tests alongside behavior changes.

## Security & Configuration Tips
- Use `.env` for secrets (e.g., `OPENAI_API_KEY`); never commit it.
- Prefer env vars over hardcoded values; document new config in `specs/` or `README`.
