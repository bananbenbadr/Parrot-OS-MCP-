"""
Parrot OS MCP Server

A Model Context Protocol server for interacting with Parrot OS.
Provides tools for shell commands, system information, and file management.
"""

import asyncio
import subprocess
import os
import platform
import shutil
from typing import Optional
from pathlib import Path

from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession

# Create MCP server instance
mcp = FastMCP(
    "Parrot OS",
    instructions="MCP server for Parrot OS interaction with shell commands, system info, and file management"
)


@mcp.tool()
async def run_command(
    command: str,
    working_directory: Optional[str] = None,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Execute a shell command on Parrot OS and return the output."""
    if ctx:
        await ctx.info(f"Executing command: {command}")
    
    try:
        # Set working directory if specified
        cwd = Path(working_directory) if working_directory else None
        
        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        
        output = f"Exit code: {result.returncode}\n"
        if result.stdout:
            output += f"STDOUT:\n{result.stdout}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"
        
        return output
    
    except Exception as e:
        error_msg = f"Error executing command: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.tool()
async def get_system_info(ctx: Context[ServerSession, None] = None) -> str:
    """Get detailed system information about Parrot OS."""
    if ctx:
        await ctx.info("Gathering system information")
    
    info_lines = []
    
    # Basic system info
    info_lines.append(f"System: {platform.system()}")
    info_lines.append(f"Node: {platform.node()}")
    info_lines.append(f"Release: {platform.release()}")
    info_lines.append(f"Version: {platform.version()}")
    info_lines.append(f"Machine: {platform.machine()}")
    info_lines.append(f"Processor: {platform.processor()}")
    
    # Parrot OS specific info
    try:
        # Try to get Parrot OS version
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release", 'r') as f:
                os_release = f.read()
            info_lines.append(f"OS Release:\n{os_release}")
        
        # Get memory info
        if os.path.exists("/proc/meminfo"):
            with open("/proc/meminfo", 'r') as f:
                mem_info = f.read()
            info_lines.append(f"Memory Info:\n{mem_info}")
            
    except Exception as e:
        if ctx:
            await ctx.warning(f"Could not read system files: {str(e)}")
    
    return "\n".join(info_lines)


@mcp.tool()
async def list_directory(
    path: str = ".",
    show_hidden: bool = False,
    ctx: Context[ServerSession, None] = None
) -> str:
    """List contents of a directory."""
    if ctx:
        await ctx.info(f"Listing directory: {path}")
    
    try:
        dir_path = Path(path)
        if not dir_path.exists():
            return f"Directory does not exist: {path}"
        
        if not dir_path.is_dir():
            return f"Path is not a directory: {path}"
        
        items = []
        for item in dir_path.iterdir():
            if not show_hidden and item.name.startswith('.'):
                continue
            
            item_type = "dir" if item.is_dir() else "file"
            size = item.stat().st_size if item.is_file() else "-"
            items.append(f"{item_type:4} {size:8} {item.name}")
        
        return "\n".join(sorted(items))
    
    except Exception as e:
        error_msg = f"Error listing directory: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.tool()
async def read_file(
    file_path: str,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Read the contents of a file."""
    if ctx:
        await ctx.info(f"Reading file: {file_path}")
    
    try:
        file_path_obj = Path(file_path)
        if not file_path_obj.exists():
            return f"File does not exist: {file_path}"
        
        if not file_path_obj.is_file():
            return f"Path is not a file: {file_path}"
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        return content
    
    except Exception as e:
        error_msg = f"Error reading file: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.tool()
async def write_file(
    file_path: str,
    content: str,
    append: bool = False,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Write content to a file."""
    if ctx:
        await ctx.info(f"Writing to file: {file_path}")
    
    try:
        file_path_obj = Path(file_path)
        
        # Create parent directories if they don't exist
        file_path_obj.parent.mkdir(parents=True, exist_ok=True)
        
        mode = 'a' if append else 'w'
        with open(file_path, mode) as f:
            f.write(content)
        
        return f"Successfully {'appended to' if append else 'wrote'} file: {file_path}"
    
    except Exception as e:
        error_msg = f"Error writing file: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.tool()
async def copy_file(
    source: str,
    destination: str,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Copy a file or directory."""
    if ctx:
        await ctx.info(f"Copying from {source} to {destination}")
    
    try:
        source_path = Path(source)
        dest_path = Path(destination)
        
        if not source_path.exists():
            return f"Source does not exist: {source}"
        
        if source_path.is_file():
            shutil.copy2(source_path, dest_path)
            return f"Copied file: {source} -> {destination}"
        elif source_path.is_dir():
            shutil.copytree(source_path, dest_path)
            return f"Copied directory: {source} -> {destination}"
        else:
            return f"Source is neither file nor directory: {source}"
    
    except Exception as e:
        error_msg = f"Error copying: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.tool()
async def delete_path(
    path: str,
    recursive: bool = False,
    ctx: Context[ServerSession, None] = None
) -> str:
    """Delete a file or directory."""
    if ctx:
        await ctx.info(f"Deleting: {path}")
    
    try:
        path_obj = Path(path)
        
        if not path_obj.exists():
            return f"Path does not exist: {path}"
        
        if path_obj.is_file():
            path_obj.unlink()
            return f"Deleted file: {path}"
        elif path_obj.is_dir():
            if recursive:
                shutil.rmtree(path_obj)
                return f"Deleted directory recursively: {path}"
            else:
                # Try to delete empty directory
                path_obj.rmdir()
                return f"Deleted directory: {path}"
        else:
            return f"Path is neither file nor directory: {path}"
    
    except Exception as e:
        error_msg = f"Error deleting: {str(e)}"
        if ctx:
            await ctx.error(error_msg)
        return error_msg


@mcp.resource("parrot://system/info")
async def system_info_resource() -> str:
    """Resource providing current system information."""
    return await get_system_info()


@mcp.resource("parrot://system/current-directory")
async def current_directory_resource() -> str:
    """Resource providing current working directory."""
    return f"Current directory: {os.getcwd()}"


@mcp.prompt()
def system_diagnostic_prompt() -> str:
    """Prompt for system diagnostic analysis."""
    return """Please analyze the current system state and provide:
1. System health assessment
2. Potential issues or anomalies
3. Recommendations for optimization
4. Security considerations

Use the available tools to gather system information first."""


if __name__ == "__main__":
    # Run the server with stdio transport for MCP clients
    mcp.run(transport="stdio")