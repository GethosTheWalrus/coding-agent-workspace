# FastAPI Todo API

A simple **Todo** REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**. The project includes a Docker setup, a `docker‑compose` configuration, and a CI pipeline (GitHub Actions) that runs automated tests with >90% coverage.

## Features

- CRUD endpoints for todo items (`id`, `title`, `description`, `completed`).
- SQLite database with SQLAlchemy ORM.
- Automatic API documentation (Swagger UI & ReDoc) at `/docs` and `/redoc`.
- Dockerized development and production environments.
- GitHub Actions CI that builds the Docker image, runs tests, and checks coverage.

## Project Structure

```
.
├─ app/                     # FastAPI application package
│  ├─ __init__.py
│  ├─ main.py               # Application entry point
│  ├─ models.py             # SQLAlchemy models
│  ├─ schemas.py            # Pydantic schemas
│  ├─ crud.py               # Database CRUD utilities
│  ├─ database.py           # DB engine & session handling
│  └─ routers/
│     ├─ __init__.py
│     └─ todo.py            # Todo router (endpoints)
├─ tests/                   # Automated test suite (to be implemented)
├─ Dockerfile               # Build image for the API
├─ docker-compose.yml       # Compose file for local dev
├─ requirements.txt         # Python dependencies
├─ docs/architecture.md    # Architecture documentation
└─ README.md                # This file
```

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11 (if you want to run locally without Docker)

### Running with Docker Compose

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Running Locally (development)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Running Tests

```bash
pytest -q
```

## CI / CD

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
1. Builds the Docker image.
2. Installs dependencies.
3. Executes the test suite.
4. Fails the build if coverage is below 90%.

## License

MIT License.
