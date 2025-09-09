# Phase 0: Research

## Unknowns & Clarifications
- Language/Version: Python 3.11+ (confirmed by requirements.txt)
- Primary Dependencies: FastAPI, SQLAlchemy, Pydantic, python-dotenv, uvicorn (dev only)
- Storage: SQLite (via DW_DB_PATH, local file)
- Testing: pytest, pytest-asyncio, httpx; suites in tests/ and true_tests/
- Target Platform: Linux server (local dev), no frontend
- Project Type: Single backend API (no frontend, no mobile)
- Performance Goals: FastAPI default, no explicit perf targets; keep code readable and maintainable
- Constraints: Minimal dependencies, readable code, no blocking calls in request handlers, must run without OpenAI key
- Scale/Scope: Single-user/local dev, extensible for future multi-user

## Best Practices
- Use FastAPI for async API, SQLAlchemy for DB, Pydantic for schemas
- Seed DB on startup, expose health endpoint, mount routers
- Use permissive CORS for local dev
- All storylets must have spatial coordinates and pass auto-improvement
- Author endpoints must support LLM opt-out (fallbacks)
- All changes must be tested and reviewed

## Alternatives Considered
- PostgreSQL: rejected for simplicity, SQLite preferred
- More dependencies: rejected for minimalism
- Frontend: out of scope

## Decision
- Proceed with FastAPI + SQLAlchemy + Pydantic + python-dotenv, SQLite storage, pytest for tests
- No frontend, no auth, no prod scaling
- All endpoints and services must be testable and documented
