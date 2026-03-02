"""Tests for CRUD operations."""
import pytest
from sqlalchemy.orm import Session

from app.crud import create_todo, get_todos, get_todo, update_todo, delete_todo
from app.schemas import TodoCreate, TodoUpdate


class TestCreateTodo:
    """Tests for create_todo function."""
    
    def test_create_todo_with_valid_data(self, db_session: Session, sample_todo_data):
        """Test creating a todo with valid data."""
        todo_create = TodoCreate(**sample_todo_data)
        result = create_todo(db=db_session, todo=todo_create)
        
        assert result is not None
        assert result.title == sample_todo_data["title"]
        assert result.description == sample_todo_data["description"]
        assert result.completed == sample_todo_data["completed"]
        assert result.id is not None
    
    def test_create_todo_with_minimal_data(self, db_session: Session):
        """Test creating a todo with only required fields."""
        todo_create = TodoCreate(title="Minimal Todo")
        result = create_todo(db=db_session, todo=todo_create)
        
        assert result is not None
        assert result.title == "Minimal Todo"
        assert result.description is None
        assert result.completed == False


class TestGetTodos:
    """Tests for get_todos function."""
    
    def test_get_todos_empty_database(self, db_session: Session):
        """Test getting todos from empty database."""
        result = get_todos(db=db_session)
        assert result == []
    
    def test_get_todos_returns_all_todos(self, db_session: Session, created_todo):
        """Test getting all todos returns created todos."""
        result = get_todos(db=db_session)
        assert len(result) == 1
        assert result[0].id == created_todo.id
    
    def test_get_todos_with_filter_completed(self, db_session: Session, created_todo):
        """Test filtering todos by completed status."""
        # Create another todo with completed=True
        todo_create = TodoCreate(title="Completed Todo", completed=True)
        create_todo(db=db_session, todo=todo_create)
        
        # Filter by completed=False
        result = get_todos(db=db_session, completed=False)
        assert len(result) == 1
        assert result[0].id == created_todo.id
        
        # Filter by completed=True
        result = get_todos(db=db_session, completed=True)
        assert len(result) == 1
        assert result[0].completed == True
    
    def test_get_todos_with_pagination(self, db_session: Session):
        """Test pagination of todos."""
        # Create multiple todos
        for i in range(5):
            todo_create = TodoCreate(title=f"Todo {i}")
            create_todo(db=db_session, todo=todo_create)
        
        # Test skip
        result = get_todos(db=db_session, skip=2, limit=10)
        assert len(result) == 3
        
        # Test limit
        result = get_todos(db=db_session, skip=0, limit=2)
        assert len(result) == 2


class TestGetTodo:
    """Tests for get_todo function."""
    
    def test_get_todo_found(self, db_session: Session, created_todo):
        """Test getting an existing todo."""
        result = get_todo(db=db_session, todo_id=created_todo.id)
        assert result is not None
        assert result.id == created_todo.id
    
    def test_get_todo_not_found(self, db_session: Session):
        """Test getting a non-existent todo."""
        result = get_todo(db=db_session, todo_id=999)
        assert result is None


class TestUpdateTodo:
    """Tests for update_todo function."""
    
    def test_update_todo_found(self, db_session: Session, created_todo):
        """Test updating an existing todo."""
        update_data = TodoUpdate(title="Updated Title", completed=True)
        result = update_todo(db=db_session, todo_id=created_todo.id, todo_update=update_data)
        
        assert result is not None
        assert result.title == "Updated Title"
        assert result.completed == True
    
    def test_update_todo_not_found(self, db_session: Session):
        """Test updating a non-existent todo."""
        update_data = TodoUpdate(title="Updated Title")
        result = update_todo(db=db_session, todo_id=999, todo_update=update_data)
        assert result is None
    
    def test_update_todo_partial(self, db_session: Session, created_todo):
        """Test partial update of a todo."""
        update_data = TodoUpdate(completed=True)
        result = update_todo(db=db_session, todo_id=created_todo.id, todo_update=update_data)
        
        assert result is not None
        assert result.completed == True
        assert result.title == created_todo.title  # Unchanged


class TestDeleteTodo:
    """Tests for delete_todo function."""
    
    def test_delete_todo_found(self, db_session: Session, created_todo):
        """Test deleting an existing todo."""
        result = delete_todo(db=db_session, todo_id=created_todo.id)
        assert result == True
        
        # Verify it's deleted
        deleted_todo = get_todo(db=db_session, todo_id=created_todo.id)
        assert deleted_todo is None
    
    def test_delete_todo_not_found(self, db_session: Session):
        """Test deleting a non-existent todo."""
        result = delete_todo(db=db_session, todo_id=999)
        assert result == False