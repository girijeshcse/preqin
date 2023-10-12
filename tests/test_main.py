import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_generate_array_valid_input(client):
    response = client.post(
        "/generate_array/", json={"sentence": "This is a valid sentence"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "input_sentence" in data
    assert "random_array" in data
    assert len(data["random_array"]) == 500


def test_generate_array_empty_input(client):
    response = client.post("/generate_array/", json={"sentence": ""})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Input sentence cannot be empty"
