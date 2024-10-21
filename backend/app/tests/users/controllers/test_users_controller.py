import pytest


@pytest.mark.asyncio
async def test_get_user(async_client, test_user_id, auth_header) -> None:
    # Act
    response = await async_client.get(
        f"/api/v1/users/{test_user_id}",
        headers=auth_header,
    )
    # Assert
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_user(async_client, auth_header) -> None:
    # Act
    response = await async_client.post(
        "/api/v1/users/",
        headers=auth_header,
        json={"nickname": "batman", "email": "batman@mail.me"},
    )
    # Assert
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user(async_client, test_user_id, auth_header) -> None:
    # Act
    response = await async_client.patch(
        f"/api/v1/users/{test_user_id}",
        headers=auth_header,
        json={"avatar": "https://avatar.me/svg?seed=batman"},
    )
    # Assert
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_user_account(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.get(
        f"/api/v1/users/{test_user_id}/account/", headers=auth_header
    )
    # Assert
    assert response.status_code == 200


# +-------------------+
# | Forbidden Methods |
# +-------------------+


@pytest.mark.asyncio
async def test_create_user_account(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.post(
        f"/api/v1/users/{test_user_id}/account/", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_delete_user_account(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.delete(
        f"/api/v1/users/{test_user_id}/account/", headers=auth_header
    )
    # Assert
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_replace_user_account(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.put(
        f"/api/v1/users/{test_user_id}/account/", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 403


# +-------------------------+
# | Not Implemented Methods |
# +-------------------------+


@pytest.mark.asyncio
async def test_list_users(async_client, auth_header) -> None:
    # Act
    response = await async_client.get("/api/v1/users/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_delete_user(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.delete(
        f"/api/v1/users/{test_user_id}", headers=auth_header
    )
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_replace_user(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.put(
        f"/api/v1/users/{test_user_id}", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_update_user_account(async_client, auth_header, test_user_id) -> None:
    # Act
    response = await async_client.patch(
        f"/api/v1/users/{test_user_id}/account/", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 405
