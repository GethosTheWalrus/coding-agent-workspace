"""SQLModel definitions for Todo items.

The Todo model represents the database table. The TodoCreate and
TodoRead schemas are used for request validation and response
serialization, respectively.
"""

from typing import Optional
from sqlmodel import Field, SQLModel

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

class TodoUpdate:
    title: Optional[str] = None
    description: Optional
    description: """""""
