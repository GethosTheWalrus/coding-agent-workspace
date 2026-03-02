"""CRUD operations for Todo items."""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    """
    Create a new todo item.
    
    Args:
        db: Database session
        todo: TodoCreate schema with title and optional description
    
    Returns:
        The created Todo model instance
    """
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """
    Get a todo item by ID.
    
    Args:
        db: Database session
        todo_id: The ID of the todo to retrieve
    
    Returns:
        Todo model if found, None otherwise
    """
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_all_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Todo]:
    """
    Get all todo items.
    
    Args:
        db: Database session
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return
    
    Returns:
        List of Todo model instances
    """
    return db.query(Todo).offset(skip).limit(limit).all()


def update_todo(db: Session, todo_id: int, todo: TodoUpdate) -> Optional[Todo]:
    """
    Update an existing todo item.
    
    Args:
        db: Database session
        todo_id: The ID of the todo to update
        todo: TodoUpdate schema with fields to update
    
    Returns:
        Updated Todo model if found, None otherwise
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if db_todo is None:
        return None
    
    # Update only provided fields
    update_data = todo.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> bool:
    """
    Delete a todo item.
    
    Args:
        db: Database session
        todo_id: The ID of the todo to delete
    
    Returns:
        True if deleted, False if todo not found
    """
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if db_todo is None:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True