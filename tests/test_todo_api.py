"""Integration tests for the FastAPI Todo API.

These tests cover all CRUD endpoints and aim for >90% code coverage.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def todo_payload():
    return {
        "title": "Test Todo",
        "description": "A todo item for testing",
        "completed": False,
    }

def test_create_todo(todo_payload):
    response = client.post("/todos/", json=todo_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == todo_payload["title"]
    assert data["description"] == todo_payload["description"]
    assert data["completed"] == todo_payload["completed"]
    assert isinstance(data["id"], int)
    # Store ID for later tests
    return data["id"]

def test_read_todo(todo_payload):
    # First create
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    # Read it back
    resp = client.get(f"/todos/{todo_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == todo_id
    assert data["title"] == todo_payload["title"]

def test_list_todos(todo_payload):
    # Ensure at least one exists
    client.post("/todos/", json=todo_payload)
    resp = client.get("/todos/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    # Verify structure of first item
    first = data[0]
    assert "id" in first and "title" in first and "completed" in first

def test_update_todo(todo_payload):
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    update_data = {"title": "Updated Title", "completed": True}
    resp = client.put(f"/todos/{todo_id}", json=update_data)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Updated Title"
    assert data["completed"] is True
    # Unchanged fields remain the same
    assert data["description"] == todo_payload["description"]

def test_delete_todo(todo_payload):
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    del_resp = client.delete(f"/todos/{todo_id}")
    assert del_resp.status_code == 204
    # Subsequent get should 404
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 404

def test_not_found():
    # Access a non-existent ID
    resp = client.get("/todos/9999")
    assert resp.status_code == 404
    del_resp = client.delete("/todos/9999")
    assert del_resp.status_code == 404
    put_resp = client.put("/todos/9999", json={"title": "x"})
    assert put_resp.status_code == 404
