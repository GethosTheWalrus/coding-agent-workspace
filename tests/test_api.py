"""Integration tests for API endpoints."""

import pytest
from fastapi.testclient import TestClient


class TestCreateTodoEndpoint:
    """Tests for POST /todos endpoint."""
    
    def test_create_todo_success(self, client: TestClient, sample_todo_data: dict):
        """Test successful todo creation."""
        response = client.post("/todos", json=sample_todo_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_todo_data["title"]
        assert data["description"] == sample_todo_data["description"]
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
    
    def test_create_todo_with_minimal_data(self, client: TestClient):
        """Test creating a todo with only required fields."""
        response = client.post("/todos", json={"title": "Minimal Todo"})
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Minimal Todo"
        assert data["description"] is None
        assert data["completed"] is False
    
    def test_create_todo_with_completed_true(self, client: TestClient):
        """Test creating a completed todo."""
        response = client.post("/todos", json={
            "title": "Completed Todo",
            "completed": True
        })
        
        assert response.status_code == 201
        data = response.json()
        assert data["completed"] is True
    
    def test_create_todo_invalid_data(self, client: TestClient):
        """Test creating a todo with invalid data."""
        response = client.post("/todos", json={"title": ""})
        
        assert response.status_code == 422
    
    def test_create_todo_missing_title(self, client: TestClient):
        """Test creating a todo without title."""
        response = client.post("/todos", json={"description": "No title"})
        
        assert response.status_code == 422


class TestListTodosEndpoint:
    """Tests for GET /todos endpoint."""
    
    def test_list_todos_empty(self, client: TestClient):
        """Test listing todos when none exist."""
        response = client.get("/todos")
        
        assert response.status_code == 200
        data = response.json()
        assert data["items"] == []
        assert data["total"] == 0
    
    def test_list_todos_with_items(self, client: TestClient, sample_todo_data: dict):
        """Test listing todos when items exist."""
        # Create some todos
        for i in range(3):
            client.post("/todos", json={**sample_todo_data, "title": f"Todo {i}"})
        
        response = client.get("/todos")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 3
        assert data["total"] == 3
    
    def test_list_todos_with_pagination(self, client: TestClient, sample_todo_data: dict):
        """Test listing todos with pagination."""
        # Create multiple todos
        for i in range(5):
            client.post("/todos", json={**sample_todo_data, "title": f"Todo {i}"})
        
        response = client.get("/todos?skip=0&limit=2")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 2
        assert data["total"] == 5
        assert data["page"] == 1
    
    def test_list_todos_filter_by_completed(self, client: TestClient, sample_todo_data: dict):
        """Test listing todos filtered by completion status."""
        # Create todos with different completion status
        client.post("/todos", json={**sample_todo_data, "title": "Completed", "completed": True})
        client.post("/todos", json={**sample_todo_data, "title": "Not Completed", "completed": False})
        client.post("/todos", json={**sample_todo_data, "title": "Another Completed", "completed": True})
        
        response = client.get("/todos?completed=true")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 2
        assert all(item["completed"] is True for item in data["items"])


class TestGetTodoEndpoint:
    """Tests for GET /todos/{todo_id} endpoint."""
    
    def test_get_todo_success(self, client: TestClient, sample_todo_data: dict):
        """Test retrieving an existing todo."""
        # Create a todo first
        create_response = client.post("/todos", json=sample_todo_data)
        create_response.raise_for_status()
        todo_id = create_response.json()["id"]
        
        response = client.get(f"/todos/{todo_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == todo_id
        assert data["title"] == sample_todo_data["title"]
    
    def test_get_todo_not_found(self, client: TestClient):
        """Test retrieving a todo that doesn't exist."""
        response = client.get("/todos/99999")
        
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data


class TestUpdateTodoEndpoint:
    """Tests for PUT /todos/{todo_id} endpoint."""
    
    def test_update_todo_success(self, client: TestClient, sample_todo_data: dict):
        """Test successful todo update."""
        # Create a todo first
        create_response = client.post("/todos", json=sample_todo_data)
        create_response.raise_for_status()
        todo_id = create_response.json()["id"]
        
        update_data = {"title": "Updated Title", "completed": True}
        response = client.put(f"/todos/{todo_id}", json=update_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["completed"] is True
    
    def test_update_todo_partial(self, client: TestClient, sample_todo_data: dict):
        """Test partial todo update."""
        # Create a todo first
        create_response = client.post("/todos", json=sample_todo_data)
        create_response.raise_for_status()
        todo_id = create_response.json()["id"]
        original_description = create_response.json().get("description")
        
        response = client.put(f"/todos/{todo_id}", json={"title": "New Title"})
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "New Title"
        assert data["description"] == original_description
    
    def test_update_todo_not_found(self, client: TestClient):
        """Test updating a todo that doesn't exist."""
        response = client.put("/todos/99999", json={"title": "New Title"})
        
        assert response.status_code == 404
    
    def test_update_todo_invalid_data(self, client: TestClient, sample_todo_data: dict):
        """Test updating a todo with invalid data."""
        # Create a todo first
        create_response = client.post("/todos", json=sample_todo_data)
        create_response.raise_for_status()
        todo_id = create_response.json()["id"]
        
        response = client.put(f"/todos/{todo_id}", json={"title": ""})
        
        assert response.status_code == 422


class TestDeleteTodoEndpoint:
    """Tests for DELETE /todos/{todo_id} endpoint."""
    
    def test_delete_todo_success(self, client: TestClient, sample_todo_data: dict):
        """Test successful todo deletion."""
        # Create a todo first
        create_response = client.post("/todos", json=sample_todo_data)
        create_response.raise_for_status()
        todo_id = create_response.json()["id"]
        
        response = client.delete(f"/todos/{todo_id}")
        
        assert response.status_code == 204
        
        # Verify it's deleted
        get_response = client.get(f"/todos/{todo_id}")
        assert get_response.status_code == 404
    
    def test_delete_todo_not_found(self, client: TestClient):
        """Test deleting a todo that doesn't exist."""
        response = client.delete("/todos/99999")
        
        assert response.status_code == 404


class TestRootEndpoint:
    """Tests for root endpoint."""
    
    def test_root_endpoint(self, client: TestClient):
        """Test root endpoint returns API info."""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert "docs" in data


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_endpoint(self, client: TestClient):
        """Test health check endpoint."""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"