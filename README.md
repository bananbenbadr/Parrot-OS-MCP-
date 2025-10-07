# Parrot OS MCP Server

A Model Context Protocol (MCP) server for interacting with Parrot OS. This server provides tools for shell commands, system information retrieval, and file management operations.

## Features

### Tools
- **run_command**: Execute shell commands and capture output
- **get_system_info**: Get detailed system information about Parrot OS
- **list_directory**: List contents of directories
- **read_file**: Read file contents
- **write_file**: Write content to files
- **copy_file**: Copy files and directories
- **delete_path**: Delete files and directories

### Resources
- **parrot://system/info**: Current system information
- **parrot://system/current-directory**: Current working directory

### Prompts
- **system_diagnostic_prompt**: Template for system diagnostic analysis

## Installation

1. Install Python dependencies:
```bash
uv sync
# or
pip install -r requirements.txt
```

2. Install the MCP server in Claude Desktop:
```bash
uv run mcp install main.py
```

## Usage

### Running the Server

```bash
# Development mode with MCP Inspector
uv run mcp dev main.py

# Direct execution
uv run mcp run main.py

# Or run directly with Python
python main.py
```

### Example Commands

1. **Execute a shell command**:
```
run_command "ls -la /home"
```

2. **Get system information**:
```
get_system_info
```

3. **List directory contents**:
```
list_directory "/var/log" show_hidden=true
```

4. **Read a file**:
```
read_file "/etc/hosts"
```

5. **Write to a file**:
```
write_file "/tmp/test.txt" "Hello, Parrot OS!"
```

## Security Considerations

This MCP server provides direct access to system operations. Use with caution:
- Only install from trusted sources
- Review the tools and resources exposed
- Consider running in a restricted environment
- Monitor command execution

## Development

### Adding New Tools

To add a new tool, use the `@mcp.tool()` decorator:

```python
@mcp.tool()
async def my_new_tool(param: str, ctx: Context = None) -> str:
    """Description of what the tool does."""
    # Your implementation here
    return "result"
```

### Adding New Resources

To add a new resource, use the `@mcp.resource()` decorator:

```python
@mcp.resource("parrot://custom/resource")
async def custom_resource() -> str:
    """Description of the resource."""
    return "resource content"
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.