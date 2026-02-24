// Simple vanilla JS to interact with the FastAPI Todo API

const API_URL = '/todos'; // FastAPI will serve under this prefix

document.addEventListener('DOMContentLoaded', () => {
  loadTodos();
  const form = document.getElementById('new-todo-form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value.trim();
    const description = document.getElementById('description').value.trim();
    const completed = document.getElementById('completed').checked;
    if (!title) return;
    await createTodo({ title, description, completed });
    form.reset();
    loadTodos();
  });
});

async function loadTodos() {
  const resp = await fetch(API_URL);
  const todos = await resp.json();
  const list = document.getElementById('todo-list');
  list.innerHTML = '';
  todos.forEach(renderTodo);
}

function renderTodo(todo) {
  const li = document.createElement('li');
  li.dataset.id = todo.id;
  li.className = todo.completed ? 'completed' : '';
  li.innerHTML = `
    <span>
      <strong>${todo.title}</strong> - ${todo.description || ''}
    </span>
    <span>
      <button class="edit">Edit</button>
      <button class="delete">Delete</button>
    </span>
  `;
  // Delete handler
  li.querySelector('.delete').addEventListener('click', async () => {
    await fetch(`${API_URL}/${todo.id}`, { method: 'DELETE' });
    li.remove();
  });
  // Edit handler (simple toggle completed)
  li.querySelector('.edit').addEventListener('click', async () => {
    const newCompleted = !todo.completed;
    await fetch(`${API_URL}/${todo.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: newCompleted })
    });
    loadTodos();
  });
  document.getElementById('todo-list').appendChild(li);
}

async function createTodo(data) {
  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
}
