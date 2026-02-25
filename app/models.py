"""SQLAlchemy models for the Todo API.

Only the ``Todo`` model is defined.  The backend developer will flesh out the
model (e.g., add indexes, constraints) and ensure compatibility with SQLAlchemy
2.0.
"""

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Todo(Base):
    """Todo item model.

    Attributes
    ----------
    id: int
        Primary key.
    title: str
        Short title of the todo item.
    description: str | None
        Optional longer description.
    completed: bool
        Completion flag.
    """

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
