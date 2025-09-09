# 04-domain-spatial.md

## Spatial Domain Specification

### Semantics
- Locations mapped semantically (forest → west, mountain → north, etc.).
- 8-direction navigation supported (N, NE, E, SE, S, SW, W, NW).
- Coordinate integrity enforced via SpatialNavigator and LocationMapper.

### Navigation
- Compass navigation available immediately after world generation.
- All storylets must be reachable via spatial map.
- Bulk assignment and dry-run logging for coordinate fixes.

### Edge Cases & Fallbacks
- Handles isolated locations, dead-ends, and one-way connections.
- Robust fallbacks for invalid or missing coordinates.
- Dry-run mode for safe testing.

### Testing
- Integration tests for navigation in `tests/integration/test_spatial_navigation.py`.
- 100% coverage for storylets with locations.

### Definition of Done
- All storylets have valid coordinates and are reachable.
- Navigation tests pass for all directions and edge cases.
- No broken navigation states.
