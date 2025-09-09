# 08-observability-and-errors.md

## Observability & Error Handling Specification

### Structured Logging
- Key events (storylet create/update, spatial map, auto-improvement) are logged.
- Logs are structured, actionable, and non-sensitive.

### Error Envelopes
- All errors are wrapped in consistent envelopes.
- Error messages are actionable and do not leak sensitive data.

### Audit Trail
- Full audit trail for storylet improvements and navigation changes.
- Console and file logging available for admin review.

### Logging Policy
- Logging policy documented and enforced in code.
- Error envelope structure reviewed and tested.

### Testing
- Tests for error logging and envelope consistency in `true_tests/api/`.

### Definition of Done
- All key events are logged and auditable.
- Error envelopes are consistent and safe.
- Logging tests pass for all endpoints.
