"""CRUD operations for Todo items.

These functions are used by the FastAPI route handlers to interact with the
database. They accept a SQLAlchemy `Session` and return model instances or
simple success flags.
"""

from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate) -> Optional[models.Todo]:
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    update_data = todo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
