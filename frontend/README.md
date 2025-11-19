# Frontend - Task Management App

React application for the Task Management system.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build
```

## 📜 Available Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Start development server (port 3000) |
| `npm run build` | Build production bundle |
| `npm test` | Run tests (single run) |
| `npm run test:watch` | Run tests in watch mode |
| `npm run test:coverage` | Run tests with coverage report |
| `npm run lint` | Check code for linting errors |
| `npm run lint:fix` | Auto-fix linting errors |
| `npm run format` | Format code with Prettier |
| `npm run format:check` | Check code formatting |
| `npm run check` | Run lint, format check, and tests |

## 🧪 Testing

### Run Tests
```bash
# Single run
npm test

# Watch mode
npm run test:watch

# With coverage
npm run test:coverage
```

### View Coverage Report
```bash
# After running test:coverage
open coverage/lcov-report/index.html  # macOS
xdg-open coverage/lcov-report/index.html  # Linux
```

## 🔍 Code Quality

### Linting
```bash
# Check for errors
npm run lint

# Auto-fix errors
npm run lint:fix
```

### Formatting
```bash
# Format all files
npm run format

# Check formatting
npm run format:check
```

### Pre-commit Check
```bash
# Run all checks before committing
npm run check
```

## ⚙️ Configuration Files

- **`.eslintrc.json`** - ESLint configuration
- **`.prettierrc`** - Prettier configuration
- **`.eslintignore`** - Files to ignore for linting
- **`.prettierignore`** - Files to ignore for formatting

## 🗂️ Project Structure

```
frontend/
├── public/
│   └── index.html        # HTML template
├── src/
│   ├── App.js           # Main application component
│   ├── App.css          # Application styles
│   ├── App.test.js      # Application tests
│   ├── index.js         # Entry point
│   └── index.css        # Global styles
├── .eslintrc.json       # ESLint config
├── .prettierrc          # Prettier config
├── .env                 # Environment variables
├── package.json         # Dependencies and scripts
└── README.md           # This file
```

## 🌐 Environment Variables

Create a `.env` file:

```bash
REACT_APP_API_URL=http://localhost:5000
```

Available variables:
- `REACT_APP_API_URL` - Backend API URL

## 🎨 Features

- ✅ Task creation and management
- 📊 Real-time statistics dashboard
- 🎯 Priority levels (High, Medium, Low)
- 🔄 Status tracking (Pending, In Progress, Completed)
- 🎨 Modern, gradient UI design
- 📱 Fully responsive layout
- 🔍 Task filtering by status

## 🐳 Docker

### Build Image
```bash
docker build -t task-management-frontend .
```

### Run Container
```bash
docker run -p 80:80 task-management-frontend
```

### Using Docker Compose
```bash
# From project root
docker-compose up frontend
```

## 📦 Dependencies

### Production
- **react** (^18.2.0) - UI framework
- **react-dom** (^18.2.0) - React DOM bindings
- **react-scripts** (5.0.1) - Build scripts
- **web-vitals** (^3.5.0) - Performance metrics

### Development
- **@testing-library/react** - React testing utilities
- **@testing-library/jest-dom** - Jest DOM matchers
- **@testing-library/user-event** - User interaction simulation
- **eslint** - JavaScript linter
- **prettier** - Code formatter

## 🔧 ESLint Rules

Key rules configured:
- ✅ React Hooks validation
- ✅ No console warnings
- ✅ No unused variables
- ✅ Prefer const over let
- ✅ No var declarations
- ✅ Strict equality checks
- ✅ Semicolon enforcement

## 💅 Code Style

- **Indentation**: 2 spaces
- **Quotes**: Single quotes for JS, double for JSX
- **Semicolons**: Required
- **Line Length**: 100 characters
- **Trailing Commas**: ES5 style

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run `npm run check` to verify
4. Commit and push
5. Create a pull request

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### Node Modules Issues
```bash
# Clean install
rm -rf node_modules package-lock.json
npm install
```

### Build Errors
```bash
# Clear cache
npm run build -- --reset-cache
```

## 📄 License

MIT License
