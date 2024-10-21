from app.health.models.health_model import HealthLiveStatus
import pytest


@pytest.mark.asyncio
async def test_get_health_live(async_client, auth_header):
    # Act
    response = await async_client.post("/api/v1/health:live", headers=auth_header)
    # Assert
    assert response.status_code == 200
    assert response.json() == {"state": HealthLiveStatus.LIVE}


@pytest.mark.asyncio
async def test_get_health(async_client, auth_header):
    # Act
    response = await async_client.get("/api/v1/health/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_create_health(async_client, auth_header):
    # Act
    response = await async_client.post("/api/v1/health/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_update_health(async_client, auth_header):
    # Act
    response = await async_client.patch("/api/v1/health/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_delete_health(async_client, auth_header):
    # Act
    response = await async_client.delete("/api/v1/health/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_replace_health(async_client, auth_header):
    # Act
    response = await async_client.put("/api/v1/health/", headers=auth_header)
    # Assert
    assert response.status_code == 405
