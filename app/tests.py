from fastapi.testclient import TestClient
from app.main import app   # <-- absolute import

client = TestClient(app)

def test_get_octocat_gists():
    response = client.get("/users/octocat")
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert data["user"] == "octocat"
    assert "gists" in data


