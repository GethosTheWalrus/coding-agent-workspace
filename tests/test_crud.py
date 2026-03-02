"""Unit tests for CRUD operations."""

import pytest
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.crud import (
    create_todo,
    get_todo,
    get_todos,
    update_todo,
    delete_todo,
    get_todo_count,
)
from app.schemas import TodoCreate, TodoUpdate


class TestCreateTodo:
    """Tests for create_todo function."""

    def test_create_todo_with_valid_data(self, test_db: Session):
        """Test creating a todo with valid data."""
        todo_data = TodoCreate(
            title="Test Todo", description="Test description", completed=False
        )

        result = create_todo(test_db, todo_data)

        assert result.id is not None
        assert result.title == "Test Todo"
        assert result.description == "Test description"
        assert result.completed is False

    def test_create_todo_with_minimal_data(self, test_db: Session):
        """Test creating a todo with only required fields."""
        todo_data = TodoCreate(title="Minimal Todo")

        result = create_todo(test_db, todo_data)

        assert result.id is not None
        assert result.title == "Minimal Todo"
        assert result.description is None
        assert result.completed is False

    def test_create_todo_sets_timestamps(self, test_db: Session):
        """Test that creating a todo sets created_at timestamp."""
        todo_data = TodoCreate(title="Timestamp Test")

        result = create_todo(test_db, todo_data)

        assert result.created_at is not None


class TestGetTodo:
    """Tests for get_todo function."""

    def test_get_existing_todo(self, test_db: Session):
        """Test retrieving an existing todo."""
        # Create a todo first
        todo_data = TodoCreate(title="Get Test")
        created = create_todo(test_db, todo_data)

        # Retrieve it
        result = get_todo(test_db, created.id)

        assert result is not None
        assert result.id == created.id
        assert result.title == "Get Test"

    def test_get_nonexistent_todo(self, test_db: Session):
        """Test retrieving a todo that doesn't exist."""
        result = get_todo(test_db, 99999)

        assert result is None


class TestGetTodos:
    """Tests for get_todos function."""

    def test_get_all_todos(self, test_db: Session):
        """Test retrieving all todos."""
        # Create multiple todos
        for i in range(3):
            create_todo(test_db, TodoCreate(title=f"Todo {i}"))

        result = get_todos(test_db)

        assert len(result) == 3

    def test_get_todos_with_pagination(self, test_db: Session):
        """Test retrieving todos with pagination."""
        # Create multiple todos
        for i in range(5):
            create_todo(test_db, TodoCreate(title=f"Todo {i}"))

        result = get_todos(test_db, skip=0, limit=2)

        assert len(result) == 2

    def test_get_todos_with_completed_filter(self, test_db: Session):
        """Test retrieving todos filtered by completion status."""
        # Create todos with different completion status
        create_todo(test_db, TodoCreate(title="Completed", completed=True))
        create_todo(test_db, TodoCreate(title="Not Completed", completed=False))
        create_todo(test_db, TodoCreate(title="Another Completed", completed=True))

        completed_todos = get_todos(test_db, completed=True)
        incomplete_todos = get_todos(test_db, completed=False)

        assert len(completed_todos) == 2
        assert len(incomplete_todos) == 1


class TestUpdateTodo:
    """Tests for update_todo function."""

    def test_update_existing_todo(self, test_db: Session):
        """Test updating an existing todo."""
        # Create a todo first
        todo_data = TodoCreate(title="Original Title")
        created = create_todo(test_db, todo_data)

        # Update it
        update_data = TodoUpdate(title="Updated Title", completed=True)
        result = update_todo(test_db, created.id, update_data)

        assert result is not None
        assert result.title == "Updated Title"
        assert result.completed is True

    def test_update_todo_partial_fields(self, test_db: Session):
        """Test updating only some fields of a todo."""
        # Create a todo first
        todo_data = TodoCreate(title="Original", description="Original desc")
        created = create_todo(test_db, todo_data)

        # Update only title
        update_data = TodoUpdate(title="New Title")
        result = update_todo(test_db, created.id, update_data)

        assert result.title == "New Title"
        assert result.description == "Original desc"

    def test_update_nonexistent_todo(self, test_db: Session):
        """Test updating a todo that doesn't exist."""
        update_data = TodoUpdate(title="New Title")
        result = update_todo(test_db, 99999, update_data)

        assert result is None


class TestDeleteTodo:
    """Tests for delete_todo function."""

    def test_delete_existing_todo(self, test_db: Session):
        """Test deleting an existing todo."""
        # Create a todo first
        todo_data = TodoCreate(title="Delete Me")
        created = create_todo(test_db, todo_data)

        # Delete it
        result = delete_todo(test_db, created.id)

        assert result is True
        assert get_todo(test_db, created.id) is None

    def test_delete_nonexistent_todo(self, test_db: Session):
        """Test deleting a todo that doesn't exist."""
        result = delete_todo(test_db, 99999)

        assert result is False


class TestGetTodoCount:
    """Tests for get_todo_count function."""

    def test_get_total_count(self, test_db: Session):
        """Test getting total count of todos."""
        # Create multiple todos
        for i in range(5):
            create_todo(test_db, TodoCreate(title=f"Todo {i}"))

        count = get_todo_count(test_db)

        assert count == 5

    def test_get_count_with_filter(self, test_db: Session):
        """Test getting count with completion filter."""
        # Create todos with different completion status
        create_todo(test_db, TodoCreate(title="Completed", completed=True))
        create_todo(test_db, TodoCreate(title="Not Completed", completed=False))
        create_todo(test_db, TodoCreate(title="Another Completed", completed=True))

        completed_count = get_todo_count(test_db, completed=True)
        incomplete_count = get_todo_count(test_db, completed=False)

        assert completed_count == 2
        assert incomplete_count == 1
