"""Router definitions for the Todo API.

All CRUD endpoints are defined here. The router is included in the main
application via ``app.include_router``.
"""

from fastapi import APIRouter, HTTPException, Depends, status, Response
from sqlmodel import Session, select

from ..database import get_session
from ..models import Todo, TodoCreate, TodoRead, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])


def get_db() -> Session:
    """FastAPI dependency that provides a database session.

    The session is automatically closed after the request.
    """
    with get_session() as session:
        yield session


@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db)) -> TodoRead:
    """Create a new todo item.

    Parameters
    ----------
    todo_in: TodoCreate
        The data for the new todo.
    db: Session
        Database session provided by FastAPI dependency injection.
    """
    todo = Todo.from_orm(todo_in)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.get("/", response_model=list[TodoRead])
def list_todos(db: Session = Depends(get_db)) -> list[TodoRead]:
    """Return a list of all todo items."""
    todos = db.exec(select(Todo)).all()
    return todos


@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, db: Session = Depends(get_db)) -> TodoRead:
    """Retrieve a single todo item by its ID."""
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)) -> TodoRead:
    """Fully replace a todo item.

    All fields are optional; only provided fields are updated.
    """
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo_in.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(todo, key, value)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Response:
    """Delete a todo item.

    Returns a 204 No Content response on success.
    """
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
