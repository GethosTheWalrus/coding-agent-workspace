"""CRUD utility functions for the Todo API.

These functions encapsulate database operations and will be used by the API
router.  Implementation details (e.g., handling of integrity errors) are left
as TODOs for the backend developer.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas


def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    """Retrieve a single Todo by its ID.
    """
    # TODO: Implement actual query
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    """Retrieve a list of Todos with pagination.
    """
    # TODO: Implement pagination logic
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    """Create a new Todo record.
    """
    # Convert Pydantic model to dict using model_dump (Pydantic v2)
    todo_data = todo.model_dump()
    db_todo = models.Todo(**todo_data)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate) -> Optional[models.Todo]:
    """Update an existing Todo. Returns the updated object or ``None`` if not found.
    """
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    # Use model_dump with exclude_unset to get only provided fields
    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a Todo by ID. Returns ``True`` if deletion succeeded.
    """
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
