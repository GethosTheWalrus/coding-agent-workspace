"""Integration tests for API endpoints."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


class TestCreateTodoEndpoint:
    """Tests for POST /todos endpoint."""
    
    def test_create_todo_success(self, client: TestClient, sample_todo_data):
        """Test creating a todo with valid data."""
        response = client.post("/todos/", json=sample_todo_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_todo_data["title"]
        assert data["description"] == sample_todo_data["description"]
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
    
    def test_create_todo_with_title_only(self, client: TestClient):
        """Test creating a todo with only title."""
        response = client.post("/todos/", json={"title": "Test"})
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test"
        assert data["description"] is None
    
    def test_create_todo_missing_title(self, client: TestClient):
        """Test creating a todo without title returns 422."""
        response = client.post("/todos/", json={"description": "No title"})
        
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
    
    def test_create_todo_empty_title(self, client: TestClient):
        """Test creating a todo with empty title returns 422."""
        response = client.post("/todos/", json={"title": ""})
        
        assert response.status_code == 422


class TestListTodosEndpoint:
    """Tests for GET /todos endpoint."""
    
    def test_list_todos_empty(self, client: TestClient):
        """Test listing todos when database is empty."""
        response = client.get("/todos/")
        
        assert response.status_code == 200
        assert response.json() == []
    
    def test_list_todos_with_data(self, client: TestClient, created_todo):
        """Test listing todos with data."""
        response = client.get("/todos/")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == created_todo.id
        assert data[0]["title"] == created_todo.title
    
    def test_list_todos_with_pagination(self, client: TestClient):
        """Test listing todos with pagination."""
        # Create multiple todos
        for i in range(5):
            client.post("/todos/", json={"title": f"Todo {i}"})
        
        # Test skip
        response = client.get("/todos/?skip=2")
        assert response.status_code == 200
        assert len(response.json()) == 3
        
        # Test limit
        response = client.get("/todos/?limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2


class TestGetTodoEndpoint:
    """Tests for GET /todos/{id} endpoint."""
    
    def test_get_todo_success(self, client: TestClient, created_todo):
        """Test getting an existing todo."""
        response = client.get(f"/todos/{created_todo.id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_todo.id
        assert data["title"] == created_todo.title
    
    def test_get_todo_not_found(self, client: TestClient):
        """Test getting a non-existent todo."""
        response = client.get("/todos/999")
        
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data


class TestUpdateTodoEndpoint:
    """Tests for PUT /todos/{id} endpoint."""
    
    def test_update_todo_success(self, client: TestClient, created_todo):
        """Test updating an existing todo."""
        update_data = {"title": "Updated Title", "completed": True}
        response = client.put(f"/todos/{created_todo.id}", json=update_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["completed"] is True
    
    def test_update_todo_partial(self, client: TestClient, created_todo):
        """Test partial update of a todo."""
        update_data = {"completed": True}
        response = client.put(f"/todos/{created_todo.id}", json=update_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == created_todo.title  # Unchanged
        assert data["completed"] is True
    
    def test_update_todo_not_found(self, client: TestClient):
        """Test updating a non-existent todo."""
        response = client.put("/todos/999", json={"title": "Updated"})
        
        assert response.status_code == 404


class TestDeleteTodoEndpoint:
    """Tests for DELETE /todos/{id} endpoint."""
    
    def test_delete_todo_success(self, client: TestClient, created_todo):
        """Test deleting an existing todo."""
        response = client.delete(f"/todos/{created_todo.id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Todo deleted successfully"
        
        # Verify todo is deleted
        get_response = client.get(f"/todos/{created_todo.id}")
        assert get_response.status_code == 404
    
    def test_delete_todo_not_found(self, client: TestClient):
        """Test deleting a non-existent todo."""
        response = client.delete("/todos/999")
        
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data


class TestRootEndpoint:
    """Tests for root endpoint."""
    
    def test_root_endpoint(self, client: TestClient):
        """Test root endpoint returns API info."""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Todo API"
        assert data["version"] == "1.0.0"


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_endpoint(self, client: TestClient):
        """Test health check endpoint."""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"