"""SQLAlchemy ORM model for a Todo item.

Fields:
- id: Primary key, integer.
- title: Short description of the task.
- description: Optional longer text.
- completed: Boolean flag indicating if the task is done.
- created_at: Timestamp when the record was created.
- updated_at: Timestamp when the record was last updated.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.db.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
