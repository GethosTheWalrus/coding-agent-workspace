"""Pydantic schemas for request and response bodies.

- TodoBase: shared fields (title, description, completed)
- TodoCreate: inherits from TodoBase, used for POST requests
- TodoUpdate: all fields optional for PATCH requests
- TodoRead: includes id and timestamps, used for responses
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., max_length=200)
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
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
