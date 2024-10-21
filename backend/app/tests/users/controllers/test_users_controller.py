import pytest

from app.common.core.settings import settings


@pytest.mark.asyncio
async def test_get_user(async_client, test_user_id) -> None:
    # Act
    response = await async_client.get(
        f"/api/v1/users/{test_user_id}",
        headers={
            "content-type": "application/json",
            "X-Secret-Token": settings.X_SECRET_TOKEN,
        },
    )
    # Assert
    assert response.status_code == 200


# def test_list_users(client: TestClient) -> None:
#     response = client.get("/api/v1/users/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 405


@pytest.mark.asyncio
async def test_create_user(async_client) -> None:
    # Act
    response = await async_client.post(
        "/api/v1/users/",
        headers={
            "content-type": "application/json",
            "X-Secret-Token": settings.X_SECRET_TOKEN,
        },
        json={"nickname": "tester", "email": "tester@mail.me"},
    )
    # Assert
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user(async_client, test_user_id) -> None:
    # Act
    response = await async_client.patch(
        f"/api/v1/users/{test_user_id}",
        headers={
            "content-type": "application/json",
            "X-Secret-Token": settings.X_SECRET_TOKEN,
        },
        json={"avatar": "https://avatar.me/svg?seed=batman"},
    )
    # Assert
    assert response.status_code == 200


# def test_delete_user(client: TestClient) -> None:
#     response = client.delete("/api/v1/users/{userId}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 405


# def test_replace_user(client: TestClient) -> None:
#     response = client.put("/api/v1/users/{userId}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 405


# def test_get_user_account(client: TestClient) -> None:
#     # TODO: Implement test
#     pass


# def test_update_user_account(client: TestClient) -> None:
#     response = client.push("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 405


# def test_create_user_account(client: TestClient) -> None:
#     response = client.post("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 403


# def test_delete_user_account(client: TestClient) -> None:
#     response = client.delete("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 403


# def test_replace_user_account(client: TestClient) -> None:
#     response = client.put("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
#     assert response.status_code == 403
