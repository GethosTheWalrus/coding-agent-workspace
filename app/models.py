"""SQLAlchemy ORM model for Todo items."""

from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = """Title of the todo item"""
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
