# Todo API with FastAPI and SQLite

A simple **RESTful** Todo application built with **FastAPI**, **SQLAlchemy**, and **SQLite**. The API supports creating, reading, updating, and deleting todo items.

## Features
- FastAPI for high‑performance async API
- SQLite as a lightweight, file‑based database
- SQLAlchemy ORM for database interactions
- Pydantic models for request validation and response schemas
- Automatic interactive docs (Swagger UI & ReDoc)

## Project Structure
```
app/
├── __init__.py
├── main.py            # FastAPI application entry point
├── database.py        # DB engine & session handling
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── crud.py            # CRUD helper functions
└── routers/
    └── todo.py        # Todo endpoints

tests/
    └── test_main.py   # Basic integration tests

docs/
    └── architecture.md # Architecture overview
requirements.txt        # Project dependencies
```

## Getting Started
### Prerequisites
- Python 3.9+ installed on your machine
- `git` (optional, for cloning the repo)

### Installation
```bash
# Clone the repository (if applicable)
git clone <repo-url>
cd <repo-directory>

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Running the API
```bash
uvicorn app.main:app --reload
```
The server will start at `http://127.0.0.1:8000`. You can explore the automatic documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Running Tests
```bash
pip install pytest httpx
pytest
```

## API Endpoints
| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/todos/` | List all todos |
| `GET` | `/todos/{todo_id}` | Retrieve a single todo |
| `POST` | `/todos/` | Create a new todo |
| `PUT` | `/todos/{todo_id}` | Update an existing todo |
| `DELETE` | `/todos/{todo_id}` | Delete a todo |

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
