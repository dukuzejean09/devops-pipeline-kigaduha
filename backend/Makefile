.PHONY: help install install-dev test test-cov lint format clean run dev check security

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt

install-dev:  ## Install all dependencies including dev tools
	pip install -r requirements.txt
	pip install black isort pylint mypy bandit autopep8

test:  ## Run tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage report
	pytest tests/ --cov=src --cov-report=term-missing --cov-report=html --cov-report=xml -v

lint:  ## Run all linting checks
	@echo "🔍 Running linting checks..."
	@echo ""
	@echo "📝 Checking code formatting with Black..."
	@black src/ tests/ --check --diff
	@echo ""
	@echo "📦 Checking import sorting with isort..."
	@isort src/ tests/ --check-only --diff
	@echo ""
	@echo "📋 Running flake8..."
	@flake8 src/ tests/
	@echo ""
	@echo "🔬 Running pylint..."
	@pylint src/ --rcfile=pyproject.toml || true
	@echo ""
	@echo "🔎 Running mypy..."
	@mypy src/ --config-file=mypy.ini || true
	@echo ""
	@echo "✅ Linting complete!"

format:  ## Auto-format code with Black and isort
	@echo "🔧 Auto-formatting code..."
	isort src/ tests/
	black src/ tests/
	@echo "✅ Formatting complete!"

security:  ## Run security checks with bandit
	@echo "🔒 Running security checks..."
	bandit -r src/ -ll
	@echo "✅ Security check complete!"

check: format lint test  ## Run format, lint, and test (pre-commit check)

clean:  ## Remove cache and build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build dist .coverage coverage.xml
	@echo "✅ Cleaned up!"

run:  ## Run the Flask application
	python src/app.py

dev:  ## Run the Flask application in debug mode
	FLASK_ENV=development FLASK_APP=src/app.py DEBUG=True python src/app.py

docker-build:  ## Build Docker image
	docker build -t task-management-backend .

docker-run:  ## Run Docker container
	docker run -p 5000:5000 task-management-backend

docker-test:  ## Run tests in Docker container
	docker run --rm task-management-backend pytest tests/

venv:  ## Create virtual environment
	python3 -m venv venv
	@echo "Virtual environment created. Activate with: source venv/bin/activate"

requirements:  ## Generate requirements.txt from installed packages
	pip freeze > requirements.txt

upgrade:  ## Upgrade all dependencies
	pip install --upgrade -r requirements.txt

init: venv install-dev  ## Initialize development environment
	@echo "✅ Development environment ready!"
	@echo "Activate virtual environment: source venv/bin/activate"
