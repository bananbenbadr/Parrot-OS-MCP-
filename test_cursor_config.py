#!/usr/bin/env python3
"""
Comprehensive test script for Cursor MCP configuration
"""

import json
import os
import subprocess
import sys

def test_config_file_exists():
    """Test if configuration file exists and is readable"""
    print("🔍 Testing configuration file existence...")
    config_path = os.path.expanduser("~/.cursor/mcp.json")
    
    if not os.path.exists(config_path):
        print("❌ Configuration file does not exist")
        return False
    
    if not os.access(config_path, os.R_OK):
        print("❌ Configuration file is not readable")
        return False
    
    print(f"✅ Configuration file exists: {config_path}")
    return True

def test_config_json_syntax():
    """Test JSON syntax validity"""
    print("\n🔍 Testing JSON syntax...")
    config_path = os.path.expanduser("~/.cursor/mcp.json")
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ JSON syntax is valid")
        return True, config
    except json.JSONDecodeError as e:
        print(f"❌ JSON syntax error: {e}")
        return False, None
    except Exception as e:
        print(f"❌ Error reading configuration: {e}")
        return False, None

def test_config_structure(config):
    """Test configuration structure"""
    print("\n🔍 Testing configuration structure...")
    
    required_keys = ["mcp", "servers", "parrot-os"]
    current = config
    
    for key in required_keys:
        if key not in current:
            print(f"❌ Missing required key: {key}")
            return False
        current = current[key]
        print(f"✅ Found key: {key}")
    
    print("✅ Configuration structure is valid")
    return True

def test_server_config(config):
    """Test server configuration details"""
    print("\n🔍 Testing server configuration...")
    
    server_config = config["mcp"]["servers"]["parrot-os"]
    
    # Test required fields
    required_fields = ["command", "args", "env"]
    for field in required_fields:
        if field not in server_config:
            print(f"❌ Missing required field: {field}")
            return False
        print(f"✅ Found field: {field}")
    
    # Test command path
    command_path = server_config["command"]
    if not os.path.exists(command_path):
        print(f"❌ Command path does not exist: {command_path}")
        return False
    print(f"✅ Command path exists: {command_path}")
    
    # Test script path
    script_path = server_config["args"][0]
    if not os.path.exists(script_path):
        print(f"❌ Script path does not exist: {script_path}")
        return False
    print(f"✅ Script path exists: {script_path}")
    
    # Test environment variable
    env_pythonpath = server_config["env"]["PYTHONPATH"]
    if not os.path.exists(env_pythonpath):
        print(f"❌ PYTHONPATH does not exist: {env_pythonpath}")
        return False
    print(f"✅ PYTHONPATH exists: {env_pythonpath}")
    
    print("✅ Server configuration is valid")
    return True

def test_mcp_server_execution():
    """Test MCP server execution"""
    print("\n🔍 Testing MCP server execution...")
    
    try:
        # Change to the correct directory
        os.chdir("/home/ben/Documents/parrot mcp")
        
        # Test server startup
        process = subprocess.Popen(
            ["python", "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send initialization request
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
        
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            if "result" in response and "serverInfo" in response["result"]:
                server_info = response["result"]["serverInfo"]
                print(f"✅ MCP server responds correctly")
                print(f"   Server: {server_info['name']}")
                print(f"   Version: {server_info['version']}")
                print(f"   Protocol: {response['result']['protocolVersion']}")
                return True
            else:
                print(f"❌ Invalid server response: {response}")
                return False
        else:
            print("❌ No response from MCP server")
            return False
            
    except Exception as e:
        print(f"❌ MCP server execution test failed: {e}")
        return False
    finally:
        if 'process' in locals():
            process.terminate()

def test_cursor_integration():
    """Test Cursor integration readiness"""
    print("\n🔍 Testing Cursor integration readiness...")
    
    # Check if Cursor directory exists
    cursor_dir = os.path.expanduser("~/.cursor")
    if not os.path.exists(cursor_dir):
        print("❌ Cursor directory not found")
        return False
    print(f"✅ Cursor directory exists: {cursor_dir}")
    
    # Check if MCP configuration is in the right place
    mcp_config = os.path.join(cursor_dir, "mcp.json")
    if not os.path.exists(mcp_config):
        print("❌ MCP configuration not found in Cursor directory")
        return False
    print(f"✅ MCP configuration in Cursor directory: {mcp_config}")
    
    print("✅ Cursor integration is ready")
    return True

def main():
    """Run all configuration tests"""
    print("🚀 Testing Cursor MCP Configuration")
    print("=" * 50)
    
    tests = [
        ("File Existence", test_config_file_exists),
        ("JSON Syntax", lambda: test_config_json_syntax()[0]),
        ("Config Structure", lambda: test_config_structure(test_config_json_syntax()[1]) if test_config_json_syntax()[0] else False),
        ("Server Config", lambda: test_server_config(test_config_json_syntax()[1]) if test_config_json_syntax()[0] else False),
        ("MCP Execution", test_mcp_server_execution),
        ("Cursor Integration", test_cursor_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            print()
    
    print("=" * 50)
    print(f"📊 Configuration Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All configuration tests passed!")
        print("✅ Cursor MCP configuration is properly set and working")
        print("\nConfiguration Summary:")
        print("  • File: ~/.cursor/mcp.json")
        print("  • Server: parrot-os")
        print("  • Command: /home/ben/Documents/parrot mcp/venv/bin/python")
        print("  • Script: /home/ben/Documents/parrot mcp/main.py")
        print("  • Status: Ready for Cursor integration")
    else:
        print("❌ Some configuration tests failed")
        print("Check the errors above and fix the configuration")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
