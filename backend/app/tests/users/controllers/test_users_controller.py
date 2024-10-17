from fastapi.testclient import TestClient
from app.main import app
from app.common.core.settings import settings
from app.users.models.users_model import UserPublic


def test_get_user(client: TestClient) -> None:
    # TODO: Implement test
    user = UserPublic(userId="1234")
    response = client.get(f"/api/v1/users/{user.id}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 200
    assert response.json() == user.model_dump()

def test_list_users(client: TestClient) -> None:
    response = client.get("/api/v1/users/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_create_user(client: TestClient) -> None:
    response = client.post("/api/v1/users/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_update_user(client: TestClient) -> None:
    response = client.push("/api/v1/users/{userId}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_delete_user(client: TestClient) -> None:
    response = client.delete("/api/v1/users/{userId}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_replace_user(client: TestClient) -> None:
    response = client.put("/api/v1/users/{userId}", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_get_user_account(client: TestClient) -> None:
    # TODO: Implement test
    pass


def test_update_user_account(client: TestClient) -> None:
    response = client.push("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 405


def test_create_user_account(client: TestClient) -> None:
    response = client.post("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 403


def test_delete_user_account(client: TestClient) -> None:
    response = client.delete("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 403


def test_replace_user_account(client: TestClient) -> None:
    response = client.put("/api/v1/users/{userId}/account/", headers={"X-Secret-Token": settings.X_SECRET_TOKEN})
    assert response.status_code == 403
