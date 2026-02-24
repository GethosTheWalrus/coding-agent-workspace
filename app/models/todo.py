"""SQLAlchemy model definitions for the Todo API.

The `Todo` model represents a single todo item with a title, optional description,
completion status, and timestamps.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.db.base import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
