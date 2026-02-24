# Todo API with FastAPI

A simple RESTful Todo application built with **FastAPI** and **SQLite** using SQLAlchemy for ORM and Pydantic for data validation.

## Features
- Create, read, update, and delete todo items.
- SQLite database (file‑based, no external DB required).
- Clear project structure separating API routes, database models, schemas, and CRUD logic.
- Ready for development with `uvicorn` and for testing with `pytest`.

## Project Structure
```
app/
├── api/            # FastAPI routers (endpoints)
│   └── todo.py
├── crud/           # CRUD helper functions
│   └── todo.py
├── db/             # Database connection and session handling
│   └── base.py
├── models/         # SQLAlchemy models
│   └── todo.py
├── schemas/        # Pydantic schemas for request/response
│   └── todo.py
├── main.py         # FastAPI application entry point
└── __init__.py

tests/              # Test suite (to be added later)

docs/
    └── architecture.md
requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites
- Python 3.9+ installed on your machine.

### Installation
```bash
# Clone the repository
git clone <repo-url>
cd <repo-directory>

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Running the API
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### API Documentation
FastAPI automatically generates interactive docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## License
This project is licensed under the MIT License.
