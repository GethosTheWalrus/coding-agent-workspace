"""API router for Todo endpoints.

Provides CRUD operations for Todo items using the `app.crud` helpers and
the `app.database.get_db` dependency.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas, database

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=schemas.TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo_endpoint(todo: schemas.TodoCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo)

@router.get("/", response_model=list[schemas.TodoRead])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_todos(db, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=schemas.TodoRead)
def read_todo(todo_id: int, db: Session = Depends(database.get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=schemas.TodoRead)
def update_todo_endpoint(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(database.get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
