"""CRUD operations for Todo items."""

from typing import Optional, List
from sqlalchemy.orm import Session

from .models import Todo
from .schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, todo_create: TodoCreate) -> Todo:
    """
    Create a new todo item.

    Args:
        db: Database session
        todo_create: Schema with todo data

    Returns:
        Created todo item
    """
    db_todo = Todo(
        title=todo_create.title,
        description=todo_create.description,
        completed=todo_create.completed,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """
    Retrieve a todo item by ID.

    Args:
        db: Database session
        todo_id: ID of the todo to retrieve

    Returns:
        Todo item if found, None otherwise
    """
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos(
    db: Session, skip: int = 0, limit: int = 100, completed: Optional[bool] = None
) -> List[Todo]:
    """
    Retrieve all todo items with optional filtering and pagination.

    Args:
        db: Database session
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return
        completed: Optional filter by completion status

    Returns:
        List of todo items
    """
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    return query.offset(skip).limit(limit).all()


def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    """
    Update an existing todo item.

    Args:
        db: Database session
        todo_id: ID of the todo to update
        todo_update: Schema with updated data

    Returns:
        Updated todo item if found, None otherwise
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
    """
    Delete a todo item.

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


def get_todo_count(db: Session, completed: Optional[bool] = None) -> int:
    """
    Get the total count of todo items.

    Args:
        db: Database session
        completed: Optional filter by completion status

    Returns:
        Total count of todo items
    """
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    return query.count()
