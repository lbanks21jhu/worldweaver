"""
Integration test for 8-direction movement and edge cases
"""

import pytest
import httpx


@pytest.mark.asyncio
async def test_eight_direction_movement():
    session_id = "test-session"
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        for direction in directions:
            response = await client.post(
                f"/api/spatial/move/{session_id}", json={"direction": direction}
            )
            assert response.status_code == 200
            data = response.json()
            assert "new_position" in data and isinstance(data["new_position"], dict)
            assert "x" in data["new_position"] and isinstance(
                data["new_position"]["x"], int
            )
            assert "y" in data["new_position"] and isinstance(
                data["new_position"]["y"], int
            )
        # Edge case: try moving beyond map boundaries
        # (Assume map is 0 <= x,y <= 10 for test)
        response = await client.post(
            f"/api/spatial/move/{session_id}", json={"direction": "N"}
        )
        data = response.json()
        assert 0 <= data["new_position"]["x"] <= 10
        assert 0 <= data["new_position"]["y"] <= 10
