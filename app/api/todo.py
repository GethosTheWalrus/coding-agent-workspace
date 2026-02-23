from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas, models
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.todo.TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: schemas.todo.TodoCreate, db: Session = Depends(get_db)):
    return crud.todo.create_todo(db=db, todo_in=todo_in)

@router.get("/", response_model=List[schemas.todo.TodoRead])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.todo.get_todos(db=db, skip=skip, limit=limit)
    return todos

@router.get("/{todo_id}", response_model=schemas.todo.TodoRead)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.todo.get_todo(db=db, todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=schemas.todo.TodoRead)
def update_todo(todo_id: int, todo_in: schemas.todo.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.todo.get_todo(db=db, todo_id=todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.todo.update_todo(db=db, db_todo=db_todo, todo_in=todo_in)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.todo.get_todo(db=db, todo_id=todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo "
                            "Todo not found")
    crud.todo.delete_todo(db=db, db_todo=db_todo)
    return None
