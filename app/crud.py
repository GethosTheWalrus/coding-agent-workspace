# app/crud.py
"""CRUD helper functions for Todo items.

These functions interact with the database session to perform create,
read, update, and delete operations.
"""

from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    """Create a new Todo record in the database.

    Args:
        db: SQLAlchemy Session.
        todo: Pydantic schema with data for the new Todo.
    Returns:
        The created Todo model instance.
    """
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    """Retrieve a Todo by its ID.
    """
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    """Return a list of Todos with pagination support.
    """
    return db.query(models.Todo).offset(skip).limit(limit).all()

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate) -> Optional[models.Todo]:
    """Update fields of an existing Todo.
    """
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    update_data = todo_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a Todo by ID. Returns True if deleted, False if not found.
    """
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
