"""Pydantic schemas for request and response validation of Todo items."""

from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        orm_mode = True


class TodoInDBBase(TodoBase):
    id: int

    class Config:
        orm_mode = True


class Todo(TodoInDBBase):
    pass
