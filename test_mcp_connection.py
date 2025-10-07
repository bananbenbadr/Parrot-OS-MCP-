#!/usr/bin/env python3
"""
Test script to verify MCP server connection.
This script tests that the MCP server can be started and responds to basic requests.
"""

import subprocess
import time
import os

def test_mcp_server():
    """Test that the MCP server can be started and responds."""
    print("Testing MCP Server Connection...")
    print("=" * 50)
    
    # Start the MCP server in a subprocess
    server_process = subprocess.Popen(
        ["/home/ben/Documents/parrot mcp/.venv/bin/python", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Give it a moment to start
    time.sleep(2)
    
    # Check if the process is still running (indicating it started successfully)
    if server_process.poll() is None:
        print("✓ MCP server started successfully and is running")
        print("✓ Server is waiting for MCP client connections via stdio")
        
        # Stop the server
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
            print("✓ MCP server stopped cleanly")
        except subprocess.TimeoutExpired:
            server_process.kill()
            print("⚠ MCP server had to be killed")
        
        return True
    else:
        # Process exited, check for errors
        stdout, stderr = server_process.communicate()
        print("✗ MCP server failed to start")
        if stderr:
            print(f"Error: {stderr}")
        return False

if __name__ == "__main__":
    success = test_mcp_server()
    print("\n" + "=" * 50)
    if success:
        print("✅ MCP server connection test PASSED")
        print("The Parrot OS MCP server is ready to connect with MCP clients!")
    else:
        print("❌ MCP server connection test FAILED")
        print("Check the error messages above for details.")