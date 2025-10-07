# Parrot OS MCP Server - AI Coding Guidelines

## Project Architecture

This is a **Model Context Protocol (MCP) server** for Parrot OS security operations. Key architectural patterns:

- **FastMCP Framework**: Uses `mcp.server.fastmcp.FastMCP` decorator pattern
- **Tool Structure**: All tools follow `@mcp.tool()` decorator pattern with async functions
- **Error Handling**: Consistent try-catch with context-aware error reporting
- **Path Handling**: Uses `pathlib.Path` for robust file operations

## Core Development Patterns

### Tool Implementation Template
```python
@mcp.tool()
async def tool_name(param: str, ctx: Context = None) -> str:
    """Clear docstring explaining tool purpose and parameters."""
    if ctx:
        await ctx.info(f"Action: {param}")
    
    try:
        # Implementation using pathlib.Path for file operations
        result = "operation completed"
        return result
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg
```

### Key File Patterns
- **main.py**: Primary MCP server with all tools and resources
- **test_server.py**: Direct testing without MCP client dependency
- **wifi_security_analyzer.py**: Security analysis component (standalone)

## Development Workflows

### Testing
- Use `python test_server.py` for quick tool testing
- Run `uv run mcp dev main.py` for MCP development with inspector
- Use `uv run mcp run main.py` for production execution

### Dependency Management
- **uv**: Primary package manager (preferred over pip)
- **mcp[cli]**: Core MCP framework dependency

### Security Considerations
- All tools execute with system-level privileges
- Validate user inputs before execution
- Use `subprocess.run()` with explicit parameters for shell commands
- Implement proper error handling to prevent information leakage

## Common Operations

### Adding New Tools
1. Use `@mcp.tool()` decorator pattern from existing examples
2. Include proper docstring with parameter descriptions
3. Implement async function with Context parameter
4. Add comprehensive error handling
5. Test with `test_server.py` before MCP integration

### File Operations
- Use `pathlib.Path` for all file/directory paths
- Check existence with `path.exists()` before operations
- Handle directories vs files appropriately
- Create parent directories with `parent.mkdir(parents=True, exist_ok=True)`

### Shell Command Execution
- Use `subprocess.run()` with `shell=True, capture_output=True, text=True`
- Include working directory support via `cwd` parameter
- Return exit code, stdout, and stderr in formatted output

## Project-Specific Conventions

- **Naming**: Tools use snake_case, resources use `parrot://` URI scheme
- **Logging**: Use `ctx.info()`, `ctx.warning()`, `ctx.error()` for context-aware logging
- **Output Format**: Return structured strings with clear success/error messages
- **Security**: Assume Parrot OS security context - tools may access sensitive system areas

## Integration Points

- **MCP Clients**: Claude Desktop, Cursor, other MCP-compatible tools
- **System Tools**: Integration with Parrot OS security tools in `/opt/`
- **WiFi Analysis**: `wifi_security_analyzer.py` provides standalone security assessment

## Quick Reference

Key files to understand patterns:
- `main.py:20-50` - Tool decorator pattern and error handling
- `main.py:51-100` - System information gathering
- `main.py:150-200` - File operation implementations
- `test_server.py` - Direct testing methodology

Always test new tools with both `test_server.py` and MCP inspector before deployment.