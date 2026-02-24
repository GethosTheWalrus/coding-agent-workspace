from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from .. import models, database

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=models.Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: models.TodoBase, session: Session = Depends(database.get_session)):
    db_todo = models.Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/", response_model=list[models.Todo])
def read_todos(session: Session = Depends(database.get_session)):
    todos = session.exec(select(models.Todo)).all()
    return todos


@router.get("/{todo_id}", response_model=models.Todo)
def read_todo(todo_id: int, session: Session = Depends(database.get_session)):
    todo = session.get(models.Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=models.Todo)
def update_todo(todo_id: int, todo_update: models.TodoBase, session: Session = Depends(database.get_session)):
    todo = session.get(models.Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = todo_update.title
    todo.title = todo_update.title
    todo.description = todo_update.description
    todo.completed = todo_update.completed
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: Session = Depends(database.get_session)):
    todo = session.get(models.Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo)"
    session.delete(todo)
    session.commit()
    return None
