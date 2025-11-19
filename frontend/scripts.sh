#!/bin/bash
# Frontend Development Helper Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Change to frontend directory
cd "$(dirname "$0")"

# Function to display help
show_help() {
    echo -e "${BLUE}Frontend Task Management App - Helper Script${NC}"
    echo ""
    echo "Usage: ./scripts.sh [command]"
    echo ""
    echo "Available commands:"
    echo "  install      - Install dependencies"
    echo "  start        - Start development server"
    echo "  build        - Build for production"
    echo "  test         - Run tests"
    echo "  test:watch   - Run tests in watch mode"
    echo "  test:cov     - Run tests with coverage"
    echo "  lint         - Check for linting errors"
    echo "  lint:fix     - Fix linting errors"
    echo "  format       - Format code with Prettier"
    echo "  format:check - Check code formatting"
    echo "  check        - Run all checks (lint, format, test)"
    echo "  clean        - Clean build artifacts"
    echo "  help         - Show this help message"
    echo ""
}

# Function to run commands
case "$1" in
    install)
        echo -e "${BLUE}📦 Installing dependencies...${NC}"
        npm install
        echo -e "${GREEN}✅ Dependencies installed!${NC}"
        ;;
    start)
        echo -e "${BLUE}🚀 Starting development server...${NC}"
        npm start
        ;;
    build)
        echo -e "${BLUE}🔨 Building for production...${NC}"
        npm run build
        echo -e "${GREEN}✅ Build complete!${NC}"
        ;;
    test)
        echo -e "${BLUE}🧪 Running tests...${NC}"
        npm test
        ;;
    test:watch)
        echo -e "${BLUE}🧪 Running tests in watch mode...${NC}"
        npm run test:watch
        ;;
    test:cov)
        echo -e "${BLUE}🧪 Running tests with coverage...${NC}"
        npm run test:coverage
        ;;
    lint)
        echo -e "${BLUE}🔍 Checking for linting errors...${NC}"
        npm run lint
        echo -e "${GREEN}✅ Linting complete!${NC}"
        ;;
    lint:fix)
        echo -e "${BLUE}🔧 Fixing linting errors...${NC}"
        npm run lint:fix
        echo -e "${GREEN}✅ Linting fixes applied!${NC}"
        ;;
    format)
        echo -e "${BLUE}💅 Formatting code...${NC}"
        npm run format
        echo -e "${GREEN}✅ Code formatted!${NC}"
        ;;
    format:check)
        echo -e "${BLUE}💅 Checking code formatting...${NC}"
        npm run format:check
        echo -e "${GREEN}✅ Format check complete!${NC}"
        ;;
    check)
        echo -e "${BLUE}🔍 Running all checks...${NC}"
        echo ""
        echo -e "${YELLOW}Step 1/3: Linting...${NC}"
        npm run lint
        echo ""
        echo -e "${YELLOW}Step 2/3: Format check...${NC}"
        npm run format:check
        echo ""
        echo -e "${YELLOW}Step 3/3: Testing...${NC}"
        npm test
        echo ""
        echo -e "${GREEN}✅ All checks passed!${NC}"
        ;;
    clean)
        echo -e "${BLUE}🧹 Cleaning build artifacts...${NC}"
        rm -rf build
        rm -rf node_modules/.cache
        rm -rf coverage
        echo -e "${GREEN}✅ Clean complete!${NC}"
        ;;
    help|*)
        show_help
        ;;
esac
