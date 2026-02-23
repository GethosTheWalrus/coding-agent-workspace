"""Router definitions for Todo CRUD operations.

All routes are prefixed with ``/todos`` and use the ``get_db`` dependency
from ``app.database`` to obtain a SQLAlchemy session.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo_in)


@router.get("/", response_model=schemas.TodoList)
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return schemas.TodoList(todos=todos, total=len(todos))


@router.get("/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.put("/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo_in: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, db_todo, todo_in)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    crud.delete_todo(db, db_todo)
    return None
