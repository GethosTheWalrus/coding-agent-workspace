"""SQLAlchemy models for the Todo application.

Defines the Todo model with fields:
- id (Integer, primary key)
- title (String, required)
- description (String, optional)
- completed (Boolean, default False)
"""

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
