"""
Integration test for coordinate assignment and fallbacks
"""
import pytest
import httpx

@pytest.mark.asyncio
async def test_coordinate_assignment_and_fallbacks():
    payload = {"positions": [{"storylet_id": 1, "x": 0, "y": 0}]}
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/api/spatial/assign-positions", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "assigned" in data and isinstance(data["assigned"], list)
        for a in data["assigned"]:
            assert "storylet_id" in a and isinstance(a["storylet_id"], int)
            assert "x" in a and isinstance(a["x"], int)
            assert "y" in a and isinstance(a["y"], int)
        # Edge case: fallback if position already taken
        payload_conflict = {"positions": [{"storylet_id": 2, "x": 0, "y": 0}]}
        conflict_response = await client.post("/api/spatial/assign-positions", json=payload_conflict)
        assert conflict_response.status_code in (200, 409)
