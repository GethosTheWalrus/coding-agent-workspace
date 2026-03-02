"""Tests for API endpoints."""
import pytest
from fastapi.testclient import TestClient
from httpx import Response


class TestRootEndpoint:
    """Tests for the root endpoint."""
    
    def test_root_returns_info(self, client: TestClient):
        """Test that root endpoint returns API information."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data


class TestCreateTodo:
    """Tests for POST /todos/ endpoint."""
    
    def test_create_todo_success(self, client: TestClient, sample_todo_data):
        """Test creating a todo successfully."""
        response = client.post("/todos/", json=sample_todo_data)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_todo_data["title"]
        assert data["description"] == sample_todo_data["description"]
        assert data["completed"] == sample_todo_data["completed"]
        assert "id" in data
    
    def test_create_todo_minimal_data(self, client: TestClient):
        """Test creating a todo with minimal data."""
        response = client.post("/todos/", json={"title": "Minimal Todo"})
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Minimal Todo"
        assert data["description"] is None
        assert data["completed"] == False
    
    def test_create_todo_invalid_data(self, client: TestClient):
        """Test creating a todo with invalid data."""
        response = client.post("/todos/", json={"description": "No title"})
        assert response.status_code == 422
    
    def test_create_todo_empty_title(self, client: TestClient):
        """Test creating a todo with empty title."""
        response = client.post("/todos/", json={"title": ""})
        assert response.status_code == 422


class TestReadTodos:
    """Tests for GET /todos/ endpoint."""
    
    def test_read_todos_empty(self, client: TestClient):
        """Test reading todos when database is empty."""
        response = client.get("/todos/")
        assert response.status_code == 200
        assert response.json() == []
    
    def test_read_todos_with_data(self, client: TestClient, created_todo):
        """Test reading todos with data in database."""
        response = client.get("/todos/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == created_todo.id
    
    def test_read_todos_filter_completed(self, client: TestClient, created_todo):
        """Test filtering todos by completed status."""
        # Create a completed todo
        client.post("/todos/", json={"title": "Completed", "completed": True})
        
        # Filter by completed=False
        response = client.get("/todos/?completed=false")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == created_todo.id
        
        # Filter by completed=true
        response = client.get("/todos/?completed=true")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["completed"] == True


class TestReadTodo:
    """Tests for GET /todos/{todo_id} endpoint."""
    
    def test_read_todo_success(self, client: TestClient, created_todo):
        """Test reading an existing todo."""
        response = client.get(f"/todos/{created_todo.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_todo.id
        assert data["title"] == created_todo.title
    
    def test_read_todo_not_found(self, client: TestClient):
        """Test reading a non-existent todo."""
        response = client.get("/todos/999")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data


class TestUpdateTodo:
    """Tests for PUT /todos/{todo_id} endpoint."""
    
    def test_update_todo_success(self, client: TestClient, created_todo):
        """Test updating an existing todo."""
        update_data = {"title": "Updated Title", "completed": True}
        response = client.put(f"/todos/{created_todo.id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["completed"] == True
    
    def test_update_todo_partial(self, client: TestClient, created_todo):
        """Test partial update of a todo."""
        update_data = {"completed": True}
        response = client.put(f"/todos/{created_todo.id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["completed"] == True
        assert data["title"] == created_todo.title  # Unchanged
    
    def test_update_todo_not_found(self, client: TestClient):
        """Test updating a non-existent todo."""
        response = client.put("/todos/999", json={"title": "Updated"})
        assert response.status_code == 404
    
    def test_update_todo_invalid_data(self, client: TestClient, created_todo):
        """Test updating with invalid data."""
        response = client.put(f"/todos/{created_todo.id}", json={"title": ""})
        assert response.status_code == 422


class TestDeleteTodo:
    """Tests for DELETE /todos/{todo_id} endpoint."""
    
    def test_delete_todo_success(self, client: TestClient, created_todo):
        """Test deleting an existing todo."""
        response = client.delete(f"/todos/{created_todo.id}")
        assert response.status_code == 204
        
        # Verify it's deleted
        get_response = client.get(f"/todos/{created_todo.id}")
        assert get_response.status_code == 404
    
    def test_delete_todo_not_found(self, client: TestClient):
        """Test deleting a non-existent todo."""
        response = client.delete("/todos/999")
        assert response.status_code == 404