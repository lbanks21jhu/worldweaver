# 01-api-contracts-author.md

## Endpoints

| Route                      | Method | Purpose                                  | Auth | Request Schema         | Response Schema         | Side Effects         | Idempotency/Rate Limit | Negative Tests                |
|----------------------------|--------|------------------------------------------|------|-----------------------|------------------------|----------------------|------------------------|-------------------------------|
| /author/suggest            | POST   | Suggest storylets via LLM                | None | SuggestReq            | SuggestResp            | None                 | Yes (same input)       | LLM error, empty result       |
| /author/suggest            | POST   | Suggest storylets via LLM (add `?commit=1` to save) | None | SuggestReq            | SuggestResp            | DB write, spatial, AI (if commit=1) | Yes (skips duplicates) | LLM error, empty result, DB error |
| /author/populate           | POST   | Bulk populate storylets (AI)             | None | target_count:int      | {success, added, ...}  | DB write, spatial, AI| Yes (limit 100)        | Invalid count, DB error       |
| /author/generate-intelligent| POST  | AI gap-filling storylet generation       | None | GenerateStoryletRequest| {storylets, improvements}| DB write, spatial, AI| Yes                    | LLM error, duplicate, DB error|
| /author/generate-targeted  | POST   | Targeted gap-filling storylets           | None | None                  | {storylets, improvements}| DB write, spatial, AI| Yes                    | No gaps, DB error             |
| /author/generate-world     | POST   | Generate world from description          | None | WorldDescription      | {storylets, improvements}| DB write, spatial, AI| Yes                    | LLM error, DB error           |
| /author/debug              | GET    | Debug game state                         | None | None                  | {session_variables, ...}| None                 | Yes                    | DB error                      |
| /author/storylet-analysis  | GET    | Analyze storylet ecosystem               | None | None                  | {gap_analysis, ...}    | None                 | Yes                    | DB error                      |

- **Request/Response Schemas**:  
  - See `src/models/schemas.py` for Pydantic models.
- **Side Effects**:  
  - DB writes, spatial assignment, auto-improvement, cache invalidation.
- **Idempotency**:  
  - Duplicate titles skipped, case-insensitive.
- **Rate Limits**:  
  - Bulk ops capped (e.g., max 100 storylets).
- **Negative Tests**:  
  - Duplicate storylet, invalid count, LLM/DB error, missing required fields.
