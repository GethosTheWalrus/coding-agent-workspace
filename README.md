# FastAPI Todo API

A simple **Todo** application exposing a RESTful API built with **FastAPI** and **SQLite**. The project is fully containerised with Docker‑Compose and includes a minimal static frontend served by Nginx.

## Features
- CRUD endpoints for Todo items (`id`, `title`, `description`, `completed`).
- SQLite database persisted in a Docker volume.
- Dockerised backend, frontend and database services.
- GitHub Actions CI pipeline that builds the Docker image and runs the test suite.
- High test coverage (>90%).

## Architecture
See the architecture diagram and description in [`docs/architecture.md`](docs/architecture.md).

## Getting Started
```bash
# Clone the repository
git clone <repo-url>
cd <repo-dir>

# Build and start the services
docker compose up --build -d
```
The API will be available at `http://localhost:8000/todos/` and the static UI at `http://localhost:8080/`.

## Running Tests Locally
```bash
# Run tests inside the backend container (or locally if you have the deps)
docker compose run --rm backend pytest -q
```

## Development
- **Backend**: Implement the models, schemas, CRUD helpers and routers in the `app/` package.
- **Frontend**: Add UI components in the `frontend/` directory.
- **CI**: The workflow in `.github/workflows/ci.yml` runs on every push.

---
*Architecture designed by the System Architect. Implementation tasks are tracked in GitHub issues.*
