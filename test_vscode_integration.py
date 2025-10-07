#!/usr/bin/env python3
"""
Test script to verify the MCP server configuration for VS Code integration.
"""

import subprocess
import time
import os

def test_vscode_integration():
    """Test that the MCP server works with VS Code configuration."""
    print("🔧 Testing VS Code MCP Server Integration")
    print("=" * 60)
    
    # Test the exact command that VS Code will use
    cmd = [
        "/home/ben/Documents/parrot mcp/.venv/bin/python",
        "/home/ben/Documents/parrot mcp/main.py"
    ]
    
    env = os.environ.copy()
    env["PYTHONPATH"] = "/home/ben/Documents/parrot mcp"
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Environment: PYTHONPATH={env['PYTHONPATH']}")
    
    # Start the server
    server_process = subprocess.Popen(
        cmd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Give it a moment to start
    time.sleep(2)
    
    # Check if it's running
    if server_process.poll() is None:
        print("✅ MCP server started successfully with VS Code configuration")
        print("✅ Server is ready for VS Code connections")
        
        # Stop the server
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
            print("✅ MCP server stopped cleanly")
        except subprocess.TimeoutExpired:
            server_process.kill()
            print("⚠ MCP server had to be killed")
        
        return True
    else:
        # Process exited, check for errors
        stdout, stderr = server_process.communicate()
        print("❌ MCP server failed to start with VS Code configuration")
        if stderr:
            print(f"Error: {stderr}")
        if stdout:
            print(f"Output: {stdout}")
        return False

def check_configuration():
    """Check the MCP configuration file."""
    print("\n📋 Checking MCP Configuration:")
    print("-" * 40)
    
    # Read the configuration
    try:
        with open(os.path.expanduser("~/.config/Code/User/mcp.json"), 'r') as f:
            config = f.read()
        
        if "parrot-os-server" in config:
            print("✅ Parrot OS MCP server found in VS Code configuration")
            
            # Check if paths are correct
            if "/home/ben/Documents/parrot mcp/.venv/bin/python" in config:
                print("✅ Python path is correct")
            else:
                print("❌ Python path might be incorrect")
                
            if "/home/ben/Documents/parrot mcp/main.py" in config:
                print("✅ Main script path is correct")
            else:
                print("❌ Main script path might be incorrect")
                
            return True
        else:
            print("❌ Parrot OS MCP server not found in configuration")
            return False
            
    except FileNotFoundError:
        print("❌ MCP configuration file not found")
        return False
    except Exception as e:
        print(f"❌ Error reading configuration: {e}")
        return False

if __name__ == "__main__":
    config_ok = check_configuration()
    
    if config_ok:
        print("\n" + "=" * 60)
        integration_ok = test_vscode_integration()
        
        print("\n" + "=" * 60)
        if integration_ok:
            print("🎉 VS Code MCP Integration Test PASSED!")
            print("The Parrot OS MCP server is ready for VS Code!")
        else:
            print("❌ VS Code MCP Integration Test FAILED!")
            print("Check the configuration and try again.")
    else:
        print("\n❌ Configuration check failed. Please fix mcp.json")