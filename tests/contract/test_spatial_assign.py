"""
Contract test for POST /api/spatial/assign-positions
"""

import pytest
import httpx


@pytest.mark.asyncio
async def test_post_spatial_assign_positions_contract():
    payload = {"positions": [{"storylet_id": 1, "x": 0, "y": 0}]}
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/api/spatial/assign-positions", json=payload)
        assert response.status_code == 200
        data = response.json()
        # Validate response schema
        assert "assigned" in data and isinstance(data["assigned"], list)
        for a in data["assigned"]:
            assert "storylet_id" in a and isinstance(a["storylet_id"], int)
            assert "x" in a and isinstance(a["x"], int)
            assert "y" in a and isinstance(a["y"], int)
        # Edge case: assign to invalid storylet_id
        bad_payload = {"positions": [{"storylet_id": 9999, "x": 0, "y": 0}]}
        bad_response = await client.post(
            "/api/spatial/assign-positions", json=bad_payload
        )
        assert bad_response.status_code in (400, 404)
