from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate():
    response = client.post("/calculate", json={
        "principal": 1000,
        "rate": 0.05,
        "time": 3
    })
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert round(data["total"], 2) == 1157.63  # Expected result for given input

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Investment Calculator API"}
