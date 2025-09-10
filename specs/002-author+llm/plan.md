# Implementation Plan: Epic 1 - API Contracts Complete (author/game)

**Branch**: `002-author+llm` | **Date**: September 9, 2025 | **Spec**: [/home/levibanks/personal_projects/worldweaver/specs/002-author+llm/spec.md]
**Input**: Feature specification from `/home/levibanks/personal_projects/worldweaver/specs/002-author+llm/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
4. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
5. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file
6. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
7. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
8. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
Epic 1 aims to formalize and document all author/game API contracts, add robust negative test coverage, and ensure side effects/idempotency are explicit for all endpoints. The technical approach leverages FastAPI's OpenAPI support, pytest for automated tests, and strict documentation standards.

## Technical Context
**Language/Version**: Python 3.x  
**Primary Dependencies**: FastAPI, pytest  
**Storage**: SQLite  
**Testing**: pytest  
**Target Platform**: Linux server
**Project Type**: single (backend API + tests)
**Performance Goals**: Reliable contract coverage, automated test pass rate 100%
**Constraints**: Must follow constitutional requirements for testing and documentation. No silent failures or undocumented endpoints.
**Scale/Scope**: All author/game endpoints, negative test coverage, contract documentation

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Simplicity**:
- Projects: 2 (api, tests)
- Using framework directly? Yes (FastAPI)
- Single data model? Yes (Storylet, endpoints)
- Avoiding patterns? Yes (no unnecessary wrappers)

**Architecture**:
- EVERY feature as library? Yes (API endpoints, contract files)
- Libraries listed: FastAPI (API), pytest (testing)
- CLI per library: N/A
- Library docs: OpenAPI planned

**Testing (NON-NEGOTIABLE)**:
- RED-GREEN-Refactor cycle enforced? Yes
- Git commits show tests before implementation? Yes
- Order: Contract→Integration→Unit strictly followed
- Real dependencies used? Yes
- Integration tests for: contract changes, shared schemas
- FORBIDDEN: Implementation before test, skipping RED phase

**Observability**:
- Structured logging included? Yes
- Frontend logs → backend? N/A
- Error context sufficient? Yes

**Versioning**:
- Version number assigned? Yes (OpenAPI versioning)
- BUILD increments on every change? Yes
- Breaking changes handled? Yes (review, migration plan)

## Project Structure
```
specs/002-author+llm/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
```

## Phase 0: Outline & Research
- See `research.md` for unknowns, best practices, and decisions.

## Phase 1: Design & Contracts
- See `data-model.md` for entities and validation rules.
- See `contracts/` for OpenAPI contract files.
- See `quickstart.md` for setup and validation steps.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (contracts, data model, quickstart)
- Each contract → contract test task [P]
- Each entity → model creation task [P]
- Each user story → integration test task
- Implementation tasks to make tests pass

**Ordering Strategy**:
- TDD order: Tests before implementation
- Dependency order: Models before services before UI
- Mark [P] for parallel execution (independent files)

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

## Complexity Tracking
*No constitution violations detected. No complexity deviations required.*

## Progress Tracking
**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [ ] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
