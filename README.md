# FastAPI Todo Application

## Overview
This repository contains a simple Todo REST API built with **FastAPI** and **SQLite**. The API supports full CRUD operations for Todo items.

## Getting Started
### Prerequisites
- Docker & Docker‑Compose installed on your machine.

### Running the Application
```bash
# Build and start containers
docker compose up --build -d
```
The backend API will be available at `http://localhost:8000`.

### API Documentation
FastAPI automatically generates interactive docs:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure
```
.
├─ app/                # FastAPI source code
│  ├─ __init__.py
│  ├─ main.py          # Application entry point
│  ├─ models.py        # SQLAlchemy models
│  ├─ schemas.py       # Pydantic schemas
│  ├─ crud.py          # CRUD helper functions (TODO)
│  ├─ database.py      # DB session handling (TODO)
│  └─ routers/
│     └─ todo.py       # Todo router (TODO)
├─ frontend/           # Static files for a simple UI (TODO)
├─ tests/              # Pytest suite (TODO)
├─ Dockerfile          # Backend Docker image
├─ docker-compose.yml  # Compose file for backend, frontend, DB
├─ requirements.txt    # Python dependencies
└─ README.md           # This file
```

## Development
- Implement the missing parts marked with `TODO` in the source files.
- Run tests locally with:
  ```bash
  docker compose run --rm backend pytest -q
  ```

## CI / CD
GitHub Actions will automatically build the Docker image and run the test suite on each push. See `.github/workflows/ci.yml` for details.

---

*All scaffold files contain placeholders (`TODO`) for the backend and frontend developers to fill in.*
