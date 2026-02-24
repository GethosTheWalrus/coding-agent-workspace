# Todo API

A simple **Todo** REST API built with **FastAPI**, **SQLModel**, and **SQLite**.

## Features
- Create, read, update, and delete todo items.
- Automatic interactive documentation via Swagger UI (`/docs`).
- SQLite database stored in a local file (`todo.db`).

## Technology Stack
- **FastAPI** – High‑performance web framework.
- **Uvicorn** – ASGI server.
- **SQLModel** – ORM built on top of SQLAlchemy & Pydantic.
- **SQLite** – Lightweight file‑based relational database.

## Project Structure
```
.
├── app/                # Application package
│   ├── __init__.py
│   ├── main.py         # FastAPI entry point
│   ├── database.py    # DB engine & session handling
│   ├── models.py      # SQLModel definitions
│   └── routers/
│       ├── __init__.py
│       └── todo.py    # CRUD endpoints
├── requirements.txt   # Python dependencies
├── README.md          # This file
└── docs/
    └── architecture.md
```

## Setup & Run
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd <repo-dir>
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

5. **Explore the API docs**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the automatically generated Swagger UI where you can test all endpoints.

## API Endpoints
| Method | Path | Description |
|--------|------|-------------|
| `GET`    | `/todos/` | List all todos |
| `GET`    | `/todos/{todo_id}` | Retrieve a single todo |
| `POST`   | `/todos/` | Create a new todo |
| `PUT`    | `/todos/{todo_id}` | Update an existing todo |
| `DELETE` | `/todos/{todo_id}` | Delete a todo |

## Future Enhancements
- Add authentication (OAuth2/JWT).
- Implement pagination and filtering.
- Containerize the application with Docker.
- CI/CD pipeline with GitHub Actions.
