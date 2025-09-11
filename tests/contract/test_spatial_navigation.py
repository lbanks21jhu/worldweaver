"""
Contract test for GET /api/spatial/navigation/{session_id}
"""

import pytest
import httpx


@pytest.mark.asyncio
async def test_get_spatial_navigation_contract():
    session_id = "test-session"
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get(f"/api/spatial/navigation/{session_id}")
        assert response.status_code == 200
        data = response.json()
        # Validate response schema
        assert "position" in data and isinstance(data["position"], dict)
        assert "x" in data["position"] and isinstance(data["position"]["x"], int)
        assert "y" in data["position"] and isinstance(data["position"]["y"], int)
        assert "directions" in data and isinstance(data["directions"], list)
        # Edge case: directions should only include valid compass points
        valid_directions = {"N", "NE", "E", "SE", "S", "SW", "W", "NW"}
        for d in data["directions"]:
            assert d in valid_directions
