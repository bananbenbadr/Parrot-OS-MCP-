#!/usr/bin/env python3
"""
Test script for the Parrot OS MCP server.
This script tests the basic functionality without requiring MCP client setup.
"""

import asyncio
from main import mcp

async def test_tools():
    """Test the MCP server tools directly."""
    print("Testing Parrot OS MCP Server Tools...")
    print("=" * 50)
    
    # Test system info
    print("\n1. Testing get_system_info:")
    from main import get_system_info
    result = await get_system_info()
    print(f"System Info:\n{result[:200]}...")  # Show first 200 chars
    
    # Test directory listing
    print("\n2. Testing list_directory:")
    from main import list_directory
    result = await list_directory(".")
    print(f"Current directory:\n{result}")
    
    # Test file operations
    print("\n3. Testing file operations:")
    from main import write_file, read_file, delete_path
    
    # Write test file
    write_result = await write_file("/tmp/mcp_test.txt", "Hello from MCP test!")
    print(f"Write result: {write_result}")
    
    # Read test file
    read_result = await read_file("/tmp/mcp_test.txt")
    print(f"Read result: {read_result}")
    
    # Delete test file
    delete_result = await delete_path("/tmp/mcp_test.txt")
    print(f"Delete result: {delete_result}")
    
    # Test command execution
    print("\n4. Testing run_command:")
    from main import run_command
    cmd_result = await run_command("echo 'Hello from shell command'")
    print(f"Command result: {cmd_result}")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_tools())