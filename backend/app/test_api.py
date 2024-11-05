
import requests

BASE_URL = "http://localhost:5000"  # URL de l'API backend

def test_healthcheck():
    """Test de vérification de l'état de l'API."""
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"

def test_prediction_endpoint():
    """Test de l'endpoint de prédiction."""
    data = {"first_name": "John", "last_name": "Doe", "age": 30}
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
