# FastAPI Application README

This README provides an overview of the FastAPI application implemented in `main.py`. The application is a simple API that includes user authentication and an endpoint to generate random arrays based on a provided sentence.

## Table of Contents

- [Application Overview](#application-overview)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Dependencies](#dependencies)

## Application Overview

The `main.py` file contains a FastAPI application with the following key features:

- User authentication using OAuth2 with username and password.
- Token generation for authenticated users.
- An endpoint to generate random arrays based on a provided sentence.

## Installation

1. Clone this repository:

   ```bash
   https://github.com/girijeshcse/preqin.git
   ```

2. Navigate to the project directory:

   ```bash
   cd preqin
   ```

3. Install the required dependencies. It is recommended to use a virtual environment for this:

   ```bash
   pip install -r requirements.txt
   ```

## API Endpoints

The application provides the following API endpoints:

- `POST /token`: Endpoint for user authentication and token generation.
- `POST /generate_array/`: Endpoint to receive a sentence and return a random array.

## Authentication

To access protected endpoints, you need to obtain an access token by authenticating. Use the `/token` endpoint with a valid username and password to obtain an access token. You should include the obtained token in the `Authorization` header as `Bearer <your-access-token>` when making requests to protected endpoints.
username=johndoe
password=secret

## Running the Application

You can run the FastAPI application with the following command:

```bash
uvicorn main:app --reload
```

This starts the development server, and you can access the API at `http://127.0.0.1:8000`.

## Testing

To run tests for the application, you can use [Pytest](https://docs.pytest.org/en/6.2.x/). Make sure you have the necessary test dependencies installed.

```bash
pytest
```

The tests are located in the `tests` directory and cover various scenarios for different API endpoints.

## Dependencies

The application relies on the following dependencies, which are listed in the `requirements.txt` file:

- FastAPI: A modern web framework for building APIs with Python.
- Pydantic: Data validation and parsing library.
- passlib: Password hashing library for secure password storage.
- jose: JSON Web Tokens (JWT) implementation.
- starlette: ASGI framework for building web applications.
- uvicorn: ASGI server for running FastAPI applications.
- pytest: Testing framework for Python.
- fastapi-testclient: A test client for FastAPI applications.

Make sure to install these dependencies using `pip` as described in the installation section.

---
