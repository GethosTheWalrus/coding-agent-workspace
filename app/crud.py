"""CRUD helper functions for Todo items.

All functions should accept a SQLAlchemy `Session` and perform the
appropriate operation, returning Pydantic models where appropriate.

TODO: Implement the following functions:
- `create_todo`
- `get_todo`
- `get_todos`
- `update_todo`
- `delete_todo`
"""

from sqlalchemy.orm import Session
from . import models, schemas

# TODO: Implement CRUD operations

def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    pass

def get_todo(db: Session, todo_id: int) -> models.Todo | None:
    pass

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    pass

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate) -> models.Todo | None:
    pass

def delete_ttodo(db: Session, todo_id: int) -> bool:
    pass
