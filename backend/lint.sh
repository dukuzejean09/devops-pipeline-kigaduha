#!/bin/bash
# Backend Linting Script

set -e

echo "🔍 Running Python linting and code quality checks..."
echo ""

# Change to backend directory
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run Black (Code Formatter)
echo "📝 Running Black (code formatter)..."
black src/ tests/ --check --diff || {
    echo "❌ Black formatting issues found. Run 'black src/ tests/' to fix."
    exit 1
}
echo "✅ Black formatting check passed"
echo ""

# Run isort (Import Sorter)
echo "📦 Running isort (import sorter)..."
isort src/ tests/ --check-only --diff || {
    echo "❌ Import sorting issues found. Run 'isort src/ tests/' to fix."
    exit 1
}
echo "✅ isort check passed"
echo ""

# Run flake8 (Style Guide Enforcement)
echo "📋 Running flake8 (style guide)..."
flake8 src/ tests/ || {
    echo "❌ Flake8 style violations found."
    exit 1
}
echo "✅ Flake8 check passed"
echo ""

# Run pylint (Code Analysis)
echo "🔬 Running pylint (code analysis)..."
pylint src/ --rcfile=pyproject.toml || {
    echo "⚠️  Pylint warnings found (non-blocking)"
}
echo ""

# Run mypy (Type Checking)
echo "🔎 Running mypy (type checking)..."
mypy src/ --config-file=mypy.ini || {
    echo "⚠️  Type checking warnings found (non-blocking)"
}
echo ""

# Run bandit (Security Linting)
echo "🔒 Running bandit (security linting)..."
bandit -r src/ -ll || {
    echo "⚠️  Security warnings found (non-blocking)"
}
echo ""

echo "✅ All critical linting checks passed!"
