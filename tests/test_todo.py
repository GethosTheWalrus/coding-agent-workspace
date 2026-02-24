# tests/test_todo.py
"""Tests for the Todo API CRUD operations.

Covers creation, retrieval, listing, updating, and deletion of Todo items.
Ensures proper HTTP status codes and response payloads.
"""

import pytest
from fastapi import status

@pytest.fixture
def todo_payload():
    return {"title": "Test Todo", "description": "A test todo item", "completed": False}

def test_create_todo(client, todo_payload):
    response = client.post("/todos/", json=todo_payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == todo_payload["title"]
    assert data["description"] == todo_payload["description"]
    assert data["completed"] == todo_payload["completed"]
    assert "id" in data
    return data["id"]

def test_read_todo(client, todo_payload):
    # Create first
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    # Retrieve
    resp = client.get(f"/todos/{todo_id}")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert data["id"] == todo_id
    assert data["title"] == todo_payload["title"]

def test_list_todos(client, todo_payload):
    # Ensure at least one todo exists
    client.post("/todos/", json=todo_payload)
    resp = client.get("/todos/")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert isinstance(data, list)
    assert any(item["title"] == todo_payload["title"] for item in data)

def test_update_todo(client, todo_payload):
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    update_data = {"title": "Updated Title", "completed": True}
    resp = client.put(f"/todos/{todo_id}", json=update_data)
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert data["title"] == update_data["title"]
    assert data["completed"] == update_data["completed"]

def test_delete_todo(client, todo_payload):
    create_resp = client.post("/todos/", json=todo_payload)
    todo_id = create_resp.json()["id"]
    del_resp = client.delete(f"/todos/{todo_id}")
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT
    # Verify deletion
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == status.HTTP_404_NOT_FOUND
