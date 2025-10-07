#!/bin/bash
# Parrot OS MCP Server - Cursor IDE Setup Script

echo "🔧 Setting up Cursor IDE MCP integration for Parrot OS"
echo "===================================================="

# Create Cursor configuration directory
mkdir -p ~/.cursor

echo "📁 Created Cursor configuration directory: ~/.cursor"

# Create MCP configuration file
cat > ~/.cursor/mcp.json << 'EOF'
{
  "mcp": {
    "servers": {
      "parrot-os": {
        "command": "/home/ben/Documents/parrot mcp/.venv/bin/python",
        "args": [
          "/home/ben/Documents/parrot mcp/main.py"
        ],
        "env": {
          "PYTHONPATH": "/home/ben/Documents/parrot mcp"
        }
      }
    }
  }
}
EOF

echo "📄 Created MCP configuration: ~/.cursor/mcp.json"

# Verify the configuration
echo "🔍 Verifying configuration..."
if [ -f ~/.cursor/mcp.json ]; then
    echo "✅ Configuration file created successfully"
    echo "📋 Configuration preview:"
    cat ~/.cursor/mcp.json
else
    echo "❌ Failed to create configuration file"
    exit 1
fi

# Test MCP server functionality
echo ""
echo "🧪 Testing MCP server functionality..."
cd "/home/ben/Documents/parrot mcp"

if [ -f .venv/bin/activate ]; then
    source .venv/bin/activate
    echo "✅ Virtual environment activated"
    
    # Test basic functionality
    if python test_server.py > /dev/null 2>&1; then
        echo "✅ MCP server test passed"
    else
        echo "❌ MCP server test failed"
        echo "Running detailed test..."
        python test_server.py
        exit 1
    fi
else
    echo "❌ Virtual environment not found"
    echo "Please run: python3 -m venv .venv && source .venv/bin/activate && pip install mcp[cli]"
    exit 1
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Restart Cursor IDE"
echo "2. Use MCP tools with @ commands (e.g., @get_system_info)"
echo "3. Check Cursor's MCP output: View → Output → MCP"
echo ""
echo "Available tools:"
echo "- @run_command - Execute shell commands"
echo "- @get_system_info - Get system information"
echo "- @list_directory - Browse files"
echo "- @read_file / @write_file - File operations"
echo ""
echo "For security operations:"
echo "@run_command {\"command\": \"nmap -sS target.com\"}"
echo "@run_command {\"command\": \"sqlmap --help\"}"
echo "@run_command {\"command\": \"msfconsole --version\"}"