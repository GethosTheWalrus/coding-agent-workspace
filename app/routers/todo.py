"""Router for Todo CRUD operations.

Provides endpoints to create, read, update, and delete Todo items.
Uses the `get_session` dependency from `app.database` for database
access via SQLModel sessions.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import Todo, TodoCreate, TodoRead, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(*, session: Session = Depends(get_session), todo: TodoCreate):
    """Create a new Todo item."""
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/", response_model=list[TodoRead])
def read_todos(*, session: Session = Depends(get_session)):
    """Retrieve all Todo items."""
    todos = session.exec(select(Todo)).all()
    return todos

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(*, session: Session = Depends(get_session), todo_id: int):
    """Retrieve a single Todo by its ID."""
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(*, session: Session = Depends(get_session), todo_id: int, todo: TodoUpdate):
    """Update an existing Todo item. Only provided fields are changed."""
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(*, session: Session = Depends(get_session), todo_id: int):
    """Delete a Todo item by ID."""
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(db_todo)
    session.commit()
    return None
