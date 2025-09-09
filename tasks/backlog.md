# Backlog

## Epic 1: API Contracts Complete (author/game)
- **Task**: Document all request/response schemas for author/game endpoints  
  - *Rationale*: Ensures clear contracts for frontend and test coverage  
  - *Acceptance*: All endpoints have explicit schemas, error shapes  
  - *Estimate*: 2d  
  - *Dependencies*: Constitution, models/schemas.py, specs/01-api-contracts-author.md, specs/02-api-contracts-game.md
- **Task**: Add negative tests for duplicate storylets, invalid requests  
  - *Rationale*: Prevent silent failures, ensure robust error handling  
  - *Acceptance*: Tests pass, errors are actionable  
  - *Estimate*: 2d  
  - *Dependencies*: true_tests/api/
- **Task**: Document side effects and idempotency for all endpoints  
  - *Rationale*: Traceability and safe bulk ops  
  - *Acceptance*: Spec sections updated, tests verify  
  - *Estimate*: 1d  
  - *Dependencies*: Spec drafts

## Epic 2: Spatial Integrity + Navigation Robustness
- **Task**: Ensure all storylets have valid spatial coordinates  
  - *Rationale*: Prevent broken navigation, support compass UI  
  - *Acceptance*: 100% coverage, dry-run logging  
  - *Estimate*: 2d  
  - *Dependencies*: spatial_navigator.py, tests/integration/, specs/04-domain-spatial.md
- **Task**: Add tests for 8-direction movement and edge cases  
  - *Rationale*: Validate navigation logic, prevent regressions  
  - *Acceptance*: All directions tested, failures logged  
  - *Estimate*: 2d  
  - *Dependencies*: test_spatial_navigation.py
- **Task**: Document coordinate assignment rules and fallbacks  
  - *Rationale*: Transparency for future devs  
  - *Acceptance*: Spec updated, code comments  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 3: Storylet Duplicate Prevention + Normalization
- **Task**: Enforce case-insensitive uniqueness for storylet titles  
  - *Rationale*: Prevent duplicate content, ensure integrity  
  - *Acceptance*: DB constraint, negative tests pass  
  - *Estimate*: 1d  
  - *Dependencies*: author.py, test_author_duplicates.py, specs/03-domain-storylets.md
- **Task**: Normalize choices and requirements for all storylets  
  - *Rationale*: Consistent API, easier testing  
  - *Acceptance*: All choices/requirements normalized  
  - *Estimate*: 1d  
  - *Dependencies*: schemas.py
- **Task**: Add tests for duplicate detection and normalization  
  - *Rationale*: Prevent regressions, ensure coverage  
  - *Acceptance*: Tests pass, errors are actionable  
  - *Estimate*: 1d  
  - *Dependencies*: true_tests/api/
- **Task**: Document storylet domain rules and normalization  
  - *Rationale*: Make rules explicit for future contributors  
  - *Acceptance*: specs/03-domain-storylets.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 4: Async/LLM Robustness + Fallbacks
- **Task**: Add timeout/retry logic for all LLM calls  
  - *Rationale*: Prevent blocking, ensure reliability  
  - *Acceptance*: Timeouts logged, fallbacks used  
  - *Estimate*: 2d  
  - *Dependencies*: llm_service.py, specs/06-llm-service.md
- **Task**: Document fallback storylet logic and error envelopes  
  - *Rationale*: Transparency, actionable errors  
  - *Acceptance*: Spec updated, error messages reviewed  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Add tests for LLM failure modes  
  - *Rationale*: Ensure graceful degradation  
  - *Acceptance*: Tests pass, errors are actionable  
  - *Estimate*: 1d  
  - *Dependencies*: true_tests/api/
- **Task**: Document LLM service domain and fallback logic  
  - *Rationale*: Make LLM rules explicit for future contributors  
  - *Acceptance*: specs/06-llm-service.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 5: State Manager Persistence + Recovery
- **Task**: Document state persistence and recovery guarantees  
  - *Rationale*: Prevent data loss, support save/load  
  - *Acceptance*: Spec updated, code comments  
  - *Estimate*: 1d  
  - *Dependencies*: state_manager.py, specs/05-domain-state-manager.md
- **Task**: Add tests for session recovery and cache cleanup  
  - *Rationale*: Ensure robust session management  
  - *Acceptance*: Tests pass, cache cleaned  
  - *Estimate*: 2d  
  - *Dependencies*: test_game_cache_cleanup.py
- **Task**: Document inventory/environment relationships  
  - *Rationale*: Clarify model for future devs  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Document state manager domain and recovery rules  
  - *Rationale*: Make state manager rules explicit for future contributors  
  - *Acceptance*: specs/05-domain-state-manager.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 6: DB Migrations + Idempotence Review
- **Task**: Review all migrations for idempotence and explicit types  
  - *Rationale*: Prevent destructive ops, ensure safe upgrades  
  - *Acceptance*: All migrations idempotent, types explicit  
  - *Estimate*: 2d  
  - *Dependencies*: db/, specs/07-db-and-migrations.md
- **Task**: Add tests for migration edge cases  
  - *Rationale*: Prevent data loss, ensure coverage  
  - *Acceptance*: Tests pass, errors logged  
  - *Estimate*: 1d  
  - *Dependencies*: tests/database/
- **Task**: Document migration workflow and confirmation rituals  
  - *Rationale*: Transparency, prevent accidental drops  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Document DB and migration domain rules  
  - *Rationale*: Make DB/migration rules explicit for future contributors  
  - *Acceptance*: specs/07-db-and-migrations.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 7: Test Matrix Expansion (race conditions, perf)
- **Task**: Add race-condition tests for storylet creation/session updates  
  - *Rationale*: Prevent concurrency bugs  
  - *Acceptance*: Tests pass, failures logged  
  - *Estimate*: 2d  
  - *Dependencies*: true_tests/api/, specs/09-testing-strategy.md
- **Task**: Add performance canary tests for large sessions/maps  
  - *Rationale*: Ensure scalability  
  - *Acceptance*: Tests pass, metrics logged  
  - *Estimate*: 2d  
  - *Dependencies*: tests/integration/
- **Task**: Document test matrix and coverage goals  
  - *Rationale*: Clarity for future contributors  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Document testing strategy and matrix  
  - *Rationale*: Make testing rules explicit for future contributors  
  - *Acceptance*: specs/09-testing-strategy.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 8: Observability (structured logs, error envelopes)
- **Task**: Add structured logging for key events (storylet create/update, spatial map, auto-improvement)  
  - *Rationale*: Debuggability, audit trail  
  - *Acceptance*: Logs present, errors actionable  
  - *Estimate*: 2d  
  - *Dependencies*: services/, specs/08-observability-and-errors.md
- **Task**: Document error envelope structure and logging policy  
  - *Rationale*: Consistency, safety  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Add tests for error logging and envelope consistency  
  - *Rationale*: Prevent leaks, ensure coverage  
  - *Acceptance*: Tests pass  
  - *Estimate*: 1d  
  - *Dependencies*: true_tests/api/
- **Task**: Document observability and error handling domain  
  - *Rationale*: Make observability rules explicit for future contributors  
  - *Acceptance*: specs/08-observability-and-errors.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 9: Twine/Frontend Integration (normalize <br>, no broken listeners)
- **Task**: Normalize Twine <br> rendering and navigation  
  - *Rationale*: Prevent UI bugs, improve UX  
  - *Acceptance*: No broken navigation, tests pass  
  - *Estimate*: 2d  
  - *Dependencies*: twine_resources/, specs/09-testing-strategy.md
- **Task**: Add tests for frontend integration edge cases  
  - *Rationale*: Prevent regressions  
  - *Acceptance*: Tests pass  
  - *Estimate*: 1d  
  - *Dependencies*: tests/integration/
- **Task**: Document Twine integration workflow  
  - *Rationale*: Clarity for future contributors  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts
- **Task**: Document Twine/Frontend integration domain  
  - *Rationale*: Make Twine integration rules explicit for future contributors  
  - *Acceptance*: specs/09-testing-strategy.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

## Epic 10: Docs & DevEx (runbook, local setup, env parity)
- **Task**: Write runbook for local setup and environment parity  
  - *Rationale*: Lower barrier for new contributors  
  - *Acceptance*: Runbook complete, onboarding tested  
  - *Estimate*: 2d  
  - *Dependencies*: requirements.txt, constitution.md, specs/10-non-functional.md
- **Task**: Document environment variables and config  
  - *Rationale*: Prevent config drift  
  - *Acceptance*: Spec updated  
  - *Estimate*: 1d  
  - *Dependencies*: requirements.txt
- **Task**: Add tests for setup scripts and config validation  
  - *Rationale*: Prevent setup errors  
  - *Acceptance*: Tests pass  
  - *Estimate*: 1d  
  - *Dependencies*: scripts/
- **Task**: Document non-functional requirements and DevEx  
  - *Rationale*: Make non-functional rules explicit for future contributors  
  - *Acceptance*: specs/10-non-functional.md complete  
  - *Estimate*: 1d  
  - *Dependencies*: spec drafts

### Task: Health check endpoint test
- **ID:** main-005
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** completed
- **Description:** Test GET /health returns {"ok": true} and valid ISO 8601 UTC timestamp.
- **Spec Reference:** (add manually if needed)


### Task: Remove duplicate SpatialNavigation code
- **ID:** twee-001
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** fix (code_quality)
- **Priority:** high
- **Status:** completed
- **Description:** Consolidate duplicate SpatialNavigation object definitions to avoid conflicting event listeners.
- **Spec Reference:** (add manually if needed)


### Task: Fix API path consistency
- **ID:** twee-002
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** fix (api_design)
- **Priority:** high
- **Status:** pending
- **Description:** Use consistent API prefixes (/api/author/generate-world vs /author/generate-world) to match backend routes.
- **Spec Reference:** (add manually if needed)


### Task: Generate World endpoint test
- **ID:** twee-007
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** test (integration_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test POST /author/generate-world with example payloads and error conditions using FastAPI TestClient.
- **Spec Reference:** (add manually if needed)


### Task: Next storylet endpoint test
- **ID:** twee-008
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** test (integration_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test POST /api/next with session_id and variables, assert response contains text, choices, vars.
- **Spec Reference:** (add manually if needed)


### Task: 🔒 Unified Thread Safety Implementation
- **ID:** MEGA-THREAD-SAFETY
- **Stage:** 2 (stage2)
- **File:** multiple
- **Type:** improvement (concurrency)
- **Priority:** high
- **Status:** pending
- **Description:** Implement comprehensive thread safety across game.py (cache operations), state_manager.py (state modifications), spatial_navigator.py (coordinate updates), story_smoother.py (database access), and location_mapper.py (coordinate assignment). Add threading locks, document constraints, or implement external cache solutions.
- **Spec Reference:** (add manually if needed)


### Task: Add input validation for numeric parameters
- **ID:** author-002
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (validation)
- **Priority:** high
- **Status:** completed
- **Description:** Validate numeric parameters (n, target_count, storylet_count) are positive integers within safe limits.
- **Spec Reference:** (add manually if needed)


### Task: Implement authentication/authorization for admin endpoints
- **ID:** author-003
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (security)
- **Priority:** high
- **Status:** pending
- **Description:** Add authentication and authorization checks to restrict access to admin endpoints, especially destructive ones.
- **Spec Reference:** (add manually if needed)


### Task: Test suggest endpoint with mocked services
- **ID:** author-008
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Mock llm_suggest_storylets and test POST /author/suggest with various inputs and fallback scenarios.
- **Spec Reference:** (add manually if needed)


### Task: Test commit endpoint functionality
- **ID:** author-009
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test POST /author/commit adds storylets to database and triggers spatial assignment and improvements.
- **Spec Reference:** (add manually if needed)


### Task: Add check_same_thread=False for SQLite
- **ID:** database-001
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** fix (configuration)
- **Priority:** high
- **Status:** completed
- **Description:** Set check_same_thread=False in create_engine connect_args for SQLite multi-threading support.
- **Spec Reference:** (add manually if needed)


### Task: Test environment variable logic
- **ID:** database-005
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** completed
- **Description:** Mock different environment configurations and verify correct database filename selection.
- **Spec Reference:** (add manually if needed)


### Task: Implement precise cache cleanup
- **ID:** game-003
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** improvement (cache_management)
- **Priority:** high
- **Status:** completed
- **Description:** Modify cleanup_old_sessions() to remove only deleted session IDs from cache rather than arbitrary count.
- **Spec Reference:** (add manually if needed)


### Task: Test state manager retrieval and persistence
- **ID:** game-007
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test get_state_manager() returns same instance for session and properly initializes/persists variables.
- **Spec Reference:** (add manually if needed)


### Task: Test API next storylet selection
- **ID:** game-008
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test POST /api/next with different vars payloads and verify correct storylet selection and fallbacks.
- **Spec Reference:** (add manually if needed)


### Task: Test empty database seeding
- **ID:** seed-005
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** completed
- **Description:** Test seed_if_empty() adds expected number of storylets to fresh database.
- **Spec Reference:** (add manually if needed)


### Task: Test choice normalization functionality
- **ID:** schemas-006
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test StoryletIn with various choice formats (label/set vs text/set_vars) to verify normalization works correctly.
- **Spec Reference:** (add manually if needed)


### Task: 💾 Unified Transaction Management
- **ID:** MEGA-TRANSACTION-MANAGEMENT
- **Stage:** 4 (stage4)
- **File:** multiple
- **Type:** improvement (data_integrity)
- **Priority:** high
- **Status:** pending
- **Description:** Implement comprehensive transaction management across game_logic.py (storylet inserts), auto_improvement.py (improvement operations), story_deepener.py (storylet insertions/updates), and story_smoother.py (batch updates). Ensure atomicity, rollback capabilities, and data consistency.
- **Spec Reference:** (add manually if needed)


### Task: Unify requirement evaluation logic
- **ID:** game-logic-001
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** improvement (code_consistency)
- **Priority:** high
- **Status:** pending
- **Description:** Refactor meets_requirements() to leverage AdvancedStateManager.evaluate_condition() or share common evaluation utility for consistent behavior.
- **Spec Reference:** (add manually if needed)


### Task: Test template rendering functionality
- **ID:** game-logic-007
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test render() correctly substitutes variables and leaves missing placeholders intact, including nested placeholders.
- **Spec Reference:** (add manually if needed)


### Task: Test requirement checking logic
- **ID:** game-logic-008
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test meets_requirements() with numeric comparisons, boolean checks, equality, including edge cases.
- **Spec Reference:** (add manually if needed)


### Task: Test coordinate assignment functionality
- **ID:** spatial-nav-006
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test auto_assign_coordinates() assigns coordinates to storylets with location requirements but no spatial coordinates.
- **Spec Reference:** (add manually if needed)


### Task: Test variable management operations
- **ID:** state-mgr-007
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test set_variable and increment_variable store values correctly, record history, and invalidate cache.
- **Spec Reference:** (add manually if needed)


### Task: Test item operations functionality
- **ID:** state-mgr-008
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test add_item and remove_item handle quantities, defaults, and history recording correctly.
- **Spec Reference:** (add manually if needed)


### Task: 📄 Unified JSON Parsing Framework
- **ID:** MEGA-JSON-PARSING
- **Stage:** 5 (stage5)
- **File:** multiple
- **Type:** improvement (parsing)
- **Priority:** high
- **Status:** pending
- **Description:** Implement robust JSON parsing across llm_service.py (LLM response extraction), story_deepener.py (LLM JSON extraction), and storylet_analyzer.py (requires/choices normalization). Use json.JSONDecoder.raw_decode, stack-based parsing, or OpenAI function calling for reliability.
- **Spec Reference:** (add manually if needed)


### Task: Add prompt sanitization
- **ID:** llm-service-003
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** improvement (security)
- **Priority:** high
- **Status:** pending
- **Description:** Sanitize/escape user-provided strings in prompts to mitigate prompt injection risks.
- **Spec Reference:** (add manually if needed)


### Task: Test improvement decision logic
- **ID:** auto-improve-007
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test should_run_auto_improvement() with various storylets_added values and trigger strings.
- **Spec Reference:** (add manually if needed)


### Task: Test successful improvement run
- **ID:** auto-improve-008
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Mock StorySmoother and StoryDeepener to test successful auto_improve_storylets() execution and result aggregation.
- **Spec Reference:** (add manually if needed)


### Task: Test contextual generation fallback
- **ID:** llm-service-008
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test generate_contextual_storylets() returns hard-coded fallbacks in test mode.
- **Spec Reference:** (add manually if needed)


### Task: Test LLM suggestion fallback
- **ID:** llm-service-009
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test llm_suggest_storylets() returns fallback when no API key set.
- **Spec Reference:** (add manually if needed)


### Task: Test transition analysis
- **ID:** story-deepener-008
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Seed test database with known storylets and verify transition and weak transition counts match expectations.
- **Spec Reference:** (add manually if needed)


### Task: Test problem identification
- **ID:** story-smoother-008
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Create test database with known storylets and verify dead_end_vars, isolated_locations, one_way_connections detection.
- **Spec Reference:** (add manually if needed)


### Task: Test pattern matching functionality
- **ID:** location-mapper-009
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test known location names return expected coordinates defined in patterns.
- **Spec Reference:** (add manually if needed)


### Task: Test storylet coordinate assignment
- **ID:** location-mapper-013
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test assign_coordinates_to_storylets() assigns correct spatial_x and spatial_y with no duplicates.
- **Spec Reference:** (add manually if needed)


### Task: Add database-level analysis optimization
- **ID:** storylet-analyzer-003
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (performance)
- **Priority:** high
- **Status:** pending
- **Description:** Use SQL queries/aggregates to count variable requirements and settings, reducing Python-level loops.
- **Spec Reference:** (add manually if needed)


### Task: Test gap analysis functionality
- **ID:** storylet-analyzer-009
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** high
- **Status:** pending
- **Description:** Test analyze_storylet_gaps() with controlled storylet set and verify all analysis components match expected values.
- **Spec Reference:** (add manually if needed)


### Task: Align API prefixes for consistency
- **ID:** main-002
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** improvement (api_design)
- **Priority:** low
- **Status:** pending
- **Description:** Mount both routers under same base path (e.g., /api/game and /api/author) or document reasoning for current paths.
- **Spec Reference:** (add manually if needed)


### Task: Add environment documentation
- **ID:** main-004
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** improvement (documentation)
- **Priority:** low
- **Status:** pending
- **Description:** Create README or .env.example documenting required environment variables like database connection strings.
- **Spec Reference:** (add manually if needed)


### Task: CORS settings test
- **ID:** main-008
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** test (unit_test)
- **Priority:** low
- **Status:** pending
- **Description:** Verify CORSMiddleware is configured with correct allow_origins, allow_methods parameters.
- **Spec Reference:** (add manually if needed)


### Task: Add accessibility improvements
- **ID:** twee-005
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** improvement (accessibility)
- **Priority:** low
- **Status:** pending
- **Description:** Add tabindex attributes and ARIA labels to interactive elements like compass cells for keyboard navigation.
- **Spec Reference:** (add manually if needed)


### Task: Refactor code organization
- **ID:** twee-006
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** improvement (code_organization)
- **Priority:** low
- **Status:** pending
- **Description:** Move inline CSS and JavaScript into separate files or StoryScripts for better maintainability.
- **Spec Reference:** (add manually if needed)


### Task: Add rate limiting for expensive endpoints
- **ID:** author-007
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (performance)
- **Priority:** low
- **Status:** pending
- **Description:** Implement rate limiting for endpoints that trigger expensive LLM calls or heavy analysis.
- **Spec Reference:** (add manually if needed)


### Task: Add engine disposal function
- **ID:** database-004
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** improvement (resource_management)
- **Priority:** low
- **Status:** pending
- **Description:** Expose shutdown() function to call engine.dispose() during application shutdown.
- **Spec Reference:** (add manually if needed)


### Task: Remove leading whitespace in choice label
- **ID:** seed-002
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** fix (data_quality)
- **Priority:** low
- **Status:** completed
- **Description:** Trim leading space in ' improvise with a rock' choice label.
- **Spec Reference:** (add manually if needed)


### Task: Add more seed variations
- **ID:** seed-003
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** improvement (content_expansion)
- **Priority:** low
- **Status:** pending
- **Description:** Add more seeds covering different locations, times, and variable conditions for richer gameplay.
- **Spec Reference:** (add manually if needed)


### Task: Add model documentation and examples
- **ID:** schemas-003
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** improvement (documentation)
- **Priority:** low
- **Status:** pending
- **Description:** Add docstrings and examples to each model showing expected request/response shapes for API users.
- **Spec Reference:** (add manually if needed)


### Task: Create stronger type schemas for variables
- **ID:** schemas-004
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** improvement (type_safety)
- **Priority:** low
- **Status:** pending
- **Description:** Consider defining specific Pydantic models for variable operations (inc, dec) for type safety and autocompletion.
- **Spec Reference:** (add manually if needed)


### Task: Make WorldDescription storylet_count configurable
- **ID:** schemas-005
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** improvement (configuration)
- **Priority:** low
- **Status:** pending
- **Description:** Consider making storylet_count range (5-50) configurable via environment variables.
- **Spec Reference:** (add manually if needed)


### Task: Extend connectivity analysis metrics
- **ID:** game-logic-006
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** improvement (analytics)
- **Priority:** low
- **Status:** pending
- **Description:** Enhance ensure_storylet_connectivity() with additional metrics like path length, strongly connected components, isolated storylets.
- **Spec Reference:** (add manually if needed)


### Task: Make search radius configurable
- **ID:** spatial-nav-003
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** improvement (configuration)
- **Priority:** low
- **Status:** pending
- **Description:** Expose parameters for _find_free_position() (max radius, step size) for tuning dense maps.
- **Spec Reference:** (add manually if needed)


### Task: Return structured results instead of print statements
- **ID:** spatial-nav-005
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** improvement (code_quality)
- **Priority:** low
- **Status:** pending
- **Description:** Modify methods to return assigned coordinates and provide logging mechanism instead of print statements.
- **Spec Reference:** (add manually if needed)


### Task: Make relationship ranges configurable
- **ID:** state-mgr-003
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** improvement (configuration)
- **Priority:** low
- **Status:** pending
- **Description:** Make clamp range for relationship attributes configurable per attribute or document rationale for [-100,100] range.
- **Spec Reference:** (add manually if needed)


### Task: Document flexible location keywords
- **ID:** state-mgr-005
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** improvement (documentation)
- **Priority:** low
- **Status:** pending
- **Description:** Enumerate and document all supported flexible location keywords (any_realm, any_location, in_vessel) for authors.
- **Spec Reference:** (add manually if needed)


### Task: Make cache expiry configurable
- **ID:** state-mgr-006
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** improvement (configuration)
- **Priority:** low
- **Status:** pending
- **Description:** Allow cache expiry duration to be configurable and provide method to force refresh contextual variables.
- **Spec Reference:** (add manually if needed)


### Task: Create structured result objects
- **ID:** auto-improve-005
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** improvement (type_safety)
- **Priority:** low
- **Status:** pending
- **Description:** Define typed result object (Pydantic model/dataclass) instead of free-form dict with magic keys.
- **Spec Reference:** (add manually if needed)


### Task: Implement async LLM calls
- **ID:** llm-service-007
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** improvement (performance)
- **Priority:** low
- **Status:** pending
- **Description:** Make LLM calls asynchronous to avoid blocking event loop in FastAPI endpoints.
- **Spec Reference:** (add manually if needed)


### Task: Remove external script side effects
- **ID:** story-deepener-007
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** improvement (separation_of_concerns)
- **Priority:** low
- **Status:** pending
- **Description:** Avoid running storylet_map.py in main(), provide separate CLI entry point for analyses.
- **Spec Reference:** (add manually if needed)


### Task: Add proper logging support
- **ID:** location-mapper-005
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (logging)
- **Priority:** low
- **Status:** pending
- **Description:** Replace print() statements with logging calls controlled by configuration for debug visibility.
- **Spec Reference:** (add manually if needed)


### Task: Enhance visualization capabilities
- **ID:** location-mapper-006
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (visualization)
- **Priority:** low
- **Status:** pending
- **Description:** Support more markers (alphabetical/alphanumeric) and display connections or adjacency hints in visualize_locations().
- **Spec Reference:** (add manually if needed)


### Task: Implement persistent mapping option
- **ID:** location-mapper-007
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (state_management)
- **Priority:** low
- **Status:** pending
- **Description:** Provide option to retain location_cache across calls or merge new locations without reassigning all positions.
- **Spec Reference:** (add manually if needed)


### Task: Add testing extensibility hooks
- **ID:** storylet-analyzer-008
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (testing_architecture)
- **Priority:** low
- **Status:** pending
- **Description:** Include hooks to inject custom recommendation logic or danger categorization for different games.
- **Spec Reference:** (add manually if needed)


### Task: Make database seeding asynchronous
- **ID:** main-001
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Ensure seed_if_empty() doesn't block the event loop during startup. Rewrite as async function or use asyncio.to_thread.
- **Spec Reference:** (add manually if needed)


### Task: Add proper shutdown logic
- **ID:** main-003
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** improvement (resource_management)
- **Priority:** medium
- **Status:** pending
- **Description:** Include teardown steps in lifespan context manager for database connections and background tasks.
- **Spec Reference:** (add manually if needed)


### Task: Router registration test
- **ID:** main-006
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Assert FastAPI app contains routes with prefixes /api and /author corresponding to imported routers.
- **Spec Reference:** (add manually if needed)


### Task: Lifespan startup test
- **ID:** main-007
- **Stage:** 1 (stage1)
- **File:** main.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test that lifespan startup event calls create_tables() and seed_if_empty() once using mocks.
- **Spec Reference:** (add manually if needed)


### Task: Implement session persistence
- **ID:** twee-003
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** improvement (user_experience)
- **Priority:** medium
- **Status:** pending
- **Description:** Store sessionId in localStorage or retrieve from backend to maintain continuity across page reloads.
- **Spec Reference:** (add manually if needed)


### Task: Improve error handling
- **ID:** twee-004
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** improvement (error_handling)
- **Priority:** medium
- **Status:** pending
- **Description:** Add more granular error messages for different failure scenarios (invalid inputs, unreachable endpoint).
- **Spec Reference:** (add manually if needed)


### Task: Spatial navigation endpoint tests
- **ID:** twee-009
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** test (integration_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test GET /api/spatial/navigation/{sessionId} and POST /api/spatial/move/{sessionId} endpoints.
- **Spec Reference:** (add manually if needed)


### Task: Assign positions endpoint test
- **ID:** twee-010
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** test (integration_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test POST /api/spatial/assign-positions returns successful status and sets up navigation graph.
- **Spec Reference:** (add manually if needed)


### Task: Frontend error handling test
- **ID:** twee-011
- **Stage:** 1 (stage1)
- **File:** WorldWeaver-Twine-Story.twee
- **Type:** test (frontend_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test frontend functions handle backend errors gracefully using headless browser or mocked fetch.
- **Spec Reference:** (add manually if needed)


### Task: Add duplicate storylet prevention
- **ID:** author-004
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (data_integrity)
- **Priority:** medium
- **Status:** pending
- **Description:** Check for existing storylets with same title before adding to prevent duplicates during commit.
- **Spec Reference:** (add manually if needed)


### Task: Add confirmation for destructive world generation
- **ID:** author-005
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (safety)
- **Priority:** medium
- **Status:** pending
- **Description:** Add confirmation flag (force=true) for generate-world endpoint to prevent accidental data loss.
- **Spec Reference:** (add manually if needed)


### Task: Implement transactional commits
- **ID:** author-006
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** improvement (data_integrity)
- **Priority:** medium
- **Status:** pending
- **Description:** Wrap commit operations in transactions to prevent partial inserts on errors.
- **Spec Reference:** (add manually if needed)


### Task: Test populate endpoint
- **ID:** author-010
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock auto_populate_storylets and test /author/populate with different target_count values.
- **Spec Reference:** (add manually if needed)


### Task: Test generate-world endpoint
- **ID:** author-011
- **Stage:** 2 (stage2)
- **File:** src/api/author.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock world generation services and test database clearing, storylet insertion, and improvement pipeline.
- **Spec Reference:** (add manually if needed)


### Task: Set expire_on_commit configuration
- **ID:** database-002
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Consider setting expire_on_commit=False in sessionmaker if objects need to remain usable after commit.
- **Spec Reference:** (add manually if needed)


### Task: Add directory creation for database path
- **ID:** database-003
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** improvement (error_handling)
- **Priority:** medium
- **Status:** pending
- **Description:** Ensure parent directories exist when DW_DB_PATH points to nested directory or provide clear error.
- **Spec Reference:** (add manually if needed)


### Task: Test session generator lifecycle
- **ID:** database-006
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test get_db() generator yields and closes sessions properly.
- **Spec Reference:** (add manually if needed)


### Task: Test table creation
- **ID:** database-007
- **Stage:** 2 (stage2)
- **File:** src/database.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test create_tables() actually creates tables in SQLite database.
- **Spec Reference:** (add manually if needed)


### Task: Fix default has_pickaxe value
- **ID:** game-002
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** improvement (game_balance)
- **Priority:** medium
- **Status:** pending
- **Description:** Consider setting has_pickaxe to False by default to make "Where's My Pickaxe?" storylet accessible.
- **Spec Reference:** (add manually if needed)


### Task: Use JSON querying for storylet location filtering
- **ID:** game-004
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** improvement (database_optimization)
- **Priority:** medium
- **Status:** pending
- **Description:** Replace string-based contains() filters with SQLAlchemy JSON operators for reliable location queries.
- **Spec Reference:** (add manually if needed)


### Task: Refine error handling with specific exceptions
- **ID:** game-006
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** improvement (error_handling)
- **Priority:** medium
- **Status:** pending
- **Description:** Catch specific exceptions instead of broad Exception types for clearer error responses.
- **Spec Reference:** (add manually if needed)


### Task: Test spatial navigation endpoints
- **ID:** game-009
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test GET /api/spatial/navigation/{session_id} returns correct location, storylet info, and directions.
- **Spec Reference:** (add manually if needed)


### Task: Test spatial movement functionality
- **ID:** game-010
- **Stage:** 2 (stage2)
- **File:** src/api/game.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test POST /api/spatial/move/{session_id} with valid/invalid directions and proper response codes.
- **Spec Reference:** (add manually if needed)


### Task: Normalize choice dictionary formats
- **ID:** seed-001
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** fix (data_consistency)
- **Priority:** medium
- **Status:** pending
- **Description:** Use consistent format for choices across all seed storylets (label/set vs text/set_vars).
- **Spec Reference:** (add manually if needed)


### Task: Document placeholder requirements
- **ID:** seed-004
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** improvement (documentation)
- **Priority:** medium
- **Status:** pending
- **Description:** Document that placeholders like {name} and {danger} require state manager variables.
- **Spec Reference:** (add manually if needed)


### Task: Test idempotent seeding
- **ID:** seed-006
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test seed_if_empty() doesn't create duplicates when called multiple times.
- **Spec Reference:** (add manually if needed)


### Task: Test choice normalization
- **ID:** seed-007
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test all seeded storylet choices can be normalized by _norm_choices() without errors.
- **Spec Reference:** (add manually if needed)


### Task: Test placeholder rendering
- **ID:** seed-008
- **Stage:** 2 (stage2)
- **File:** src/services/seed_data.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test storylets with placeholders render correctly with different variable contexts.
- **Spec Reference:** (add manually if needed)


### Task: Add default empty dict for NextReq.vars
- **ID:** schemas-001
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** improvement (api_usability)
- **Priority:** medium
- **Status:** pending
- **Description:** Set default_factory=dict for NextReq.vars field so clients can omit it when no state updates needed.
- **Spec Reference:** (add manually if needed)


### Task: Enhance choice normalization validation
- **ID:** schemas-002
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** improvement (validation)
- **Priority:** medium
- **Status:** pending
- **Description:** Add type checks in StoryletIn._normalize_choices to ensure input is dict and set_obj is dict, raise ValueError for malformed input.
- **Spec Reference:** (add manually if needed)


### Task: Test NextReq vars default behavior
- **ID:** schemas-007
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test NextReq creation with and without vars field to verify default behavior or validation errors.
- **Spec Reference:** (add manually if needed)


### Task: Test WorldDescription validation
- **ID:** schemas-008
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test WorldDescription with invalid values (short description, out-of-range storylet_count) to ensure validation errors.
- **Spec Reference:** (add manually if needed)


### Task: Test GenerateStoryletRequest defaults
- **ID:** schemas-009
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test that default values for count, themes, and intelligent are correctly applied when fields omitted.
- **Spec Reference:** (add manually if needed)


### Task: Test JSON serialization round-trip
- **ID:** schemas-010
- **Stage:** 3 (stage3)
- **File:** src/models/schemas.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Serialize and deserialize each model to/from JSON to ensure data structures preserved and choice normalization works.
- **Spec Reference:** (add manually if needed)


### Task: Improve LLM exception handling
- **ID:** game-logic-002
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** improvement (error_handling)
- **Priority:** medium
- **Status:** pending
- **Description:** Capture exceptions from LLM calls, log appropriately, and consider retrying or returning fallback response instead of silent failures.
- **Spec Reference:** (add manually if needed)


### Task: Make storylet generation threshold configurable
- **ID:** game-logic-003
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Make the threshold (currently 3) for generating contextual storylets configurable via environment variables or parameters.
- **Spec Reference:** (add manually if needed)


### Task: Add storylet deduplication
- **ID:** game-logic-005
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** improvement (data_integrity)
- **Priority:** medium
- **Status:** pending
- **Description:** Check for existing titles before committing new LLM-generated storylets to avoid duplicates.
- **Spec Reference:** (add manually if needed)


### Task: Test storylet selection and weighting
- **ID:** game-logic-009
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test pick_storylet() with varying requirements and weights to verify correct selection and probability distribution.
- **Spec Reference:** (add manually if needed)


### Task: Test fallback storylet generation
- **ID:** game-logic-010
- **Stage:** 4 (stage4)
- **File:** src/services/game_logic.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock generate_contextual_storylets() and test storylet generation when eligible count below threshold.
- **Spec Reference:** (add manually if needed)


### Task: Validate and parse requires field safely
- **ID:** spatial-nav-001
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** improvement (error_handling)
- **Priority:** medium
- **Status:** pending
- **Description:** Check if requires is string before json.loads(), skip parsing if already dict from ORM.
- **Spec Reference:** (add manually if needed)


### Task: Batch database updates for efficiency
- **ID:** spatial-nav-002
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Collect coordinate updates and commit once to reduce database overhead, use transactions for atomicity.
- **Spec Reference:** (add manually if needed)


### Task: Test spatial position assignment
- **ID:** spatial-nav-007
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test assign_spatial_positions() places all storylets correctly without overlaps and with reasonable relative positioning.
- **Spec Reference:** (add manually if needed)


### Task: Test directional navigation
- **ID:** spatial-nav-008
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test get_directional_navigation() returns accurate neighbor storylets with correct details and requirements.
- **Spec Reference:** (add manually if needed)


### Task: Test movement requirements validation
- **ID:** spatial-nav-009
- **Stage:** 4 (stage4)
- **File:** src/services/spatial_navigator.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test can_move_to_direction() correctly validates player variables against neighbor storylet requirements.
- **Spec Reference:** (add manually if needed)


### Task: Limit change history length
- **ID:** state-mgr-002
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** improvement (memory_management)
- **Priority:** medium
- **Status:** pending
- **Description:** Implement maximum history length or ring buffer to prevent unbounded growth of change_history.
- **Spec Reference:** (add manually if needed)


### Task: Implement proper deep copy utilities
- **ID:** state-mgr-004
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** improvement (data_integrity)
- **Priority:** medium
- **Status:** pending
- **Description:** Provide helper methods to deep copy ItemState and RelationshipState instances to ensure nested structures are cloned.
- **Spec Reference:** (add manually if needed)


### Task: Test relationship updates
- **ID:** state-mgr-009
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test update_relationship creates entries, clamps values, records memories, and updates interaction counts.
- **Spec Reference:** (add manually if needed)


### Task: Test condition evaluation logic
- **ID:** state-mgr-010
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test evaluate_condition with relationship, item, environment, location, and numeric conditions.
- **Spec Reference:** (add manually if needed)


### Task: Test contextual variables caching
- **ID:** state-mgr-011
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test get_contextual_variables caching behavior and cache invalidation triggers.
- **Spec Reference:** (add manually if needed)


### Task: Test state export/import functionality
- **ID:** state-mgr-012
- **Stage:** 4 (stage4)
- **File:** src/services/state_manager.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test export/import of state with all components and verify data integrity after round-trip.
- **Spec Reference:** (add manually if needed)


### Task: Make improvement triggers configurable
- **ID:** auto-improve-002
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Allow configuration of storylets_added threshold and trigger list via environment variables or application settings.
- **Spec Reference:** (add manually if needed)


### Task: Implement asynchronous improvement execution
- **ID:** auto-improve-003
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Offload improvement process to background task (Celery/FastAPI background tasks) for faster API responses.
- **Spec Reference:** (add manually if needed)


### Task: 🧪 Unified Testing Architecture
- **ID:** MEGA-TESTING-ARCHITECTURE
- **Stage:** 5 (stage5)
- **File:** multiple
- **Type:** improvement (testing_architecture)
- **Priority:** medium
- **Status:** pending
- **Description:** Implement comprehensive testing architecture across author.py (dependency injection for services), auto_improvement.py (smoother/deepener injection), llm_service.py (mockable OpenAI client), and storylet_analyzer.py (extensibility hooks). Enable easy mocking, test isolation, and dependency injection patterns.
- **Spec Reference:** (add manually if needed)


### Task: Test improvement failure handling
- **ID:** auto-improve-009
- **Stage:** 5 (stage5)
- **File:** src/services/auto_improvement.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock smoother/deepener to raise exceptions and verify proper error handling and rollback.
- **Spec Reference:** (add manually if needed)


### Task: Centralize configuration management
- **ID:** llm-service-001
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Move environment checks and API key retrieval into dedicated configuration class to avoid scattered environment logic.
- **Spec Reference:** (add manually if needed)


### Task: 📝 Unified Logging Framework
- **ID:** MEGA-LOGGING-STANDARDIZATION
- **Stage:** 5 (stage5)
- **File:** multiple
- **Type:** improvement (logging)
- **Priority:** medium
- **Status:** pending
- **Description:** Standardize logging across llm_service.py (replace print statements), auto_improvement.py (structured logging), location_mapper.py (debug visibility), and story_deepener.py (configurable levels). Implement consistent logging patterns, configurable levels, and structured output.
- **Spec Reference:** (add manually if needed)


### Task: Add storylet validation and normalization
- **ID:** llm-service-006
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** improvement (validation)
- **Priority:** medium
- **Status:** pending
- **Description:** Add explicit validation of LLM-returned storylets (weights are floats, requires is dict, choices are lists).
- **Spec Reference:** (add manually if needed)


### Task: Test JSON extraction failure handling
- **ID:** llm-service-010
- **Stage:** 5 (stage5)
- **File:** src/services/llm_service.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock OpenAI response with invalid JSON and test generate_world_storylets() fallback behavior.
- **Spec Reference:** (add manually if needed)


### Task: Make thresholds and limits configurable
- **ID:** story-deepener-001
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Expose parameters for weak transition count (currently 3) and coherence threshold (0.6) via arguments or environment.
- **Spec Reference:** (add manually if needed)


### Task: Make topic extraction configurable
- **ID:** story-deepener-002
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Allow topic keywords to be configured externally or learned from world description instead of fixed lists.
- **Spec Reference:** (add manually if needed)


### Task: Improve storylet matching logic
- **ID:** story-deepener-003
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** improvement (code_consistency)
- **Priority:** medium
- **Status:** pending
- **Description:** Consider merging with AdvancedStateManager.evaluate_condition() for more robust requirement evaluation.
- **Spec Reference:** (add manually if needed)


### Task: 🗄️ Unified Database Access Patterns
- **ID:** MEGA-DATABASE-ACCESS
- **Stage:** 5 (stage5)
- **File:** multiple
- **Type:** improvement (database_architecture)
- **Priority:** medium
- **Status:** pending
- **Description:** Standardize database access across story_deepener.py (SQLAlchemy sessions), story_smoother.py (session adoption), and storylet_analyzer.py (read-only sessions). Implement connection pooling, session management, and consistent query patterns.
- **Spec Reference:** (add manually if needed)


### Task: Test bridge storylet creation
- **ID:** story-deepener-009
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock _call_llm() and test _create_choice_destination() and _create_transition_bridge() produce expected storylets.
- **Spec Reference:** (add manually if needed)


### Task: Test choice preview functionality
- **ID:** story-deepener-010
- **Stage:** 5 (stage5)
- **File:** src/services/story_deepener.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test add_choice_previews() adds appropriate → hints without modifying existing suffixes.
- **Spec Reference:** (add manually if needed)


### Task: Implement contextual location assignment
- **ID:** story-smoother-001
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** improvement (ai_enhancement)
- **Priority:** medium
- **Status:** pending
- **Description:** Derive possible locations from world description or existing storylets instead of keyword heuristics.
- **Spec Reference:** (add manually if needed)


### Task: Improve connection logic
- **ID:** story-smoother-002
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** improvement (game_logic)
- **Priority:** medium
- **Status:** pending
- **Description:** Build connections based on variables, themes, or spatial proximity instead of random movement connections.
- **Spec Reference:** (add manually if needed)


### Task: Implement consistent dry run mode
- **ID:** story-smoother-003
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** improvement (testing_support)
- **Priority:** medium
- **Status:** pending
- **Description:** Update in-memory structures during dry run but skip DB writes to allow subsequent call accuracy.
- **Spec Reference:** (add manually if needed)


### Task: Add performance optimizations
- **ID:** story-smoother-004
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Profile storylet loading/analysis and consider adding database indexes or SQL query optimizations.
- **Spec Reference:** (add manually if needed)


### Task: Enhance return path requirements
- **ID:** story-smoother-005
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** improvement (game_logic)
- **Priority:** medium
- **Status:** pending
- **Description:** Inspect player state variables when adding return paths to ensure return choice availability is appropriate.
- **Spec Reference:** (add manually if needed)


### Task: Test exit choice generation
- **ID:** story-smoother-009
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test generate_exit_choices() produces choices with appropriate text and location settings.
- **Spec Reference:** (add manually if needed)


### Task: Test variable requirement storylets
- **ID:** story-smoother-010
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test generate_variable_requirement_storylets() creates storylets requiring dead-end variables.
- **Spec Reference:** (add manually if needed)


### Task: Test spatial integration fixes
- **ID:** story-smoother-011
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test fix_spatial_integration() assigns locations to storylets and adds movement choices correctly.
- **Spec Reference:** (add manually if needed)


### Task: Test integration with deepening
- **ID:** story-smoother-012
- **Stage:** 5 (stage5)
- **File:** src/services/story_smoother.py
- **Type:** test (integration_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Write integration tests combining smoothing and deepening to ensure coherent, connected storylet graph.
- **Spec Reference:** (add manually if needed)


### Task: Make location patterns configurable
- **ID:** location-mapper-001
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Allow games to supply custom location patterns or extend defaults via configuration files for different genres.
- **Spec Reference:** (add manually if needed)


### Task: Enhance location name matching
- **ID:** location-mapper-002
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (matching_algorithm)
- **Priority:** medium
- **Status:** pending
- **Description:** Incorporate synonyms or fuzzy matching (difflib, word2vec) to improve partial match algorithm and reduce hash fallbacks.
- **Spec Reference:** (add manually if needed)


### Task: Make coordinate space flexible
- **ID:** location-mapper-003
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (scalability)
- **Priority:** medium
- **Status:** pending
- **Description:** Allow customization of coordinate range beyond ±10 to reduce collisions in dense worlds.
- **Spec Reference:** (add manually if needed)


### Task: Optimize position placement algorithm
- **ID:** location-mapper-004
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Replace spiral search with more efficient algorithm (grid occupancy map, k-d tree) for finding nearest free coordinates.
- **Spec Reference:** (add manually if needed)


### Task: Test partial match scoring
- **ID:** location-mapper-010
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test _find_partial_match() picks best matching pattern for complex location names.
- **Spec Reference:** (add manually if needed)


### Task: Test hash fallback mechanism
- **ID:** location-mapper-011
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test _hash_to_coordinates() produces deterministic coordinates for unusual location names within expected range.
- **Spec Reference:** (add manually if needed)


### Task: Test collision resolution
- **ID:** location-mapper-012
- **Stage:** 6 (stage6)
- **File:** src/services/location_mapper.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test _find_free_position() assigns unique positions when multiple locations map to same coordinates.
- **Spec Reference:** (add manually if needed)


### Task: Make analysis heuristics configurable
- **ID:** storylet-analyzer-001
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (configuration)
- **Priority:** medium
- **Status:** pending
- **Description:** Expose thresholds for danger levels, location connectivity, and recommendation limits via environment variables.
- **Spec Reference:** (add manually if needed)


### Task: Implement dynamic recommendations
- **ID:** storylet-analyzer-002
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (extensibility)
- **Priority:** medium
- **Status:** pending
- **Description:** Extend generate_gap_recommendations() to handle arbitrary variables with generic suggestions and configurable variable lists.
- **Spec Reference:** (add manually if needed)


### Task: Implement analysis result caching
- **ID:** storylet-analyzer-004
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (performance)
- **Priority:** medium
- **Status:** pending
- **Description:** Cache analyze_storylet_gaps() results for short period with invalidation when storylets change.
- **Spec Reference:** (add manually if needed)


### Task: Normalize JSON handling at model layer
- **ID:** storylet-analyzer-005
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (data_consistency)
- **Priority:** medium
- **Status:** pending
- **Description:** Ensure requires and choices fields are always Python structures by the time they reach analysis functions.
- **Spec Reference:** (add manually if needed)


### Task: Add LLM guardrails for targeted generation
- **ID:** storylet-analyzer-006
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (ai_reliability)
- **Priority:** medium
- **Status:** pending
- **Description:** Include recommendations explicitly in system prompt and use function calling/schema enforcement for generated storylets.
- **Spec Reference:** (add manually if needed)


### Task: Implement parallel safety measures
- **ID:** storylet-analyzer-007
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** improvement (concurrency)
- **Priority:** medium
- **Status:** pending
- **Description:** Guard against race conditions with read-only database sessions and thread-safe cache for frequent calls.
- **Spec Reference:** (add manually if needed)


### Task: Test recommendation generation
- **ID:** storylet-analyzer-010
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test generate_gap_recommendations() returns appropriate suggestions with correct themes and priorities.
- **Spec Reference:** (add manually if needed)


### Task: Test targeted storylet generation
- **ID:** storylet-analyzer-011
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Mock llm_suggest_storylets() and test generate_targeted_storylets() constructs prompts and returns expected storylets.
- **Spec Reference:** (add manually if needed)


### Task: Test AI learning context
- **ID:** storylet-analyzer-012
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test get_ai_learning_context() returns correct context with all expected analysis components.
- **Spec Reference:** (add manually if needed)


### Task: Test successful pattern identification
- **ID:** storylet-analyzer-013
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test _identify_successful_patterns() returns appropriate messages for various danger distributions and location flows.
- **Spec Reference:** (add manually if needed)


### Task: Test JSON normalization robustness
- **ID:** storylet-analyzer-014
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (unit_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Test string fields for requires and choices are properly parsed and invalid JSON handled gracefully.
- **Spec Reference:** (add manually if needed)


### Task: Test performance with large datasets
- **ID:** storylet-analyzer-015
- **Stage:** 6 (stage6)
- **File:** src/services/storylet_analyzer.py
- **Type:** test (performance_test)
- **Priority:** medium
- **Status:** pending
- **Description:** Measure execution time of analyze_storylet_gaps() with large number of storylets and ensure acceptable performance.
- **Spec Reference:** (add manually if needed)

