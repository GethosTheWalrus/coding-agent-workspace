# System Architecture

This document outlines the high‑level architecture of the **FastAPI Todo** application.

## Components

```mermaid
flowchart LR
    subgraph DockerCompose[Docker‑Compose]
        direction TB
        Backend[FastAPI Backend] -->|SQLite DB| DB[SQLite (volume)]
        Frontend[Nginx Static Frontend] --> Backend
    end
    classDef backend fill:#f9f,stroke:#333,stroke-width:2px;
    classDef db fill:#bbf,stroke:#333,stroke-width:2px;
    classDef frontend fill:#bfb,stroke:#333,stroke-width:2px;
    class Backend backend;
    class DB db;
    class Frontend frontend;
```

- **FastAPI Backend** – Provides a RESTful API for CRUD operations on Todo items. It uses **SQLAlchemy** with a **SQLite** database stored in a Docker volume.
- **SQLite Database** – Simple file‑based relational store. Persisted across container restarts via a named volume (`db_data`).
- **Nginx Frontend** – Serves static HTML/JS files that interact with the API. (Implementation left to the frontend developer.)
- **Docker‑Compose** – Orchestrates the three services, exposing ports `8000` (API) and `8080` (frontend).

## Data Model

| Model | Fields |
|-------|--------|
| `Todo` | `id: int` (PK), `title: str`, `description: str` (optional), `completed: bool` (default `false`) |

## Interaction Flow
1. **Client** (browser) loads the static UI from the Nginx container.
2. UI makes HTTP requests to `http://localhost:8000/todos/...`.
3. FastAPI routes forward calls to CRUD helpers which interact with the SQLite DB.
4. Responses are returned to the UI.

## Extensibility
- Swap SQLite for PostgreSQL by updating `SQLALCHEMY_DATABASE_URL` and adding the appropriate driver.
- Add authentication middleware (e.g., OAuth2) without changing the core CRUD logic.
- Deploy to Kubernetes – the same Docker images can be used.

---
*Architecture designed by the System Architect. Implementation details are left to the backend, frontend, and DevOps engineers.*
