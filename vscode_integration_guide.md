# VS Code MCP Server Integration Guide

## ✅ Installation Complete

The Parrot OS MCP server has been successfully installed and configured for VS Code.

## 📋 Configuration Details

### MCP Server Configuration
**File**: `~/.config/Code/User/mcp.json`

```json
{
    "servers": {
        "microsoft/markitdown": {
            "type": "stdio",
            "command": "uvx",
            "args": [
                "markitdown-mcp==0.0.1a4"
            ],
            "gallery": "https://api.mcp.github.com/v0/servers/976a2f68-e16c-4e2b-9709-7133487f8c14",
            "version": "1.0.0"
        },
        "parrot-os-server": {
            "type": "stdio",
            "command": "/home/ben/Documents/parrot mcp/.venv/bin/python",
            "args": [
                "/home/ben/Documents/parrot mcp/main.py"
            ],
            "env": {
                "PYTHONPATH": "/home/ben/Documents/parrot mcp"
            },
            "version": "1.0.0",
            "description": "Parrot OS MCP Server for security operations and system management"
        }
    },
    "inputs": []
}
```

## 🚀 How to Use in VS Code

### 1. Restart VS Code
After updating the MCP configuration, restart VS Code to load the new server.

### 2. Access MCP Tools
Once VS Code restarts:
1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Type "MCP" to see available MCP commands
3. Use the Parrot OS tools through the MCP interface

### 3. Available Tools
The Parrot OS MCP server provides these tools:
- **run_command** - Execute shell commands on Parrot OS
- **get_system_info** - Get detailed system information
- **list_directory** - List directory contents
- **read_file** - Read file contents
- **write_file** - Write to files
- **copy_file** - Copy files/directories
- **delete_path** - Delete files/directories

## 🔧 Testing

The integration has been tested and verified:
- ✅ Configuration file correctly formatted
- ✅ Python path and script paths are correct
- ✅ MCP server starts successfully
- ✅ Environment variables properly set
- ✅ Server responds to connections

## 📊 Server Capabilities

The Parrot OS MCP server can:
- Execute any shell command on Parrot OS
- Access and manage files
- Gather system information
- Interact with security tools
- Provide real-time system diagnostics

## 🎯 Usage Examples

### Through VS Code MCP Interface:
1. Use Command Palette MCP commands
2. Access through AI assistants (Claude, Copilot, etc.)
3. Use via chat interfaces that support MCP

### Direct Tool Examples:
- Execute security scans
- Manage files and directories
- Gather system intelligence
- Automate security operations

## ⚠️ Troubleshooting

### If the server doesn't start:
1. Check that the Python virtual environment exists
2. Verify all dependencies are installed: `pip install mcp[cli]`
3. Ensure file paths are correct in `mcp.json`

### If tools aren't available:
1. Restart VS Code
2. Check VS Code's MCP server logs
3. Verify the server is running in terminal

## 🔄 Updating

To update the MCP server:
1. Update the code in `/home/ben/Documents/parrot mcp/`
2. Restart VS Code to reload the server
3. No need to modify `mcp.json` unless paths change

## 📝 Notes

- The server uses stdio transport for maximum compatibility
- All tools run with the same permissions as the user
- Error handling is built into each tool
- The server is designed for security operations on Parrot OS

Your Parrot OS MCP server is now ready for use in VS Code! 🎉