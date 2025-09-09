"""
Contract test for POST /api/spatial/move/{session_id}
"""
import pytest
import httpx

@pytest.mark.asyncio
async def test_post_spatial_move_contract():
    session_id = "test-session"
    payload = {"direction": "N"}
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post(f"/api/spatial/move/{session_id}", json=payload)
        assert response.status_code == 200
        data = response.json()
        # Validate response schema
        assert "result" in data and isinstance(data["result"], str)
        assert "new_position" in data and isinstance(data["new_position"], dict)
        assert "x" in data["new_position"] and isinstance(data["new_position"]["x"], int)
        assert "y" in data["new_position"] and isinstance(data["new_position"]["y"], int)
        # Edge case: try moving in an invalid direction
        bad_payload = {"direction": "INVALID"}
        bad_response = await client.post(f"/api/spatial/move/{session_id}", json=bad_payload)
        assert bad_response.status_code in (400, 422)
