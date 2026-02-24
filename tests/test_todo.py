import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.main import get_app
from app import database, models

# Use an in-memory SQLite database for tests
TEST_DATABASE_URL = "sqlite:///:memory:"

def get_test_engine():
    return create_engine(TEST_DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

@pytest.fixture(name="client")
def client_fixture():
    # Create a new engine and session for each test run
    engine = get_test_engine()
    SQLModel.metadata.create_all(engine)

    def get_test_session() -> Session:
        with Session(engine) as session:
            yield session

    # Override the dependency that provides a DB session
    app = get_app()
    app.dependency_overrides[database.get_session] = get_test_session
    with TestClient(app) as client:
        yield client
    # Clean up overrides after test
    app.dependency_overrides.clear()

def test_create_read_update_delete_todo(client: TestClient):
    # Create a new todo
    todo_data = {
        "title": "Test Todo",
        "description": "A test todo item",
        "completed": False,
    }
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == 201
    created = response.json()
    assert created["title"] == todo_data["title"]
    assert created["description"] == todo_data["description"]
    assert created["completed"] is False
    todo_id = created["id"]

    # Read the list of todos
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert any(t["id"] == todo_id for t in todos)

    # Read the specific todo
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    todo = response.json()
    assert todo["id"] == todo_id
    assert todo["title"] == "Test Todo"

    # Update the todo (partial)
    update_data = {"completed": True, "title": "Updated Title"}
    response = client.patch(f"/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["completed"] is True
    assert updated["title"] == "Updated Title"

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Verify it is gone
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
