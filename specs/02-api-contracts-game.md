# 02-api-contracts-game.md

## Endpoints

| Route                          | Method | Purpose                                  | Auth | Request Schema         | Response Schema         | Side Effects         | Idempotency/Rate Limit | Negative Tests                |
|--------------------------------|--------|------------------------------------------|------|-----------------------|------------------------|----------------------|------------------------|-------------------------------|
| /api/next                      | POST   | Get next storylet for session            | None | NextReq               | NextResp               | DB write (session)   | Yes                    | No eligible storylet          |
| /api/state/{session_id}        | GET    | Get session state summary                | None | None                  | {state_summary}        | None                 | Yes                    | Invalid session               |
| /api/state/{session_id}/relationship | POST | Update relationship between entities     | None | entity_a, entity_b, changes, memory | {relationship} | DB write (session)   | Yes                    | Invalid entities, DB error    |
| /api/state/{session_id}/item   | POST   | Add item to inventory                    | None | item_id, name, quantity, properties | {item}         | DB write (session)   | Yes                    | Invalid item, DB error        |
| /api/state/{session_id}/environment | POST | Update environment conditions            | None | changes:dict          | {environment}          | DB write (session)   | Yes                    | Invalid changes, DB error     |
| /api/cleanup-sessions          | POST   | Cleanup old sessions                     | None | None                  | {success, removed}     | DB delete, cache     | Yes                    | DB error                      |
| /api/spatial/navigation/{session_id} | GET | Get navigation options                   | None | None                  | {directions, location} | None                 | Yes                    | Invalid location, DB error    |
| /api/spatial/move/{session_id} | POST   | Move player in direction                 | None | direction:str         | {success, new_location}| DB write (session)   | Yes                    | Invalid direction, blocked    |
| /api/spatial/map               | GET    | Get spatial map data                     | None | None                  | {map, directions}      | None                 | Yes                    | DB error                      |
| /api/spatial/assign-positions  | POST   | Assign spatial positions to storylets    | None | None                  | {success, positions}   | DB update            | Yes                    | DB error                      |

- **Request/Response Schemas**:  
  - See `src/models/schemas.py` for Pydantic models.
- **Side Effects**:  
  - DB writes, session updates, cache cleanup.
- **Idempotency**:  
  - Movement, state updates are repeatable.
- **Rate Limits**:  
  - None enforced, but bulk ops are capped.
- **Negative Tests**:  
  - Invalid direction, blocked movement, missing session, DB error.
