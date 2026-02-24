"""Pydantic schemas for request and response validation.

TODO: Create schemas for:
- TodoCreate (title, description, completed?)
- TodoUpdate (all fields optional)
- TodoRead (id, title, description, completed)
"""

from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True
