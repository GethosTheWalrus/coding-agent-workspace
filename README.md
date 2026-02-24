# FastAPI Todo API

A simple Todo REST API built with **FastAPI** and **SQLite**. The project includes:

- CRUD endpoints for todo items (create, read, update, delete)
- Pydantic models for request/response validation
- SQLAlchemy ORM with a SQLite database
- Automated tests with **pytest** achieving >90% coverage
- CI pipeline using **GitHub Actions**
- A minimal frontend UI (to be implemented)

## Project Structure

```
.
├── app/                     # FastAPI application package
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # DB engine & session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # CRUD helper functions (TODO)
│   └── routers/
│       └── todo.py          # Todo router (TODO)
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── test_todo.py         # Placeholder tests (TODO)
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignored files
├── docs/
│   └── architecture.md      # System architecture documentation
└── README.md                # This file
```

## Getting Started

```bash
# Clone the repo
git clone <repo-url>
cd <repo-dir>

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. OpenAPI docs are at `http://127.0.0.1:8000/docs`.

## Running Tests

```bash
pytest --cov=app --cov-report=term-missing
```

## CI

GitHub Actions will automatically run the test suite on each push and pull request. See `.github/workflows/ci.yml` for details.

## Next Steps

- Implement the CRUD logic in `app/crud.py` and route definitions in `app/routers/todo.py` (Backend Developer).
- Write comprehensive tests covering all endpoints (QA Tester).
- Set up CI pipeline (DevOps Engineer).
- Build a minimal frontend UI to interact with the API (Frontend Developer).
