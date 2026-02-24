# app/main.py
"""FastAPI application entry point.

Creates the FastAPI app instance, includes routers, and configures any
middleware or event handlers. Also serves the minimal frontend UI.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from .routers import todo

app = FastAPI(title="Todo API", version="0.1.0")

# Include the Todo router
app.include_router(todo.router)

# Serve static assets (CSS, JS) from the frontend directory
frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve the index.html at the root path
@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse(frontend_path / "index.html")
