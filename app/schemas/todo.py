# app/schemas/todo.py
from __future__ import annotations

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class TodoRead(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
