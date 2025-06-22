from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_flight():
    response = client.get("/flights?airline_code=AI&airline_number=101&departure_date=2024-06-20")
    assert response.status_code == 200
    assert "airline" in response.json()
