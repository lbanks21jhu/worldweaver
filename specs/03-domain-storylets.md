# 03-domain-storylets.md

## Storylet Domain Specification

### Uniqueness & Normalization
- Storylet titles must be unique (case-insensitive, trimmed).
- Choices and requirements are normalized to standard schema (see Pydantic models).
- Duplicate detection is enforced at DB and API level.

### Mandatory Spatial Assignment
- Every storylet must have a spatial coordinate assigned at creation.
- Semantic mapping (e.g., 'forest' → west, 'mountain' → north) via LocationMapper.
- Bulk fixes and dry-run logging available for legacy storylets.

### Choice Normalization
- Choices must use `{label, set}` format; legacy `{text, set_vars}` auto-converted.
- All choices must lead to valid storylet transitions or state changes.

### Duplicate Detection
- Case-insensitive, normalized title comparison.
- API skips duplicates and logs attempts.
- Negative tests for duplicate creation in `true_tests/api/test_author_duplicates.py`.

### Error Handling
- Duplicate attempts return actionable error messages.
- All errors are logged and surfaced in API responses.

### Definition of Done
- 100% of storylets have unique, normalized titles and spatial coordinates.
- All choices/requirements conform to schema.
- Negative tests for duplicates and normalization pass.
