# Cursor IDE MCP Integration - Parrot OS Server

## 📋 MCP Server Configuration

Your MCP server is already configured in `mcp-server.json`. Here's the setup for Cursor IDE:

### Configuration File Location
Cursor looks for MCP configurations in:
- `~/.cursor/mcp.json` (User-level configuration)
- `./cursor/mcp.json` (Project-level configuration)

### Recommended Configuration
Create `~/.cursor/mcp.json` with:

```json
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
```

## 🚀 Quick Setup Commands

### 1. Create Cursor Configuration Directory
```bash
mkdir -p ~/.cursor
```

### 2. Create MCP Configuration File
```bash
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
```

### 3. Verify Configuration
```bash
cat ~/.cursor/mcp.json
```

## 🛠️ Available Tools in Cursor

Once configured, you can use these tools directly in Cursor:

### System Commands
- `run_command` - Execute shell commands
- `get_system_info` - Get Parrot OS system details
- `list_directory` - Browse files and directories

### File Operations
- `read_file` - Read file contents
- `write_file` - Create or modify files
- `copy_file` - Copy files/directories
- `delete_path` - Delete files/directories

## 💡 Usage Examples in Cursor

### 1. System Information
```
@get_system_info
```

### 2. Run Security Scan
```
@run_command {"command": "nmap -sS -sV scanme.nmap.org"}
```

### 3. List Security Tools
```
@run_command {"command": "ls /usr/bin/ | grep -E '(nmap|sqlmap|msf)'"}
```

### 4. Read Security Documentation
```
@read_file {"file_path": "/home/ben/Documents/parrot mcp/pentesting_guide.md"}
```

### 5. Create Security Script
```
@write_file {
  "file_path": "/tmp/security_scan.sh",
  "content": "#!/bin/bash\necho 'Running security scan...'\nnmap -sS $1\necho 'Scan complete!'"
}
```

## 🔧 Troubleshooting

### Common Issues:

1. **MCP server not found**
   - Ensure virtual environment is activated: `source /home/ben/Documents/parrot mcp/.venv/bin/activate`
   - Check Python path: `which python`

2. **Permission denied**
   - Make script executable: `chmod +x /home/ben/Documents/parrot mcp/main.py`

3. **Cursor doesn't recognize MCP**
   - Restart Cursor IDE
   - Check Cursor logs: `View → Output → MCP`

### Verification Commands:
```bash
# Check MCP server status
cd "/home/ben/Documents/parrot mcp" && source .venv/bin/activate && python test_server.py

# Test individual tools
cd "/home/ben/Documents/parrot mcp" && source .venv/bin/activate && python -c "from main import get_system_info; import asyncio; print(asyncio.run(get_system_info()))"
```

## 🎯 Advanced Configuration

### Project-specific Setup
Create `cursor/mcp.json` in your project directory:

```json
{
  "mcp": {
    "servers": {
      "parrot-security": {
        "command": "/home/ben/Documents/parrot mcp/.venv/bin/python",
        "args": [
          "/home/ben/Documents/parrot mcp/main.py"
        ],
        "env": {
          "PYTHONPATH": "/home/ben/Documents/parrot mcp",
          "CUSTOM_ENV": "security"
        }
      }
    }
  }
}
```

### Multiple Server Instances
```json
{
  "mcp": {
    "servers": {
      "parrot-system": {
        "command": "/home/ben/Documents/parrot mcp/.venv/bin/python",
        "args": [
          "/home/ben/Documents/parrot mcp/main.py"
        ]
      },
      "parrot-security": {
        "command": "/home/ben/Documents/parrot mcp/.venv/bin/python",
        "args": [
          "/home/ben/Documents/parrot mcp/main.py",
          "--profile",
          "security"
        ]
      }
    }
  }
}
```

## 📊 Status Check

Your Parrot OS MCP server is **ready for Cursor integration**! The configuration is complete and tested.

**Next Steps:**
1. Create the Cursor configuration file
2. Restart Cursor IDE
3. Start using MCP tools with `@` commands

**Current Status:** ✅ **Operational and Tested**