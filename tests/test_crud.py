"""Unit tests for CRUD operations."""
import pytest
from sqlalchemy.orm import Session
from app.crud import create_todo, get_todo, get_all_todos, update_todo, delete_todo
from app.schemas import TodoCreate, TodoUpdate


class TestCreateTodo:
    """Tests for create_todo function."""
    
    def test_create_todo_with_title_only(self, db_session: Session):
        """Test creating a todo with only title."""
        todo_data = TodoCreate(title="Test Todo")
        result = create_todo(db=db_session, todo=todo_data)
        
        assert result.id is not None
        assert result.title == "Test Todo"
        assert result.description is None
        assert result.completed is False
    
    def test_create_todo_with_title_and_description(self, db_session: Session):
        """Test creating a todo with title and description."""
        todo_data = TodoCreate(
            title="Test Todo",
            description="Test description"
        )
        result = create_todo(db=db_session, todo=todo_data)
        
        assert result.id is not None
        assert result.title == "Test Todo"
        assert result.description == "Test description"
        assert result.completed is False
    
    def test_create_todo_persists_to_database(self, db_session: Session):
        """Test that created todo is persisted in database."""
        todo_data = TodoCreate(title="Persistent Todo")
        create_todo(db=db_session, todo=todo_data)
        
        # Query directly to verify persistence
        todos = db_session.query(Todo).all()
        assert len(todos) == 1
        assert todos[0].title == "Persistent Todo"


class TestGetTodo:
    """Tests for get_todo function."""
    
    def test_get_todo_found(self, db_session: Session, created_todo):
        """Test getting an existing todo."""
        result = get_todo(db=db_session, todo_id=created_todo.id)
        
        assert result is not None
        assert result.id == created_todo.id
        assert result.title == created_todo.title
    
    def test_get_todo_not_found(self, db_session: Session):
        """Test getting a non-existent todo."""
        result = get_todo(db=db_session, todo_id=999)
        
        assert result is None


class TestGetAllTodos:
    """Tests for get_all_todos function."""
    
    def test_get_all_todos_empty(self, db_session: Session):
        """Test getting todos when database is empty."""
        result = get_all_todos(db=db_session)
        
        assert result == []
    
    def test_get_all_todos_with_data(self, db_session: Session):
        """Test getting all todos."""
        # Create multiple todos
        for i in range(3):
            todo_data = TodoCreate(title=f"Todo {i}")
            create_todo(db=db_session, todo=todo_data)
        
        result = get_all_todos(db=db_session)
        
        assert len(result) == 3
    
    def test_get_all_todos_with_pagination(self, db_session: Session):
        """Test getting todos with skip and limit."""
        # Create 5 todos
        for i in range(5):
            todo_data = TodoCreate(title=f"Todo {i}")
            create_todo(db=db_session, todo=todo_data)
        
        # Test skip
        result = get_all_todos(db=db_session, skip=2)
        assert len(result) == 3
        
        # Test limit
        result = get_all_todos(db=db_session, limit=2)
        assert len(result) == 2
        
        # Test skip and limit
        result = get_all_todos(db=db_session, skip=1, limit=2)
        assert len(result) == 2


class TestUpdateTodo:
    """Tests for update_todo function."""
    
    def test_update_todo_found(self, db_session: Session, created_todo):
        """Test updating an existing todo."""
        update_data = TodoUpdate(title="Updated Title", completed=True)
        result = update_todo(db=db_session, todo_id=created_todo.id, todo=update_data)
        
        assert result is not None
        assert result.title == "Updated Title"
        assert result.completed is True
    
    def test_update_todo_partial(self, db_session: Session, created_todo):
        """Test partial update of a todo."""
        update_data = TodoUpdate(completed=True)
        result = update_todo(db=db_session, todo_id=created_todo.id, todo=update_data)
        
        assert result is not None
        assert result.title == created_todo.title  # Unchanged
        assert result.completed is True
    
    def test_update_todo_not_found(self, db_session: Session):
        """Test updating a non-existent todo."""
        update_data = TodoUpdate(title="Updated Title")
        result = update_todo(db=db_session, todo_id=999, todo=update_data)
        
        assert result is None


class TestDeleteTodo:
    """Tests for delete_todo function."""
    
    def test_delete_todo_found(self, db_session: Session, created_todo):
        """Test deleting an existing todo."""
        result = delete_todo(db=db_session, todo_id=created_todo.id)
        
        assert result is True
        
        # Verify todo is deleted
        todo = get_todo(db=db_session, todo_id=created_todo.id)
        assert todo is None
    
    def test_delete_todo_not_found(self, db_session: Session):
        """Test deleting a non-existent todo."""
        result = delete_todo(db=db_session, todo_id=999)
        
        assert result is False
    
    def test_delete_todo_removes_from_database(self, db_session: Session, created_todo):
        """Test that deleted todo is removed from database."""
        delete_todo(db=db_session, todo_id=created_todo.id)
        
        todos = db_session.query(Todo).all()
        assert len(todos) == 0