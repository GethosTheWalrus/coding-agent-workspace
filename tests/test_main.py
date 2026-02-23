"""Basic integration tests for the Todo API using pytest and httpx.

These tests start the FastAPI app with TestClient and perform a simple
create‑read‑update‑delete (CRUD) cycle.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_crud_flow():
    # Create a new todo
    response = client.post(
        "/todos/",
        json={"title": "Write tests", "description": "Add integration tests", "completed": False},
    )
    assert response.status_code == 201
    todo = response.json()
    todo_id = todo["id"]
    assert todo["title"] == "Write tests"

    # Read the created todo
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["id"] == todo_id
    assert fetched["title"] == "Write tests"

    # Update the todo
    response = client.put(
        f"/todos/{todo_id}", json={"completed": True, "title": "Write tests (updated)"}
    )
    assert response.status_code == 200
    updated = response.json()
    assert updated["completed"] is True
    assert updated["title"] == "Write tests (updated)"

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Verify deletion
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
