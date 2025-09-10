# Epic 1: API Contracts Complete (author/game)

## Feature Overview
Document and formalize all request/response schemas for author/game endpoints. Ensure robust contract coverage for frontend and test automation. Add negative tests for duplicate storylets and invalid requests. Document side effects and idempotency for all endpoints.

## Requirements
- All author/game API endpoints must have documented request/response schemas.
- Negative tests for duplicate storylets and invalid requests must be present.
- Side effects and idempotency for endpoints must be documented.

## User Stories
- As a frontend developer, I need clear API contracts so I can build UI components and validate data.
- As a tester, I need negative test cases to ensure error handling is robust.
- As a backend developer, I need documentation of side effects and idempotency to safely implement bulk operations.

## Functional Requirements
- API contract documentation for all author/game endpoints.
- Negative test coverage for duplicate storylets and invalid requests.
- Documentation of endpoint side effects and idempotency.

## Non-Functional Requirements
- Documentation must be clear, versioned, and accessible to all contributors.
- Tests must be automated and integrated into CI.

## Success Criteria
- All endpoints have request/response schemas documented in OpenAPI format.
- Negative tests for duplicate and invalid requests pass and are reviewed.
- Side effects and idempotency are documented for each endpoint.

## Acceptance Criteria
- API contracts are published in `specs/002-author+llm/contracts/`.
- Negative tests are present in `true_tests/api/` and pass.
- Documentation of side effects and idempotency is included in the spec.

## Dependencies
- Constitution
- models/schemas.py
- specs/01-api-contracts-author.md
- specs/02-api-contracts-game.md
- true_tests/api/

## Constraints
- Must follow constitutional requirements for testing and documentation.
- No silent failures or undocumented endpoints.

## Technical Context
- Language: Python 3.x
- Framework: FastAPI
- Testing: pytest
- Storage: SQLite
- Target Platform: Linux server
