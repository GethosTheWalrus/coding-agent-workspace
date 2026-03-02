"""SQLAlchemy models for the Todo application."""
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Todo(Base):
    """Todo item model."""
    
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    completed = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}', completed={self.completed})>"