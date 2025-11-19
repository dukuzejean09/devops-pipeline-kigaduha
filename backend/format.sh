#!/bin/bash
# Backend Auto-fix Script

set -e

echo "🔧 Auto-fixing Python code formatting..."
echo ""

# Change to backend directory
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run isort to fix imports
echo "📦 Fixing import sorting with isort..."
isort src/ tests/
echo "✅ Import sorting completed"
echo ""

# Run Black to format code
echo "📝 Formatting code with Black..."
black src/ tests/
echo "✅ Code formatting completed"
echo ""

echo "✅ Auto-fix completed! Now run './lint.sh' to verify."
