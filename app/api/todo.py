"""FastAPI router for Todo CRUD operations.

Endpoints:
- GET /todos/            → list todos (pagination)
- GET /todos/{id}        → retrieve a single todo
- POST /todos/           → create a new todo
- PUT /todos/{id}        → update an existing todo
- DELETE /todos/{id}     → delete a todo
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import todo as crud_todo
from app.schemas.todo import (
    TodoResponse,
    TodoCreate,
    TodoUpdate,
)
from app.db.base import get_db

router = APIRouter()

# List todos
@router.get("/", response_model=list[TodoResponse])
async def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud_todo.get_todos(db, skip=skip, limit=limit)
    return todos

# Get a single todo
@router.get("/{todo_id}", response_model=TodoResponse)
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud_todo.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Create a new todo
@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    return crud_todo.create_todo(db, todo_in)

# Update an existing todo
@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud_todo.update_todo(db, db_todo, todo_in)

# Delete a todo
@router.delete("/{todo_id}", response_model=TodoResponse)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud_todo.delete_todo(db, db_todo)
