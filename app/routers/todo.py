"""Router for Todo CRUD operations (skeleton)."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models, db

router = APIRouter(prefix="/todos", tags=["todos"])

# Dependency to get DB session
def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# Placeholder endpoints – to be implemented by backend developer
@router.post("/", response_model=schemas.Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    raise NotImplementedError("Create todo not implemented yet")

@router.get("/", response_model=List[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raise NotImplementedError("Read todos not implemented yet")

@router.get("/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    raise NotImplementedError("Read todo not implemented yet")

@router.put("/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    raise NotImplementedError("Update todo not implemented now")

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    raise NotImplementedError("Delete todo not implemented yet")
