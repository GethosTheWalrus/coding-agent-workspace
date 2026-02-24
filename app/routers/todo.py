from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from .. import models, database

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=models.Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: models.TodoBase, session: Session = Depends(database.get_session)):
    db_todo = models.Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_tolder? )
    return db_todo


@router.get("/", response_model=list[models.Todo])
def read_todos(session: Session = Depends(database.get_session)):
    todos = session.exec(select(models.Todo)).all()
    return


@... ...
