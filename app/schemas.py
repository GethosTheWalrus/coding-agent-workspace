"""Pydantic schemas for the Todo API.

These schemas define the shape of data that the API expects in requests and
returns in responses. They are deliberately separate from the SQLAlchemy
models to keep the layers decoupled.
"""

from pydantic import BaseModel, Field
from typing import Optional

class TodoBase(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    completed: bool = Field(False, example=False)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True
