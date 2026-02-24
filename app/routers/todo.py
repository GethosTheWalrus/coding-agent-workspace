"""Todo router – defines the RESTful API endpoints.

All endpoints depend on the `get_session` dependency to obtain a DB session.
Responses use the Pydantic models defined in `app.models` for validation and
serialization.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from .. import crud, models, database

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[models.TodoRead])
def read_todos(
    *, session: Session = Depends(database.get_session), skip: int = 0, limit: int = 100
):
    """Retrieve a list of todos with optional pagination."""
    todos = crud.get_todos(session, skip=skip, limit=limit)
    return todos


@router.post("/", response_model=models.TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(*, session: Session = Depends(database.get_session), todo: models.TodoCreate):
    """Create a new todo item."""
    db_todo = crud.create_todo(session, todo)
    return db_todo


@router.get("/{todo_id}", response_model=models.TodoRead)
def read_todo(*, session: Session = Depends(database.get_session), todo_id: int):
    """Retrieve a single todo by its ID."""
    db_todo = crud.get_todo_by_id(session, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.patch("/{todo_id}", response_model=models.TodoRead)
def update_todo(
    *, session: Session = Depends(database.get_session), todo_id: int, todo: models.TodoUpdate
):
    """Partially update a todo item."""
    db_todo = crud.update_todo(session, todo_id=todo_id, todo_update=todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(*, session: Session = Depends(database.get_session), todo_id: int):
    """Delete a todo item."""
    success = crud.delete_todo(session, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
