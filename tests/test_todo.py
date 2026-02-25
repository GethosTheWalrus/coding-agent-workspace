"""Tests for the Todo API.

These tests cover all CRUD endpoints and error handling, aiming for >90% coverage of the
`app` package.
"""

import pytest

# The `client` fixture is provided by `tests/conftest.py`

def test_create_todo_success(client):
    payload = {"title": "Test Todo", "description": "A test item", "completed": False}
    response = client.post("/todos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert isinstance(data["id"], int)

def test_create_todo_missing_title(client):
    # title is required; should get validation error (422)
    payload = {"description": "No title"}
    response = client.post("/todos/", json=payload)
    assert response.status_code == 422

def test_read_todos_list(client):
    # Ensure at least one todo exists from previous test
    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # The list should contain dictionaries with required keys
    if data:
        first = data[0]
        for key in ["id", "title", "description", "completed"]:
            assert key in first

def test_read_single_todo_success(client):
    # Create a new todo to fetch
    payload = {"title": "Fetch Me", "description": "Fetch description", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    # Retrieve it
    resp = client.get(f"/todos/{todo_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == todo_id
    assert data["title"] == payload["title"]

def test_read_single_todo_not_found(client):
    resp = client.get("/todos/999999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Todo not found"

def test_update_todo_success(client):
    # Create a todo
    payload = {"title": "Old Title", "description": "Old desc", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    # Update fields
    update_payload = {"title": "New Title", "completed": True}
    resp = client.put(f"/todos/{todo_id}", json=update_payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "New Title"
    assert data["completed"] is True
    # Unchanged fields remain the same
    assert data["description"] == "Old desc"

def test_update_todo_not_found(client):
    resp = client.put("/todos/999999", json={"title": "Doesn't matter"})
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Todo not found"

def test_delete_todo_success(client):
    # Create a todo to delete
    payload = {"title": "Delete Me", "description": "Will be deleted", "completed": False}
    create_resp = client.post("/todos/", json=payload)
    todo_id = create_resp.json()["id"]
    # Delete it
    del_resp = client.delete(f"/todos/{todo_id}")
    assert del_resp.status_code == 204
    # Subsequent get should be 404
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 404

def test_delete_todo_not_found(client):
    resp = client.delete("/todos/999999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Todo not found"
