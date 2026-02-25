// Simple Todo frontend interacting with FastAPI backend
// Assumes backend is reachable at http://localhost:8000

const API_URL = 'http://localhost:8000/todos';

// Helper to handle fetch responses
async function handleResponse(response) {
    if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || response.statusText);
    }
    return response.json();
}

// Fetch all todos and render them
async function loadTodos() {
    const todos = await fetch(API_URL).then(handleResponse);
    const list = document.getElementById('todo-list');
    list.innerHTML = '';
    todos.forEach(renderTodo);
}

function renderTodo(todo) {
    const li = document.createElement('li');
    li.dataset.id = todo.id;
    li.textContent = `${todo.title} - ${todo.description || ''}`;
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = todo.completed;
    checkbox.addEventListener('change', () => toggleComplete(todo.id, checkbox.checked));
    li.prepend(checkbox);
    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.addEventListener('click', () => deleteTodo(todo.id));
    li.appendChild(delBtn);
    document.getElementById('todo-list').appendChild(li);
}

async function createTodo(event) {
    event.preventDefault();
    const title = document.getElementById('title').value.trim();
    const description = document.getElementById('description').value.trim();
    const completed = document.getElementById('completed').checked;
    if (!title) return alert('Title is required');
    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description, completed })
    }).then(handleResponse);
    document.getElementById('create-form').reset();
    loadTodos();
}

async function toggleComplete(id, completed) {
    await fetch(`${API_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed })
    }).then(handleResponse);
    loadTodos();
}

async function deleteTodo(id) {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' }).then(r => {
        if (!r.ok) throw new Error('Delete failed');
    });
    loadTodos();
}

// Attach form handler
document.getElementById('create-form').addEventListener('submit', createTodo);

// Initial load
loadTodos();
