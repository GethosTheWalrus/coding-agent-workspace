"""CRUD operations for the Todo model.

These functions are deliberately thin wrappers around SQLAlchemy session
methods. They are used by the API routers to keep the endpoint code tidy.
"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    """Retrieve a single Todo by its ID."""
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    """Return a list of Todos with optional pagination."""
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo_in: schemas.TodoCreate) -> models.Todo:
    """Create a new Todo record from a Pydantic schema."""
    db_todo = models.Todo(**todo_in.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, db_todo: models.Todo, todo_in: schemas.TodoUpdate) -> models.Todo:
    """Update fields of an existing Todo.

    Only fields present in ``todo_in`` (i.e., not ``None``) are updated.
    """
    update_data = todo_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, db_todo: models.Todo) -> None:
    """Delete a Todo from the database."""
    db.delete(db_todo)
    db.commit()
