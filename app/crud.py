"""CRUD helper functions for Todo items.

All functions accept a SQLAlchemy `Session` and perform the appropriate
operation, returning SQLAlchemy model instances. Pydantic schemas are used
by the API layer for request validation and response serialization.
"""

from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, todo_id: int) -> models.Todo | None:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate) -> models.Todo | None:
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        return None
    update_data = todo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
