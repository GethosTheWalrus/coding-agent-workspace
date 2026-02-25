"""Todo router defining CRUD endpoints.

All endpoint implementations delegate to the ``crud`` module.  The actual
business logic is left as TODOs for the backend developer.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo item.
    """
    # TODO: Add validation, error handling as needed
    return crud.create_todo(db, todo)


@router.get("/{todo_id}", response_model=schemas.TodoRead)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Retrieve a todo by its ID.
    """
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.get("/", response_model=list[schemas.TodoRead])
def list_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List todos with optional pagination.
    """
    return crud.get_todos(db, skip=skip, limit=limit)


@router.put("/{todo_id}", response_model=schemas.TodoRead)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    """Update an existing todo.
    """
    db_todo = crud.update_todo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo.
    """
    success = crud.delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
