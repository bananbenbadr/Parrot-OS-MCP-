#!/bin/bash

# Complete MCP Setup Script for Cursor
# This script sets up all MCP servers for Cursor IDE

set -e

echo "🚀 Setting up Complete MCP Configuration for Cursor"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    print_error "Node.js is not installed. Please install Node.js first."
    print_info "Visit: https://nodejs.org/"
    exit 1
fi

print_status "Node.js found: $(node --version)"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    print_error "npm is not installed. Please install npm first."
    exit 1
fi

print_status "npm found: $(npm --version)"

# Create credentials directory
mkdir -p ~/.credentials
print_status "Created credentials directory: ~/.credentials"

# Install MCP servers globally
print_info "Installing MCP servers..."

# Core servers (no API keys required)
print_info "Installing core MCP servers..."
npx -y @modelcontextprotocol/server-filesystem --version
npx -y @modelcontextprotocol/server-git --version
npx -y @modelcontextprotocol/server-memory --version
npx -y @modelcontextprotocol/server-fetch --version
npx -y @modelcontextprotocol/server-time --version

# Optional servers (require API keys)
print_warning "Optional servers require API keys. You can install them later:"
echo "  - Brave Search: npx -y @modelcontextprotocol/server-brave-search"
echo "  - Everart: npx -y @modelcontextprotocol/server-everart"
echo "  - Google Drive: npx -y @modelcontextprotocol/server-gdrive"
echo "  - GitHub: npx -y @modelcontextprotocol/server-github"
echo "  - Slack: npx -y @modelcontextprotocol/server-slack"
echo "  - Weather: npx -y @modelcontextprotocol/server-weather"
echo "  - Puppeteer: npx -y @modelcontextprotocol/server-puppeteer"
echo "  - SQLite: npx -y @modelcontextprotocol/server-sqlite"
echo "  - PostgreSQL: npx -y @modelcontextprotocol/server-postgres"

# Verify Cursor MCP configuration
if [ -f ~/.cursor/mcp.json ]; then
    print_status "Cursor MCP configuration found"
    print_info "Configuration location: ~/.cursor/mcp.json"
else
    print_warning "Cursor MCP configuration not found"
    print_info "Make sure Cursor is installed and the configuration file exists"
fi

# Test Parrot OS MCP server
print_info "Testing Parrot OS MCP server..."
cd "/home/ben/Documents/parrot mcp"
if [ -f "venv/bin/python" ]; then
    source venv/bin/activate
    python -c "import mcp; print('MCP module available')" 2>/dev/null && print_status "Parrot OS MCP server ready" || print_error "Parrot OS MCP server not ready"
else
    print_error "Parrot OS MCP server virtual environment not found"
fi

echo ""
echo "🎉 MCP Setup Complete!"
echo "====================="
echo ""
print_info "Next steps:"
echo "1. Restart Cursor IDE to load the new MCP configuration"
echo "2. Configure API keys for optional services (see ~/.cursor/mcp.json)"
echo "3. Test MCP servers in Cursor by asking me to use them"
echo ""
print_info "Available MCP servers:"
echo "  • parrot-os: Parrot OS security tools and system management"
echo "  • filesystem: File system operations"
echo "  • git: Git repository management"
echo "  • memory: Persistent memory storage"
echo "  • fetch: HTTP requests and web scraping"
echo "  • time: Date and time utilities"
echo "  • [Optional] brave-search, everart, gdrive, github, slack, weather, puppeteer, sqlite, postgres"
echo ""
print_warning "Remember to configure API keys for services that require them!"
