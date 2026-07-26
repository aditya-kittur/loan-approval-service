from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_status_returns_service_metadata_with_http_200() -> None:
    """GET /api/status returns 200 with expected service metadata fields."""
    response = client.get("/api/status")

    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "loan-approval-service"
    assert body["version"] == "1.0.0"
    assert isinstance(body["uptime_seconds"], float)
