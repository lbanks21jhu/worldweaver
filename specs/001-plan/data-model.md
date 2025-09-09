# Phase 1: Data Model

## Entities

### Storylet
- Fields: id (int, PK), title (str, unique, case-insensitive), text_template (str), requires (JSON/dict), choices (JSON/list), weight (float), spatial_x (int), spatial_y (int)
- Validation: title unique, choices normalized, requires must include location

### SessionVars
- Fields: session_id (str, PK), vars (JSON/dict), updated_at (datetime)
- Validation: session_id unique

### Inventory (per session)
- Fields: item_id (str), name (str), quantity (int), properties (dict)

### Relationship (per session)
- Fields: entity_a (str), entity_b (str), trust (float), respect (float), interaction_count (int), memory_fragments (list)

### Environment (per session)
- Fields: time_of_day (str), weather (str), danger_level (int), mood_modifiers (dict)

## Relationships
- SessionVars links to Inventory, Relationship, Environment by session_id
- Storylet choices may set variables that affect session state

## State Transitions
- Storylet creation → spatial assignment → auto-improvement
- Session updates via API endpoints
