# 10-non-functional.md

## Non-Functional Requirements Specification

### Reliability
- Health endpoint always returns `{ ok: true, time: <UTC> }`.
- Startup/shutdown hooks are deterministic and tested.

### Performance
- Cold start and P95 handler latency targets defined and monitored.
- LLM timeout bounds enforced for all endpoints.

### Safety
- No silent failures; all errors are logged and surfaced.
- Error envelopes are explicit and non-leaky.

### Observability
- Structured logs for key events and error conditions.
- Audit trail for storylet creation, spatial updates, auto-improvement.

### Accessibility & UX
- Inputs normalized for Twine/IF surfaces.
- No broken navigation; informative errors for all failures.

### Definition of Done
- All non-functional requirements are documented and tested.
- Reliability, performance, safety, and accessibility goals are met.
