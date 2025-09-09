# Quickstart

## Setup
1. Clone repo and create virtualenv
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with any needed variables (e.g., DW_DB_PATH)
4. Run: `uvicorn main:app --reload`

## Usage
- Health check: GET `/health`
- Author endpoints: POST `/author/suggest`, `/author/commit`, `/author/populate`, etc.
- Game endpoints: POST `/api/next`, `/api/state/*`, `/api/spatial/navigation/{session_id}`, etc.
- All endpoints documented in OpenAPI at `/docs`

## Testing
- Run all tests: `pytest tests/ true_tests/`
- Integration tests cover spatial navigation, authoring, auto-improvement
- Negative tests for duplicates, LLM failures, edge cases

## Notes
- App runs without OpenAI key (LLM calls fallback)
- All storylets auto-assigned spatial coordinates and improved
- Minimal dependencies, readable code
