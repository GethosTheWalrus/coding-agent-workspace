"""Pydantic schemas for request validation and response serialization.

- `TodoBase` contains shared fields.
- `TodoCreate` is used for POST requests (title required).
- `TodoUpdate` allows partial updates.
- `TodoResponse` is returned to clients and includes the DB-generated fields.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., max_length=200)
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


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
