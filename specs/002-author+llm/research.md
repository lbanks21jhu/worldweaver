# Phase 0: Research for Epic 1 (API Contracts Complete)

## Unknowns / Clarifications
- Are all endpoints already defined in FastAPI, or are new ones needed?
- What are the edge cases for duplicate storylets and invalid requests?
- What are the current side effects and idempotency guarantees for each endpoint?
- How are contracts currently documented (OpenAPI, markdown, etc.)?
- What is the process for updating contracts and tests in CI?

## Best Practices
- Use OpenAPI 3.0 for contract documentation.
- Document idempotency and side effects in endpoint descriptions.
- Negative tests should cover all failure modes, not just duplicates/invalids.
- Contracts should be versioned and reviewed before merging.
- Integrate contract tests with CI to prevent regressions.

## Integration Patterns
- Use FastAPI's built-in OpenAPI generation for endpoint schemas.
- Store contract files in `specs/002-author+llm/contracts/`.
- Use pytest for negative test automation in `true_tests/api/`.
- Document side effects/idempotency in endpoint docstrings and OpenAPI descriptions.

## Decisions
- All contracts will be documented in OpenAPI format and stored in the feature's contracts directory.
- Negative tests will be automated and integrated into CI.
- Side effects and idempotency will be documented for each endpoint in both code and spec files.

## Rationale
- OpenAPI is widely supported and integrates with FastAPI.
- Automated tests ensure robust error handling and prevent silent failures.
- Documenting side effects/idempotency supports safe bulk operations and future development.

## Alternatives Considered
- Using markdown for contracts (rejected: less tooling support).
- Manual test scripts (rejected: not scalable, less reliable).
- Skipping idempotency documentation (rejected: risk of destructive ops).

---
All unknowns and clarifications will be resolved before moving to Phase 1.
