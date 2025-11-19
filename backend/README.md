# Backend - Task Management API

Python Flask REST API for the Task Management application.

## 🚀 Quick Start

### Using Make (Recommended)

```bash
# Show all available commands
make help

# Initialize development environment
make init

# Install dependencies
make install-dev

# Run the application
make run

# Run in development mode
make dev
```

### Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

## 🧪 Testing

```bash
# Run tests
make test

# Run tests with coverage
make test-cov

# View coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

## 🔍 Code Quality

### Linting

```bash
# Run all linting checks
make lint

# Or run individual checks
flake8 src/ tests/
pylint src/
mypy src/
```

### Formatting

```bash
# Auto-format code
make format

# Or run individual formatters
black src/ tests/
isort src/ tests/
```

### Security

```bash
# Run security checks
make security
```

### Pre-commit Check

```bash
# Run format, lint, and test (before committing)
make check
```

## 📋 Available Make Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install production dependencies |
| `make install-dev` | Install all dependencies including dev tools |
| `make test` | Run tests |
| `make test-cov` | Run tests with coverage |
| `make lint` | Run all linting checks |
| `make format` | Auto-format code |
| `make security` | Run security checks |
| `make check` | Run format, lint, and test |
| `make clean` | Remove cache and build artifacts |
| `make run` | Run the Flask application |
| `make dev` | Run in debug mode |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |
| `make venv` | Create virtual environment |
| `make init` | Initialize development environment |

## 📚 API Endpoints

### Health Check
```bash
GET /health
```

### Tasks
```bash
GET    /api/v1/tasks           # Get all tasks
GET    /api/v1/tasks/:id       # Get specific task
POST   /api/v1/tasks           # Create new task
PUT    /api/v1/tasks/:id       # Update task
DELETE /api/v1/tasks/:id       # Delete task
GET    /api/v1/tasks/stats     # Get statistics
```

### Example Requests

**Create Task:**
```bash
curl -X POST http://localhost:5000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project",
    "description": "Finish the task management app",
    "priority": "high"
  }'
```

**Get All Tasks:**
```bash
curl http://localhost:5000/api/v1/tasks
```

**Update Task Status:**
```bash
curl -X PUT http://localhost:5000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

**Delete Task:**
```bash
curl -X DELETE http://localhost:5000/api/v1/tasks/1
```

**Get Statistics:**
```bash
curl http://localhost:5000/api/v1/tasks/stats
```

## 🗂️ Project Structure

```
backend/
├── src/
│   ├── app.py          # Main Flask application
│   ├── config.py       # Configuration settings
│   └── utils.py        # Utility functions
├── tests/
│   ├── conftest.py     # Pytest configuration
│   ├── test_app.py     # API tests
│   └── test_utils.py   # Utility tests
├── .flake8             # Flake8 configuration
├── pyproject.toml      # Python project configuration
├── mypy.ini            # MyPy type checking configuration
├── Makefile            # Make commands
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── lint.sh             # Linting script
├── format.sh           # Formatting script
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```bash
DEBUG=False
ENVIRONMENT=production
PORT=5000
SECRET_KEY=your-secret-key-here
```

### Linting Configuration

- **Flake8**: `.flake8`
- **Black**: `pyproject.toml`
- **isort**: `pyproject.toml`
- **Pylint**: `pyproject.toml`
- **MyPy**: `mypy.ini`

## 🐳 Docker

```bash
# Build image
make docker-build

# Run container
make docker-run

# Or use docker-compose from project root
docker-compose up backend
```

## 📦 Dependencies

### Production
- Flask 3.0.0 - Web framework
- flask-cors 4.0.0 - CORS support
- gunicorn 21.2.0 - WSGI HTTP server
- python-dotenv 1.0.0 - Environment variables

### Development
- pytest 7.4.3 - Testing framework
- pytest-cov 4.1.0 - Coverage plugin
- flake8 6.1.0 - Style guide enforcement
- black 23.12.1 - Code formatter
- isort 5.13.2 - Import sorter
- pylint 3.0.3 - Code analysis
- mypy 1.7.1 - Type checking
- bandit 1.7.6 - Security linting

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run `make check` to verify
4. Commit and push
5. Create a pull request

## 📄 License

MIT License
