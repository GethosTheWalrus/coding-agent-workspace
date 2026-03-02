"""CRUD operations for Todo items."""
from typing import List, Optional
from sqlalchemy.orm import Session

from .models import Todo
from .schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    """Create a new todo item.
    
    Args:
        db: Database session
        todo: TodoCreate schema with todo data
        
    Returns:
        Created Todo model instance
    """
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(db: Session, skip: int = 0, limit: int = 100, completed: Optional[bool] = None) -> List[Todo]:
    """Retrieve all todo items with optional filtering.
    
    Args:
        db: Database session
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return
        completed: Optional filter by completion status
        
    Returns:
        List of Todo model instances
    """
    query = db.query(Todo)
    
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    
    return query.offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """Retrieve a single todo item by ID.
    
    Args:
        db: Database session
        todo_id: ID of the todo to retrieve
        
    Returns:
        Todo model instance or None if not found
    """
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    """Update an existing todo item.
    
    Args:
        db: Database session
        todo_id: ID of the todo to update
        todo_update: TodoUpdate schema with updated data
        
    Returns:
        Updated Todo model instance or None if not found
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if db_todo is None:
        return None
    
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a todo item by ID.
    
    Args:
        db: Database session
        todo_id: ID of the todo to delete
        
    Returns:
        True if deleted, False if not found
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if db_todo is None:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True