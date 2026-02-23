"""SQLAlchemy models for the Todo application.

Only a single `Todo` model is required, representing a task with a title,
optional description, and a completion flag.
"""

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
