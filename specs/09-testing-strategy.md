# 09-testing-strategy.md

## Testing Strategy Specification

### Test Matrix
- Unit, integration, and async tests for all subsystems.
- Tests run in isolation and clean up after themselves.
- Race-condition simulations for storylet creation and session updates.

### Contract Tests
- Contract tests for every endpoint (success + failure cases).
- Regression tests for known frontend quirks (e.g., Twine `<br>` normalization).

### Performance Tests
- Canary tests for large sessions/maps to ensure scalability.
- Metrics logged for performance analysis.

### Coverage Goals
- 100% coverage for critical flows (storylet creation, navigation, state updates).
- Coverage matrix documented and updated regularly.

### Definition of Done
- All subsystems have unit, integration, and contract tests.
- Race-condition and performance tests pass.
- Coverage goals are met and documented.
