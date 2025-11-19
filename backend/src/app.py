import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
app.config["DEBUG"] = os.getenv("DEBUG", "False") == "True"
app.config["ENV"] = os.getenv("ENVIRONMENT", "production")

# In-memory task storage (replace with database in production)
tasks = [
    {
        "id": 1,
        "title": "Welcome to Task Manager",
        "description": "This is your first task. Click to mark it as complete!",
        "status": "pending",
        "priority": "medium",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
]
next_id = 2


@app.route("/")
def index():
    """Root endpoint"""
    return jsonify(
        {
            "message": "Task Management API",
            "status": "running",
            "version": "1.0.0",
            "endpoints": {
                "health": "/health",
                "tasks": "/api/v1/tasks",
                "create_task": "POST /api/v1/tasks",
                "get_task": "GET /api/v1/tasks/<id>",
                "update_task": "PUT /api/v1/tasks/<id>",
                "delete_task": "DELETE /api/v1/tasks/<id>",
            },
        }
    )


@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "task-management-api", "tasks_count": len(tasks)}), 200


@app.route("/api/v1/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks"""
    status_filter = request.args.get("status")
    priority_filter = request.args.get("priority")

    filtered_tasks = tasks

    if status_filter:
        filtered_tasks = [t for t in filtered_tasks if t["status"] == status_filter]

    if priority_filter:
        filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority_filter]

    return jsonify({"tasks": filtered_tasks, "total": len(filtered_tasks)}), 200


@app.route("/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a specific task"""
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@app.route("/api/v1/tasks", methods=["POST"])
def create_task():
    """Create a new task"""
    global next_id

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "status": data.get("status", "pending"),
        "priority": data.get("priority", "medium"),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task), 201


@app.route("/api/v1/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task"""
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    if "title" in data:
        task["title"] = data["title"]
    if "description" in data:
        task["description"] = data["description"]
    if "status" in data:
        task["status"] = data["status"]
    if "priority" in data:
        task["priority"] = data["priority"]

    task["updated_at"] = datetime.now().isoformat()

    return jsonify(task), 200


@app.route("/api/v1/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task"""
    global tasks

    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({"message": "Task deleted successfully"}), 200


@app.route("/api/v1/tasks/stats", methods=["GET"])
def get_stats():
    """Get task statistics"""
    total = len(tasks)
    pending = len([t for t in tasks if t["status"] == "pending"])
    in_progress = len([t for t in tasks if t["status"] == "in-progress"])
    completed = len([t for t in tasks if t["status"] == "completed"])

    return (
        jsonify(
            {
                "total": total,
                "pending": pending,
                "in_progress": in_progress,
                "completed": completed,
                "by_priority": {
                    "high": len([t for t in tasks if t["priority"] == "high"]),
                    "medium": len([t for t in tasks if t["priority"] == "medium"]),
                    "low": len([t for t in tasks if t["priority"] == "low"]),
                },
            }
        ),
        200,
    )


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
