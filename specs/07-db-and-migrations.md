# 07-db-and-migrations.md

## Database & Migrations Specification

### Idempotent Migrations
- All migrations are idempotent and safe to run multiple times.
- Explicit types, constraints, and defaults for all columns.
- No destructive operations without explicit confirmation.

### Schema
- Storylet table: unique title, spatial_x/y, requires, choices, weight.
- SessionVars table: session_id, vars, updated_at.
- Inventory, relationships, environment tracked per session.

### Migration Workflow
- Confirmation rituals required for destructive changes.
- Dry-run mode available for migration testing.

### Testing
- Edge case tests for migrations in `tests/database/`.
- Negative tests for destructive ops.

### Definition of Done
- All migrations are idempotent and safe.
- Schema is explicit and documented.
- Migration tests pass for all edge cases.
