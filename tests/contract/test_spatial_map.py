"""
Contract test for GET /api/spatial/map
"""

import pytest
import httpx


@pytest.mark.asyncio
async def test_get_spatial_map_contract():
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/api/spatial/map")
        assert response.status_code == 200
        data = response.json()
        # Validate response schema
        assert "storylets" in data and isinstance(data["storylets"], list)
        for s in data["storylets"]:
            assert "id" in s and isinstance(s["id"], int)
            assert "title" in s and isinstance(s["title"], str)
            assert "spatial_x" in s and isinstance(s["spatial_x"], int)
            assert "spatial_y" in s and isinstance(s["spatial_y"], int)
        # Edge case: map should not contain duplicate coordinates
        coords = set()
        for s in data["storylets"]:
            coord = (s["spatial_x"], s["spatial_y"])
            assert coord not in coords
            coords.add(coord)
