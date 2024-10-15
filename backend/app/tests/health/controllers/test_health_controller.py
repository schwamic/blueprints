from fastapi.testclient import TestClient
from app.main import app
from app.health.models.health_model import HealthLiveStatus

client = TestClient(app)

def test_get_health_live():
    response = client.post("/api/v1/health:live")
    assert response.status_code == 200
    assert response.json() == {"state": "live"}

def test_get_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 405

def test_create_health():
    response = client.post("/api/v1/health")
    assert response.status_code == 405

def test_update_health():
    response = client.patch("/api/v1/health")
    assert response.status_code == 405

def test_delete_health():
    response = client.delete("/api/v1/health")
    assert response.status_code == 405
    
def test_replace_health():
    response = client.put("/api/v1/health")
    assert response.status_code == 405
