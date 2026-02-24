import os
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

# Path to the SQLite DB file used by the application
DB_PATH = Path(__file__).resolve().parents[2] / "app" / "todo.db"

@pytest.fixture(scope="function", autouse=True)
def clean_db():
    """Ensure a fresh database for each test function.

    The application creates the SQLite file at ``app/todo.db``. This fixture
    removes the file before a test runs and recreates the tables after the
    import of ``app.main`` (which calls ``Base.metadata.create_all``).
    """
    # Remove existing DB file if present
    if DB_PATH.exists():
        DB_PATH.unlink()
    # Ensure tables are created (importing app triggers creation)
    yield
    # Clean up after test
    if DB_PATH.exists():
        DB_PATH.unlink()

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/todos/",
        json={"title": "Test Todo", "description": "A test item", "completed": False},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "A test item"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data

def test_read_todos_and_single_todo():
    # Create two todos first
    client.post(
        "/todos/",
        json={"title": "First", "description": "First item", "completed": False},
    )
    client.post(
        "/todos/",
        json={"title": "Second", "description": "Second item", "completed": True},
    )
    # List todos
    list_resp = client.get("/todos/")
    assert list_resp.status_code == 200
    todos = list_resp.json()
    assert isinstance(todos, list)
    assert len(todos) == 2
    # Retrieve first todo by ID
    todo_id = todos[0]["id"]
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 200
    todo = get_resp.json()
    assert todo["id"] == todo_id
    assert todo["title"] == "First"

def test_update_todo():
    # Create a todo
    create_resp = client.post(
        "/todos/",
        json={"title": "Old Title", "description": "Old desc", "completed": False},
    )
    todo_id = create_resp.json()["id"]
    # Update the todo
    update_resp = client.put(
        f"/todos/{todo_id}",
        json={"title": "New Title", "completed": True},
    )
    assert update_resp.status_code == 200
    updated = update_resp.json()
    assert updated["title"] == "New Title"
    assert updated["completed"] is True
    # Ensure other fields remain unchanged
    assert updated["description"] == "Old desc"

def test_delete_todo():
    # Create a todo
    create_resp = client.post(
        "/todos/",
        json={"title": "To be deleted", "description": "Will be removed", "completed": False},
    )
    todo_id = create_resp.json()["id"]
    # Delete the todo
    delete_resp = client.delete(f"/todos/{todo_id}")
    assert delete_resp.status_code == 200
    deleted = delete_resp.json()
    assert deleted["id"] == todo_id
    # Verify it no longer exists
    get_resp = client.get(f"/todos/{todo_id}")
    assert get_resp.status_code == 404
