"""SQLAlchemy models for the Todo API.

Only a single ``Todo`` model is required for this simple application.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from .database import Base


class Todo(Base):
    """Model representing a todo item.

    Attributes
    ----------
    id: int
        Primary key, auto‑incremented.
    title: str
        Short description of the task.
    description: Optional[str]
        Longer optional details.
    completed: bool
        Completion flag – defaults to ``False``.
    created_at: datetime
        Timestamp when the record was created.
    updated_at: datetime
        Timestamp of the last update.
    """

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Todo id={self.id} title={self.title!r}>"
