# 00-architecture.md

## System Diagram & High-Level Flow

- **FastAPI app**:  
  - Routers: `/api/game`, `/author`
  - Middleware: CORS, async lifespan hooks
- **Services**:  
  - `state_manager.py`: Tracks session variables, inventory, relationships, environment.
  - `spatial_navigator.py`: Assigns/validates coordinates, enables 8-direction navigation.
  - `auto_improvement.py`: Smoothing/deepening after storylet creation.
  - `llm_service.py`: Contextual storylet generation, fallback logic, OpenAI integration.
  - `storylet_analyzer.py`: Gap analysis, recommendations.
- **Models**:  
  - Storylet: title (unique), text_template, requires, choices, weight, spatial_x/y.
  - SessionVars: session_id, vars, updated_at.
  - Inventory/Relationship/Environment: tracked per session.
- **Control Flow**:
  - Author/game endpoints → DB insert → spatial assignment → auto-improvement.
  - Navigation: spatial map, movement, coordinate validation.
  - Session updates: state manager, DB persistence, cache cleanup.
- **Async Boundaries**:
  - Startup: table creation, seeding (background).
  - LLM calls: async, timeout/retry, fallback.
  - DB ops: non-blocking, background tasks for bulk ops.
- **Failure Modes**:
  - LLM timeout: fallback storylets, error envelope.
  - Duplicate storylets: case-insensitive skip, error logging.
  - Invalid spatial mapping: dry-run, logging, fallback assignment.
  - Race conditions: DB rollback, test coverage.
- **Observability**:
  - Structured logs for storylet creation, spatial updates, auto-improvement.
  - Error envelopes: actionable, non-sensitive.
