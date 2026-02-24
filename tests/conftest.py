"""Pytest fixtures for the FastAPI application.

TODO: Create a fixture that provides a test client using `TestClient`
and a temporary SQLite database (in‑memory) for isolated tests.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

# TODO: Override the DB dependency with an in‑memory SQLite for tests

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
