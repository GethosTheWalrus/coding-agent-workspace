import os
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine

# Import the FastAPI app after we have a chance to monkeypatch the database engine
from app import main, database

@pytest.fixture(scope="function")
def client():
    """Create a TestClient with an isolated in‑memory SQLite database.

    The fixture creates a temporary file for the SQLite DB, patches the
    ``engine`` used by ``app.database`` and recreates the tables.
    """
    # Use a temporary file to avoid sharing state between tests
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        # Build a new engine pointing at the temporary SQLite file
        test_engine = create_engine(f"sqlite:///{db_path}", echo=False)
        # Patch the module-level engine and path
        database.engine = test_engine
        database.SQLITE_DB_PATH = db_path
        # Re‑create tables on the new engine
        database.create_db_and_tables()

        # Initialise the FastAPI app (the router is already attached)
        client = TestClient(main.app)
        yield client
        # No explicit teardown needed – the temporary directory is removed

def test_create_read_update_delete_flow(client: TestClient):
    # Create a new todo
    payload = {
        "title": "Buy milk",
        "description": "2% milk",
        "completed": False,
    }
    response = client.post("/todos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] == payload["completed"]
    todo_id = data["id"]

    # Read list – should contain the newly created todo
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert any(t["id"] == todo_id for t in todos)

    # Read single todo
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    single = response.json()
    assert single["id"] == todo_id
    assert single["title"] == payload["title"]

    # Update the todo
    update_payload = {
        "title": "Buy almond milk",
        "description": "Unsweetened",
        "completed": True,
    }
    response = client.put(f"/todos/{todo_id}", json=update_payload)
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == update_payload["title"]
    assert updated["description"] == update_payload["description"]
    assert updated["completed"] == update_payload["completed"]

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Verify it is gone
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404

def test_not_found_errors(client: TestClient):
    # Non‑existent ID for GET, PUT, DELETE should all return 404
    for method, url, json_body in [
        ("get", "/todos/999", None),
        ("put", "/todos/999", {"title": "x", "description": "y", "completed": False}),
        ("delete", "/todos/999", None),
    ]:
        if method == "get":
            resp = client.get(url)
        elif method == "put":
            resp = client.put(url, json=json_body)
        elif method == "delete":
            resp = client.delete(url)
        else:
            continue
        assert resp.status_code == 404
