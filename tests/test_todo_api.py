import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_read_update_delete_todo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a todo
        create_resp = await ac.post("/todos/", json={"title": "Test Todo", "description": "Test description"})
        assert create_resp.status_code == 201
        todo = create_resp.json()
        assert todo["title"] == "Test Todo"
        todo_id = todo["id"]

        # Read the created todo
        read_resp = await ac.get(f"/todos/{todo_id}")
        assert read_resp.status_code == 200
        read_todo = read_resp.json()
        assert read_todo["id"] == todo_id
        assert read_todo["completed"] is False

        # Update the todo
        update_resp = await ac.put(f"/todos/{todo_id}", json={"completed": True})
        assert update_resp.status_code == 200
        updated = update_resp.json()
        assert updated["completed"] is True

        # Delete the todo
        delete_resp = await ac.delete(f"/todos/{todo_id}")
        assert delete_resp.status_code == 204

        # Verify deletion
        get_resp = await ac.get(f"/todos/{todo_id}")
        assert get_resp.status_code == 404
