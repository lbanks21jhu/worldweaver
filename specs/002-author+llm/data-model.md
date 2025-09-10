# Data Model for Epic 1: API Contracts Complete

## Entities
- Storylet
  - Fields: id, title, choices, requirements, location, side effects
  - Relationships: belongs to author/game endpoint
- Author Endpoint
  - Fields: request schema, response schema, side effects, idempotency
- Game Endpoint
  - Fields: request schema, response schema, side effects, idempotency

## Validation Rules
- Storylet titles must be unique (case-insensitive)
- Choices and requirements must be normalized
- Requests must match documented schemas
- Responses must match documented schemas

## State Transitions
- Storylet creation: validate uniqueness, normalize choices/requirements
- Storylet update: validate schema, document side effects
- Storylet deletion: ensure idempotency, document side effects

---
All entities and validation rules will be reflected in OpenAPI contracts and test cases.
