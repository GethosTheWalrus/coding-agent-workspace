"""CRUD utility functions for Todo items.

These functions are used by the API routers to interact with the database.
Each function receives a `Session` object (provided by the FastAPI dependency
`get_session`).
"""

from typing import List, Optional

from sqlmodel import Session, select

from . import models


def get_todo_by_id(session: Session, todo_id: int) -> Optional[models.Todo]:
    """Retrieve a single Todo by its ID.
    """
    return session.get(models.Todo, todo_id)


def get_todos(session: Session, *, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    """Return a list of Todos with pagination support.
    """
    statement = select(models.Todo).offset(skip).limit(limit)
    results = session.exec(statement)
    return results.all()


def create_todo(session: Session, todo: models.TodoCreate) -> models.Todo:
    """Create a new Todo record.
    """
    db_todo = models.Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def update_todo(
    session: Session, *, todo_id: int, todo_update: models.TodoUpdate
) -> Optional[models.Todo]:
    """Update an existing Todo. Returns the updated Todo or None if not found.
    """
    db_todo = session.get(models.Todo, todo_id)
    if not db_todo:
        return None
    todo_data = todo_update.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def delete_todo(session: Session, todo_id: int) -> bool:
    """Delete a Todo by ID. Returns True if deleted, False if not found.
    """
    db_todo = session.get(models.Todo, todo_id)
    if not db_todo:
        return False
    session.delete(db_todo)
    session.commit()
    return True
