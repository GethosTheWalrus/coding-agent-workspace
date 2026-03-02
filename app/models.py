"""SQLAlchemy ORM models for the Todo API."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base


class Todo(Base):
    """Todo item model representing a single todo in the database."""
    
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    def __repr__(self):
        """String representation of the Todo model."""
        return f"<Todo(id={self.id}, title='{self.title}', completed={self.completed})>"