from fastapi.testclient import TestClient
from app.main import app
from app.health.models.health_model import HealthLiveStatus

client = TestClient(app)

def test_get_health_live():
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": HealthLiveStatus.LIVE}
