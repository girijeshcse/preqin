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
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MzcxMDc0fQ.6b2-HFYy8pfasuQngZRBL-I-O5ohrmBl6xXLmXk3Asg"

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
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MzcxMDc0fQ.6b2-HFYy8pfasuQngZRBL-I-O5ohrmBl6xXLmXk3Asg"

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
    assert "Not authenticated" in response.json()["detail"]


def test_generate_array_inactive_user():
    # Replace this with a valid access token for an inactive user
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjk3MTczMTQwfQ.w1d-_RcnB9X_zyOIbRqTRRIJFdLBqmoK3RPOHxX"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 401
    assert "detail" in response.json()
    assert "Inactive user" in response.json()["detail"]


def test_login_for_access_token_invalid_credentials():
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "incorrect_password"},
    )
    assert response.status_code == 401
    assert "detail" in response.json()
    assert "Incorrect username or password" in response.json()["detail"]


# def test_login_for_access_token_missing_credentials():
#     response = client.post(
#         "/token",
#         data={"username": "", "password": ""},
#     )
#     assert response.status_code == 422  # Unprocessable Entity
#     assert "detail" in response.json()
#     assert "field required" in response.json()["detail"][0]["msg"]


def test_login_for_access_token_invalid_token_request_form():
    response = client.post(
        "/token",
        data={"wrong_field": "value"},
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert (
        'string does not match regex "password"' in response.json()["detail"][0]["msg"]
    )


def test_generate_array_missing_input():
    access_token = "your-valid-access-token"

    response = client.post(
        "/generate_array/",
        json={"sentence": ""},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Input sentence cannot be empty" in response.json()["detail"]


def test_generate_array_large_input():
    access_token = "your-valid-access-token"

    # Create an input sentence with a very large size to test the application's limits
    input_sentence = "Big Sentence" * 10000

    response = client.post(
        "/generate_array/",
        json={"sentence": input_sentence},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Request entity too large" in response.json()["detail"]


# API Tests


def test_generate_array_invalid_access_token():
    access_token = "invalid-access-token"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 401
    assert "detail" in response.json()
    assert "Could not validate credentials" in response.json()["detail"]


def test_generate_array_invalid_token_scheme():
    access_token = "Basic invalid-access-token"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": access_token},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Invalid token type" in response.json()["detail"]


def test_generate_array_invalid_token_format():
    access_token = "Bearer invalid-access-token"

    response = client.post(
        "/generate_array/",
        json={"sentence": "Test Sentence"},
        headers={"Authorization": access_token},
    )
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Invalid token format" in response.json()["detail"]
