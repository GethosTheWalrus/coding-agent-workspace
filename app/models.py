from sqlmodel import SQLModel, Field


class TodoBase(SQLModel):
    title: str
    description: str | None = None
    completed: bool = False


class Todo(TodoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
