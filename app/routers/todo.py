# app/routers/todo.py
"""Todo router – implements CRUD operations for Todo items.

All endpoints interact with the SQLite database via a ``Session`` dependency.
Responses are validated against the ``TodoRead`` model, ensuring a stable API
contract.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import Todo, TodoCreate, TodoRead

router = APIRouter()

@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(*, session: Session = Depends(get_session), todo: TodoCreate):
    """Create a new Todo item.

    The ``TodoCreate`` payload is transformed into a ``Todo`` ORM instance and
    persisted. The newly created record (including its generated ``id``) is
    returned.
    """
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/", response_model=list[TodoRead])
def read_todos(*, session: Session = Depends(get_session)):
    """Retrieve all Todo items.

    Returns a list of ``TodoRead`` objects representing each row in the
    ``todos`` table.
    """
    todos = session.exec(select(Todo)).all()
    return todos

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(*, session: Session = Depends(get_session), todo_id: int):
    """Retrieve a single Todo by its ``id``.

    Raises ``404`` if the Todo does not exist.
    """
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(*, session: Session = Depends(get_session), todo_id: int, todo: TodoCreate):
    """Update an existing Todo.

    The request body contains the new values for ``title``, ``description``
    and ``completed``. The ``id`` is taken from the path parameter.
    """
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    # Update fields
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(*, session: Session = Depends(get_session), todo_id: int):
    """Delete a Todo by ``id``.

    Returns ``204 No Content`` on success. Raises ``404`` if the Todo does not
    exist.
    """
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(db_todo)
    session.commit()
    return None
