# 05-domain-state-manager.md

## State Manager Domain Specification

### Persistence Model
- Session state persisted in DB (SessionVars).
- Inventory, relationships, environment tracked per session.
- Recovery guarantees: sessions can be restored from DB at any time.

### Inventory/Environment Relationships
- Inventory supports multi-dimensional items, quantities, properties.
- Environment tracks time, weather, danger, mood modifiers.
- Relationships between inventory and environment are explicit.

### Cache Cleanup
- Only deleted sessions trigger cache cleanup.
- Precise matching for session removal in cache and DB.

### Recovery Guarantees
- Session state can be exported/imported for save/load.
- Change history tracked for rollback/debugging.

### Testing
- Tests for session recovery and cache cleanup in `true_tests/api/test_game_cache_cleanup.py`.

### Definition of Done
- All session state is persistent and recoverable.
- Inventory/environment relationships are documented and tested.
- Cache cleanup is precise and reliable.
