from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_login_for_access_token():
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "secret"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_generate_array():
    # Replace this with a valid access token obtained from the login endpoint
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MTczMTQwfQ.w1d-_RcnB9X_zyOIbRqTRRIJFdLBqmoK3RPOHxXetAQ"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert "input_sentence" in data
    assert "random_array" in data


def test_generate_array_invalid_input():
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MTczMTQwfQ.w1d-_RcnB9X_zyOIbRqTRRIJFdLBqmoK3RPOHxXetAQ"

    response = client.post(
        "/generate_array/",
        json={"sentence": ""},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Input sentence cannot be empty" in response.json()["detail"]


def test_generate_array_unauthorized():
    response = client.post("/generate_array/", json={"sentence": "Test Sentence"})
    assert response.status_code == 401
    assert "detail" in response.json()
    assert "Could not validate credentials" in response.json()["detail"]


def test_generate_array_inactive_user():
    # Replace this with a valid access token for an inactive user
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MTczMTQwfQ.w1d-_RcnB9X_zyOIbRqTRRIJFdLBqmoK3RPOHxX"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Inactive user" in response.json()["detail"]
