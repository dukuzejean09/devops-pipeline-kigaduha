"""
Tests for the task management API
"""

import json

import pytest

from src.app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Task Management API"
    assert data["status"] == "running"


def test_health(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["service"] == "task-management-api"


def test_get_tasks(client):
    """Test getting all tasks"""
    response = client.get("/api/v1/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert "tasks" in data
    assert "total" in data


def test_create_task(client):
    """Test creating a new task"""
    task_data = {"title": "Test Task", "description": "This is a test task", "priority": "high"}
    response = client.post("/api/v1/tasks", data=json.dumps(task_data), content_type="application/json")
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test Task"
    assert data["priority"] == "high"


def test_create_task_without_title(client):
    """Test creating a task without title"""
    task_data = {"description": "This task has no title"}
    response = client.post("/api/v1/tasks", data=json.dumps(task_data), content_type="application/json")
    assert response.status_code == 400


def test_get_single_task(client):
    """Test getting a specific task"""
    response = client.get("/api/v1/tasks/1")
    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data
    assert "title" in data


def test_get_nonexistent_task(client):
    """Test getting a task that doesn't exist"""
    response = client.get("/api/v1/tasks/99999")
    assert response.status_code == 404


def test_update_task(client):
    """Test updating a task"""
    update_data = {"status": "completed"}
    response = client.put("/api/v1/tasks/1", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "completed"


def test_delete_task(client):
    """Test deleting a task"""
    # First create a task
    task_data = {"title": "Task to delete"}
    create_response = client.post("/api/v1/tasks", data=json.dumps(task_data), content_type="application/json")
    task_id = create_response.get_json()["id"]

    # Then delete it
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200

    # Verify it's deleted
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


def test_get_stats(client):
    """Test getting task statistics"""
    response = client.get("/api/v1/tasks/stats")
    assert response.status_code == 200
    data = response.get_json()
    assert "total" in data
    assert "pending" in data
    assert "in_progress" in data
    assert "completed" in data
    assert "by_priority" in data
