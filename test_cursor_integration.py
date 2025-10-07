#!/usr/bin/env python3
"""
Test script to verify MCP server integration with Cursor
"""

import asyncio
import subprocess
import json
import sys
import os

def test_mcp_server_import():
    """Test if MCP server can be imported"""
    print("🔧 Testing MCP Server Import...")
    try:
        from main import mcp
        print(f"✅ MCP server imported successfully")
        print(f"   Server name: {mcp.name}")
        print(f"   Instructions: {mcp.instructions}")
        return True
    except Exception as e:
        print(f"❌ Failed to import MCP server: {e}")
        return False

def test_mcp_protocol():
    """Test MCP protocol communication"""
    print("\n🔧 Testing MCP Protocol...")
    
    # Test initialization
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "cursor-test", "version": "1.0.0"}
        }
    }
    
    try:
        # Start the server and send initialization request
        process = subprocess.Popen(
            ["python", "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd="/home/ben/Documents/parrot mcp"
        )
        
        # Send initialization request
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            if "result" in response and "serverInfo" in response["result"]:
                print("✅ MCP initialization successful")
                print(f"   Server: {response['result']['serverInfo']['name']}")
                print(f"   Version: {response['result']['serverInfo']['version']}")
                print(f"   Protocol: {response['result']['protocolVersion']}")
                return True
            else:
                print(f"❌ Invalid initialization response: {response}")
                return False
        else:
            print("❌ No response from MCP server")
            return False
            
    except Exception as e:
        print(f"❌ MCP protocol test failed: {e}")
        return False
    finally:
        if 'process' in locals():
            process.terminate()

def test_cursor_config():
    """Test Cursor MCP configuration"""
    print("\n🔧 Testing Cursor Configuration...")
    
    config_path = os.path.expanduser("~/.cursor/mcp.json")
    if not os.path.exists(config_path):
        print("❌ Cursor MCP configuration not found")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        if "mcp" in config and "servers" in config["mcp"]:
            servers = config["mcp"]["servers"]
            if "parrot-os" in servers:
                print("✅ Cursor MCP configuration found")
                print(f"   Server: parrot-os")
                print(f"   Command: {servers['parrot-os']['command']}")
                print(f"   Args: {servers['parrot-os']['args']}")
                return True
            else:
                print("❌ parrot-os server not found in configuration")
                return False
        else:
            print("❌ Invalid MCP configuration structure")
            return False
            
    except Exception as e:
        print(f"❌ Failed to read Cursor configuration: {e}")
        return False

def test_python_environment():
    """Test Python virtual environment"""
    print("\n🔧 Testing Python Environment...")
    
    venv_python = "/home/ben/Documents/parrot mcp/venv/bin/python"
    if not os.path.exists(venv_python):
        print("❌ Virtual environment not found")
        return False
    
    try:
        # Test if MCP can be imported in the virtual environment
        result = subprocess.run([
            venv_python, "-c", 
            "import mcp; from main import mcp as server; print('MCP available')"
        ], capture_output=True, text=True, cwd="/home/ben/Documents/parrot mcp")
        
        if result.returncode == 0:
            print("✅ Python environment ready")
            print("   MCP module available in virtual environment")
            return True
        else:
            print(f"❌ Python environment test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Python environment test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Testing MCP Integration with Cursor")
    print("=" * 50)
    
    tests = [
        test_python_environment,
        test_mcp_server_import,
        test_cursor_config,
        test_mcp_protocol
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MCP is ready for Cursor integration.")
        print("\nNext steps:")
        print("1. Restart Cursor IDE")
        print("2. Test MCP tools by asking me to use them")
        print("3. Try commands like 'Show system information' or 'Run a security scan'")
    else:
        print("❌ Some tests failed. Check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
