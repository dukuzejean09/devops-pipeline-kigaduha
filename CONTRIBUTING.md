# Contributing to DevOps Pipeline Task Manager

Thank you for your interest in contributing to our project! This document provides guidelines and instructions for contributing.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Branch Strategy](#branch-strategy)

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 20+
- Docker and Docker Compose
- Git

### Setup Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/dukuzejean09/devops-pipeline-kigaduha.git
   cd devops-pipeline-kigaduha
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

4. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## Development Workflow

### 1. Create a Feature Branch
Always create a new branch from `develop`:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Branch Naming Conventions
- `feature/` - New features (e.g., `feature/add-user-authentication`)
- `bugfix/` - Bug fixes (e.g., `bugfix/fix-login-error`)
- `hotfix/` - Critical production fixes (e.g., `hotfix/security-patch`)
- `docs/` - Documentation updates (e.g., `docs/update-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/optimize-queries`)

### 2. Make Your Changes
- Write clean, readable code
- Follow the code standards (see below)
- Add tests for new features
- Update documentation as needed

### 3. Commit Your Changes
Use meaningful commit messages:
```bash
git add .
git commit -m "feat: add user authentication endpoint"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## Code Standards

### Backend (Python)

#### Linting and Formatting
Run before committing:
```bash
cd backend
make format    # Format with black and isort
make lint      # Check with flake8, pylint, mypy
make check     # Run all checks
```

#### Style Guidelines
- Follow PEP 8
- Maximum line length: 120 characters
- Use type hints for function parameters and return values
- Document functions with docstrings

**Example:**
```python
def create_task(title: str, description: str, priority: str = "medium") -> dict:
    """
    Create a new task with the given parameters.
    
    Args:
        title: The task title
        description: Detailed description of the task
        priority: Task priority level (low, medium, high)
    
    Returns:
        Dictionary containing the created task
    """
    # Implementation
    pass
```

### Frontend (React)

#### Linting and Formatting
Run before committing:
```bash
cd frontend
npm run format      # Format with Prettier
npm run lint        # Check with ESLint
npm run check       # Run all checks
```

#### Style Guidelines
- Use functional components with hooks
- Follow Airbnb React style guide
- Use meaningful variable and function names
- Keep components small and focused

**Example:**
```javascript
const TaskCard = ({ task, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  
  const handleSubmit = async (updatedTask) => {
    await onUpdate(task.id, updatedTask);
    setIsEditing(false);
  };
  
  return (
    // JSX implementation
  );
};
```

## Testing Guidelines

### Backend Testing
```bash
cd backend
make test              # Run all tests
make test-coverage     # Run with coverage report
```

- Write tests for all new features
- Aim for >80% code coverage
- Use pytest fixtures for reusable test data
- Test both success and error cases

**Example:**
```python
def test_create_task(client):
    """Test task creation endpoint."""
    response = client.post('/api/v1/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description',
        'priority': 'high'
    })
    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'
```

### Frontend Testing
```bash
cd frontend
npm test               # Run all tests
npm run test:coverage  # Run with coverage
```

- Test user interactions
- Test component rendering
- Test API integration
- Use React Testing Library

**Example:**
```javascript
test('creates new task when form is submitted', async () => {
  render(<App />);
  
  const titleInput = screen.getByPlaceholderText('Task title');
  fireEvent.change(titleInput, { target: { value: 'New Task' } });
  
  const submitButton = screen.getByText('Create Task');
  fireEvent.click(submitButton);
  
  await waitFor(() => {
    expect(screen.getByText('New Task')).toBeInTheDocument();
  });
});
```

## Pull Request Process

### Before Creating a PR

1. **Update your branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout your-feature-branch
   git rebase develop
   ```

2. **Run all checks**
   ```bash
   # Backend
   cd backend && make check
   
   # Frontend
   cd frontend && npm run check
   ```

3. **Ensure tests pass**
   ```bash
   # Backend
   cd backend && make test
   
   # Frontend
   cd frontend && npm test
   ```

4. **Build Docker images**
   ```bash
   docker-compose build
   ```

### Creating the PR

1. Push your branch:
   ```bash
   git push origin your-feature-branch
   ```

2. Go to GitHub and create a Pull Request
3. Fill out the PR template completely
4. Request reviews from at least 2 team members
5. Link any related issues

### PR Requirements

- ✅ All CI checks must pass
- ✅ At least 2 approving reviews required
- ✅ No unresolved conversations
- ✅ Code coverage should not decrease
- ✅ Documentation updated if needed
- ✅ Commit messages follow conventions

### Code Review Guidelines

**For Authors:**
- Respond to all comments
- Make requested changes promptly
- Re-request review after updates
- Keep PRs focused and reasonably sized

**For Reviewers:**
- Review within 24 hours if possible
- Be constructive and specific
- Test the changes locally if needed
- Approve only when confident in the changes

## Branch Strategy

### Main Branches
- `main` - Production-ready code
- `develop` - Integration branch for features

### Workflow
```
feature/xyz → develop → main
```

1. Create feature branch from `develop`
2. Submit PR to merge into `develop`
3. After testing, create PR from `develop` to `main`
4. `main` triggers deployment to production

### Protection Rules
- `main` and `develop` are protected
- Direct pushes not allowed
- PR approval required
- CI checks must pass

## Need Help?

- Check existing issues on GitHub
- Ask in team chat
- Review documentation in `/docs`
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the project's license.

---

Thank you for contributing! 🚀
