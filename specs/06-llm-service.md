# 06-llm-service.md

## LLM Service Specification

### Async, Timeout, and Retry Policy
- All LLM calls are async and non-blocking.
- Timeout and retry logic implemented for reliability.
- Fallback storylets provided on timeout or error.

### Deterministic Fallbacks
- Fallback logic ensures consistent user experience.
- Fallback storylets are contextually relevant and non-generic.

### Logging & Error Handling
- All LLM errors are logged with actionable messages.
- Error envelopes are consistent and non-leaky.
- Sensitive data is redacted in logs.

### Customization
- Algorithms and triggers can be configured via `auto_improvement.py`.
- Opt-out flags available for auto-improvement.

### Testing
- Negative tests for LLM failures in `true_tests/api/`.
- Timeout/retry logic tested for all endpoints.

### Definition of Done
- All LLM calls are async, reliable, and have robust fallbacks.
- Errors are logged and surfaced in API responses.
- Negative tests for LLM failures pass.
