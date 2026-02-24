"""Router for Todo CRUD operations.

Defines FastAPI endpoints for creating, reading, updating, and deleting
Todo items. Uses the `get_session` dependency from `app.database` to
interact with the SQLite database via SQLModel sessions.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import Todo, TodoCreate, TodoRead, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(*, session: Session = Depends(get_session), todo: TodoCreate):
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/", response_model=list[TodoRead])
def read_todos(*, session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(*, session: Session = Depends(get_session), todo_id: int):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(*, session: Session = Depends(get_session), todo_id: int, todo: TodoUpdate):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not
        """
        """
        """
        """"""""""""""""""""""""""""""
