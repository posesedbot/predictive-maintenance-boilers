# test_api.py
from fastapi.testclient import TestClient
from api.fastapi_app import app

client = TestClient(app)

FAILURE_PAYLOAD = {
    "run_hours": 2000,
    "temp_avg": 90.0,
    "pressure_avg": 6.0,
    "vibration": 2.5,
}

SUCCESS_PAYLOAD = {
    "run_hours": 800,
    "temp_avg": 85.0,
    "pressure_avg": 5.0,
    "vibration": 1.5,
}


def test_api_is_running():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Boiler Maintenance API is running."


def test_prediction_failure_scenario():
    response = client.post("/predict", json=FAILURE_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["prediction"] == 1
    assert "SHUTDOWN & INSPECTION" in data["action_required"]


def test_prediction_success_scenario():
    response = client.post("/predict", json=SUCCESS_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["prediction"] == 0
    assert "STATUS OK" in data["action_required"]
    response = requests.post(PREDICT_URL, json=SUCCESS_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["prediction"] == 0
    assert "STATUS OK" in data["action_required"]
