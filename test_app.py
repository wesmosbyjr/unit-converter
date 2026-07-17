from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_temperature_endpoint():
    client = app.test_client()
    response = client.get("/convert/temperature?celsius=100")
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 212.0


def test_distance_rejects_empty_param():
    client = app.test_client()
    response = client.get("/convert/distance?miles=")
    assert response.status_code == 400