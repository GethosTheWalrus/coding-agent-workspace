"""CRUD operations for the Todo model.

These functions are used by the API routers to interact with the database.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """Retrieve a single Todo by its ID."""
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Todo]:
    """Retrieve a list of Todos with pagination support."""
    return db.query(Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo_in: TodoCreate) -> Todo:
    """Create a new Todo record in the database."""
    db_todo = Todo(**todo_in.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, db_todo: Todo, todo_in: TodoUpdate) -> Todo:
    """Update an existing Todo with the provided fields."""
    update_data = todo_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, db_todo: Todo) -> Todo:
    """Delete a Todo from the database and return the deleted object."""
    db.delete(db_todo)
    db.commit()
    return db_todo
