# System Architecture

This document outlines the high‑level architecture of the **FastAPI Todo API** project.

## Overview

The application follows a classic **layered architecture**:

1. **API Layer** – FastAPI routers expose HTTP endpoints.
2. **Service/CRUD Layer** – Functions that implement business logic and interact with the database.
3. **Data Access Layer** – SQLAlchemy models and a session manager handle persistence to an SQLite database.
4. **Schema Layer** – Pydantic models (schemas) define request/response payloads and validation.

All layers are loosely coupled via clear Python interfaces, making the codebase easy to test and extend.

## Component Diagram

```mermaid
flowchart TD
    subgraph API[API Layer]
        A1[router: /todos]
    end
    subgraph Service[Service / CRUD Layer]
        S1[crud.create_todo]
        S2[crud.get_todo]
        S3[crud.update_todo]
        S4[crud.delete_todo]
        S5[crud.list_todos]
    end
    subgraph Data[Data Access Layer]
        D1[SQLAlchemy models]
        D2[Database session]
    end
    subgraph Schema[Schema Layer]
        P1[TodoCreate]
        P2[TodoRead]
        P3[TodoUpdate]
    end

    A1 -->|calls| S1 & S2 & S3 & S4 & S5
    S1 -->|uses| D1 & D2
    S2 -->|uses| D1 & D2
    S3 -->|uses| D1 & D2
    S4 -->|uses| D1 & D2
    S5 -->|uses| D1 & D2
    A1 -->|accepts/returns| P1 & P2 & P3
```

## Technology Choices

| Layer | Technology | Reason |
|-------|------------|--------|
| **Web Framework** | **FastAPI** | High performance, automatic OpenAPI docs, async support. |
| **ORM** | **SQLAlchemy 2.0** | Mature, supports SQLite, declarative models. |
| **Data Validation** | **Pydantic (v2)** | FastAPI's native schema system. |
| **Database** | **SQLite** (file‑based) | Simple, zero‑config for development and CI. |
| **Containerisation** | **Docker** | Guarantees reproducible environment. |
| **CI** | **GitHub Actions** | Runs tests and coverage on each push/PR. |
| **Testing** | **pytest**, **coverage** | Widely used, easy to integrate. |

## Directory Layout

```
.
├─ app/                     # FastAPI application package
│  ├─ __init__.py
│  ├─ main.py               # Application entry point
│  ├─ models.py             # SQLAlchemy models
│  ├─ schemas.py            # Pydantic schemas
│  ├─ crud.py               # CRUD helper functions
│  ├─ database.py           # Engine & session handling
│  └─ routers/
│     ├─ __init__.py
│     └─ todo.py            # Todo router (endpoints)
├─ tests/                   # Test suite (to be implemented)
│  └─ test_todo.py
├─ Dockerfile               # Docker image definition
├─ docker-compose.yml       # Compose file for local dev
├─ requirements.txt         # Python dependencies
├─ docs/architecture.md    # This document
└─ README.md                # Project overview
```

---

*All modules contain `TODO` comments where implementation is required.  The backend developer will fill in the business logic, the frontend developer will add a UI placeholder, and the QA tester will write comprehensive tests.*