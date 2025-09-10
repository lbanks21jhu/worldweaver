# Quickstart: API Contracts Complete (Epic 1)

## Setup
1. Ensure you are on the feature branch: `002-author+llm`.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run tests:
   ```sh
   pytest true_tests/api/
   ```

## How to Use
- Review API contracts in `specs/002-author+llm/contracts/`.
- Implement endpoints in FastAPI according to documented schemas.
- Add negative tests for duplicate storylets and invalid requests.
- Document side effects and idempotency in endpoint docstrings and OpenAPI files.

## Validation
- All endpoints must pass contract and negative tests.
- Contracts must be reviewed and merged before implementation.
- Documentation must be updated for every contract change.

## Reference
- See `specs/002-author+llm/spec.md` for requirements and user stories.
- See `specs/002-author+llm/data-model.md` for entities and validation rules.
- See `specs/002-author+llm/research.md` for decisions and rationale.
