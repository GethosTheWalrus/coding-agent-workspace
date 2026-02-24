# tests/test_todo.py
"""Integration tests for the Todo API.

The tests use FastAPI's ``TestClient`` to make HTTP requests against the
application. A fresh SQLite database file (``todo.db``) is removed before the
test suite runs to ensure a clean state.
"""

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

# Ensure a clean database before each test session
@pytest.fixture(scope="session", autouse=True)
def clean_db():
    db_path = Path(__file__).parent.parent / "todo.db"
    if db_path.exists():
        db_path.unlink()
    # The FastAPI startup event will create tables automatically.
    yield
    # Cleanup after tests
    if db_path.exists():
        db_path.unlink()

@pytest.fixture()
def client():
    return TestClient(app)

def test_create_todo(client: TestClient):
    payload = {"title": "Buy milk", "description": "2% milk", "completed": False}
    response = client.post("/todos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert "id" in data
    # Store id for later tests
    return data["id"]

def test_read_todos(client: TestClient):
    # Ensure at least one todo exists (create if needed)
    payload = {"title": "Read test", "description": None, "completed": False}
    client.post("/todos/", json=payload)
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert any(todo["title"] == "Read test" for todo in todos)

def test_read_single_todo(client: TestClient):
    payload = {"title": "Single", "description": "single item", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    resp = client.get(f"/todos/{todo_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == todo_id
    assert data["title"] == payload["title"]

def test_update_todo(client: TestClient):
    payload = {"title": "Update me", "description": "old", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    update_payload = {"title": "Updated", "description": "new", "completed": True}
    resp = client.put(f"/todos/{todo_id}", json=update_payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Updated"
    assert data["description"] == "new"
    assert data["completed"] is True

def test_delete_todo(client: TestClient):
    payload = {"title": "Delete me", "description": "to be deleted", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    del_resp = client.delete(f"/todos/{todo_id}")
    assert del_resp.status_code == 204
    # Verify it no longer exists
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 404
