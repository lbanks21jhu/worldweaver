# Tasks: Epic 2 - Spatial Integrity + Navigation Robustness

**Input**: Design documents from `/specs/001-plan/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow
```
1. Load plan.md and supporting docs
2. Extract entities, endpoints, and scenarios for spatial features
3. Generate tasks by category and dependency
4. Mark parallelizable tasks [P]
5. Number tasks sequentially (T001, T002...)
```

## Phase 3.1: Setup
- [x] T001 Ensure project structure supports spatial features (src/services/spatial_navigator.py, src/models/schemas.py)
- [x] T002 [P] Verify dependencies: FastAPI, SQLAlchemy, Pydantic, pytest
- [x] T003 [P] Configure linting/formatting for spatial code (black, flake8)

## Phase 3.2: Tests First (TDD)
- [ ] T004 [P] Contract test GET /api/spatial/navigation/{session_id} in tests/contract/test_spatial_navigation.py
- [ ] T005 [P] Contract test POST /api/spatial/move/{session_id} in tests/contract/test_spatial_move.py
- [ ] T006 [P] Contract test GET /api/spatial/map in tests/contract/test_spatial_map.py
- [ ] T007 [P] Contract test POST /api/spatial/assign-positions in tests/contract/test_spatial_assign.py
- [ ] T008 Integration test: 8-direction movement and edge cases in tests/integration/test_spatial_navigation.py
- [ ] T009 Integration test: coordinate assignment and fallbacks in tests/integration/test_spatial_assignment.py

## Phase 3.3: Core Implementation
- [x] T010 [P] Implement Storylet spatial fields in src/models/schemas.py
- [x] T011 [P] Implement coordinate assignment logic in src/services/spatial_navigator.py
- [x] T012 Implement GET /api/spatial/navigation/{session_id} endpoint in src/api/game.py
- [x] T013 Implement POST /api/spatial/move/{session_id} endpoint in src/api/game.py
- [x] T014 Implement GET /api/spatial/map endpoint in src/api/game.py
- [x] T015 Implement POST /api/spatial/assign-positions endpoint in src/api/game.py
- [ ] T016 Error handling and logging for spatial endpoints in src/services/spatial_navigator.py

## Phase 3.4: Integration
- [ ] T017 Connect spatial assignment to DB and storylet creation in src/services/spatial_navigator.py
- [ ] T018 Add structured logging for spatial events in src/services/spatial_navigator.py
- [ ] T019 Document coordinate assignment rules and fallbacks in specs/04-domain-spatial.md

## Phase 3.5: Polish
- [ ] T020 [P] Unit tests for coordinate assignment in tests/unit/test_spatial_assignment.py
- [ ] T021 [P] Performance tests for navigation in tests/unit/test_spatial_performance.py
- [ ] T022 [P] Update docs for spatial endpoints in specs/001-plan/contracts/spatial.openapi.yaml
- [ ] T023 [P] Manual test: edge case navigation and assignment

## Dependencies
- Tests (T004-T009) before implementation (T010-T016)
- T010 blocks T011, T017
- T011 blocks T012-T015
- Implementation before polish (T020-T023)

## Parallel Example
```
# Launch T004-T007 together:
Task: "Contract test GET /api/spatial/navigation/{session_id} in tests/contract/test_spatial_navigation.py"
Task: "Contract test POST /api/spatial/move/{session_id} in tests/contract/test_spatial_move.py"
Task: "Contract test GET /api/spatial/map in tests/contract/test_spatial_map.py"
Task: "Contract test POST /api/spatial/assign-positions in tests/contract/test_spatial_assign.py"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts
