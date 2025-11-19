# 🚀 Quick Start Guide - Task Management App

## Option 1: Using Docker Compose (Easiest) ⭐

This is the fastest way to run the entire application:

```bash
# Clone the repository
git clone https://github.com/dukuzejean09/devops-pipeline-kigaduha.git
cd devops-pipeline-kigaduha

# Start both frontend and backend
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

**Access the app:**
- Frontend: http://localhost
- Backend API: http://localhost:5000
- API Health: http://localhost:5000/health

---

## Option 2: Run Without Docker

### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python src/app.py
```

Backend will run on: **http://localhost:5000**

### Frontend Setup (in a new terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run on: **http://localhost:3000**

---

## 📝 Using the Task Manager

### Creating Tasks
1. Enter task title (required)
2. Add description (optional)
3. Select priority level
4. Click "Add Task"

### Managing Tasks
- **Change Status**: Use dropdown to mark tasks as Pending, In Progress, or Completed
- **Delete Task**: Click the delete button (confirms before deleting)
- **Filter Tasks**: Use filter buttons to view tasks by status

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/tasks` | Get all tasks |
| GET | `/api/v1/tasks/:id` | Get specific task |
| POST | `/api/v1/tasks` | Create new task |
| PUT | `/api/v1/tasks/:id` | Update task |
| DELETE | `/api/v1/tasks/:id` | Delete task |
| GET | `/api/v1/tasks/stats` | Get statistics |

### Example API Usage

```bash
# Create a task
curl -X POST http://localhost:5000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Task details","priority":"high"}'

# Get all tasks
curl http://localhost:5000/api/v1/tasks

# Update task status
curl -X PUT http://localhost:5000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"completed"}'

# Delete a task
curl -X DELETE http://localhost:5000/api/v1/tasks/1
```

---

## 🧪 Running Tests

### Backend Tests
```bash
cd backend
pytest tests/ --cov=src
flake8 src/
```

### Frontend Tests
```bash
cd frontend
npm test
npm run lint
```

---

## 🐛 Troubleshooting

### Docker Compose Issues

**Problem:** Port already in use
```bash
# Find and stop conflicting services
docker ps
docker stop <container_id>

# Or use different ports by editing docker-compose.yml
```

**Problem:** Build fails
```bash
# Clean up and rebuild
docker-compose down -v
docker system prune -a
docker-compose up --build
```

### Frontend Can't Connect to Backend

**Fix:** Update API URL in frontend
```javascript
// In src/App.js, update:
const API_URL = 'http://localhost:5000';
```

### Backend Not Starting

**Check Python version:**
```bash
python --version  # Should be 3.11+
```

**Install missing dependencies:**
```bash
pip install -r requirements.txt
```

---

## 📦 Project Structure

```
.
├── frontend/               # React application
│   ├── src/
│   │   ├── App.js         # Main component with task logic
│   │   ├── App.css        # Styling
│   │   └── App.test.js    # Tests
│   ├── Dockerfile         # Frontend container
│   └── package.json
├── backend/               # Flask API
│   ├── src/
│   │   └── app.py        # Task management API
│   ├── tests/
│   │   └── test_app.py   # API tests
│   ├── Dockerfile        # Backend container
│   └── requirements.txt
├── docker-compose.yml     # Multi-container setup
└── README.md
```

---

## 🚀 Deployment

### Production Deployment with GitHub Actions

1. **Configure Secrets** in GitHub repository:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `SSH_PRIVATE_KEY`
   - `SERVER_HOST`

2. **Push to main branch** to trigger CI/CD:
```bash
git add .
git commit -m "Deploy task management app"
git push origin main
```

The GitHub Actions workflow will:
- Run tests
- Build Docker images
- Deploy to production
- Run health checks

### Manual Deployment with Ansible

```bash
cd ansible

# Update server IPs in inventory
vim inventory/hosts.ini

# Deploy application
ansible-playbook playbooks/deploy.yml
```

---

## 🎯 Next Steps

- [ ] Add user authentication
- [ ] Add database (PostgreSQL/MongoDB)
- [ ] Add task categories/tags
- [ ] Add due dates and reminders
- [ ] Add task sharing/collaboration
- [ ] Add dark mode
- [ ] Add export functionality (CSV/PDF)

---

## 📞 Support

For issues or questions:
- Create an issue: https://github.com/dukuzejean09/devops-pipeline-kigaduha/issues
- Email: support@yourcompany.com

---

**Happy Task Managing! 🎉**
