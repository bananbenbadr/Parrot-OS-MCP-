#!/usr/bin/env python3
"""
Comprehensive test of MCP server access to Parrot OS and its tools.
"""

import asyncio
import tempfile
import os
from main import run_command, get_system_info, list_directory, read_file, write_file, copy_file, delete_path

async def test_mcp_access():
    """Test MCP server access to Parrot OS and tools."""
    print("🔧 Comprehensive MCP Server Access Test")
    print("=" * 60)
    
    test_results = {}
    
    # Test 1: Basic system information
    print("\n1. Testing System Information Access:")
    try:
        system_info = await get_system_info()
        if "Parrot Security" in system_info:
            print("   ✅ Successfully accessed Parrot OS system info")
            test_results["system_info"] = "PASS"
        else:
            print("   ❌ Could not verify Parrot OS")
            test_results["system_info"] = "FAIL"
    except Exception as e:
        print(f"   ❌ Error: {e}")
        test_results["system_info"] = "ERROR"
    
    # Test 2: Security tool access
    print("\n2. Testing Security Tool Access:")
    security_tools = ["nmap", "aircrack-ng", "sqlmap", "hydra", "wireshark"]
    
    for tool in security_tools:
        try:
            result = await run_command(f"which {tool}")
            if "not found" not in result and tool in result:
                print(f"   ✅ {tool}: Available")
                test_results[f"tool_{tool}"] = "PASS"
            else:
                print(f"   ❌ {tool}: Not found")
                test_results[f"tool_{tool}"] = "FAIL"
        except Exception as e:
            print(f"   ❌ {tool}: Error - {e}")
            test_results[f"tool_{tool}"] = "ERROR"
    
    # Test 3: File system operations
    print("\n3. Testing File System Operations:")
    test_file = "/tmp/mcp_test_file.txt"
    test_content = "MCP Server File Operation Test - Success!"
    
    try:
        # Write file
        write_result = await write_file(test_file, test_content)
        if "Successfully" in write_result:
            print("   ✅ File write operation successful")
            test_results["file_write"] = "PASS"
        else:
            print(f"   ❌ File write failed: {write_result}")
            test_results["file_write"] = "FAIL"
        
        # Read file
        read_result = await read_file(test_file)
        if test_content in read_result:
            print("   ✅ File read operation successful")
            test_results["file_read"] = "PASS"
        else:
            print(f"   ❌ File read failed: {read_result}")
            test_results["file_read"] = "FAIL"
        
        # Delete file
        delete_result = await delete_path(test_file)
        if "Deleted" in delete_result:
            print("   ✅ File delete operation successful")
            test_results["file_delete"] = "PASS"
        else:
            print(f"   ❌ File delete failed: {delete_result}")
            test_results["file_delete"] = "FAIL"
            
    except Exception as e:
        print(f"   ❌ File operations error: {e}")
        test_results["file_operations"] = "ERROR"
    
    # Test 4: Directory operations
    print("\n4. Testing Directory Operations:")
    try:
        listing = await list_directory("/usr/bin")
        if "nmap" in listing and "python" in listing:
            print("   ✅ Directory listing successful")
            test_results["directory_list"] = "PASS"
        else:
            print("   ❌ Directory listing incomplete")
            test_results["directory_list"] = "FAIL"
    except Exception as e:
        print(f"   ❌ Directory operations error: {e}")
        test_results["directory_list"] = "ERROR"
    
    # Test 5: Command execution with security tools
    print("\n5. Testing Security Tool Execution:")
    
    # Test nmap
    try:
        nmap_result = await run_command("nmap --version")
        if "Nmap" in nmap_result:
            print("   ✅ Nmap execution successful")
            test_results["nmap_exec"] = "PASS"
        else:
            print(f"   ❌ Nmap execution failed: {nmap_result}")
            test_results["nmap_exec"] = "FAIL"
    except Exception as e:
        print(f"   ❌ Nmap error: {e}")
        test_results["nmap_exec"] = "ERROR"
    
    # Test aircrack-ng
    try:
        aircrack_result = await run_command("aircrack-ng --help")
        if "aircrack-ng" in aircrack_result:
            print("   ✅ Aircrack-ng execution successful")
            test_results["aircrack_exec"] = "PASS"
        else:
            print(f"   ❌ Aircrack-ng execution failed: {aircrack_result}")
            test_results["aircrack_exec"] = "FAIL"
    except Exception as e:
        print(f"   ❌ Aircrack-ng error: {e}")
        test_results["aircrack_exec"] = "ERROR"
    
    # Test 6: Complex command execution
    print("\n6. Testing Complex Command Execution:")
    try:
        complex_cmd = "ls /usr/bin | grep '^n' | head -5"
        result = await run_command(complex_cmd)
        if result.strip():
            print("   ✅ Complex command execution successful")
            print(f"   Result: {result.strip()}")
            test_results["complex_cmd"] = "PASS"
        else:
            print("   ❌ Complex command execution failed")
            test_results["complex_cmd"] = "FAIL"
    except Exception as e:
        print(f"   ❌ Complex command error: {e}")
        test_results["complex_cmd"] = "ERROR"
    
    # Test 7: Access to security directories
    print("\n7. Testing Security Directory Access:")
    security_dirs = ["/opt", "/usr/share/nmap", "/usr/share/wireshark"]
    
    for directory in security_dirs:
        try:
            dir_listing = await list_directory(directory)
            if dir_listing and "Error" not in dir_listing:
                print(f"   ✅ Access to {directory} successful")
                test_results[f"dir_access_{directory.replace('/', '_')}"] = "PASS"
            else:
                print(f"   ❌ Access to {directory} failed")
                test_results[f"dir_access_{directory.replace('/', '_')}"] = "FAIL"
        except Exception as e:
            print(f"   ❌ {directory} access error: {e}")
            test_results[f"dir_access_{directory.replace('/', '_')}"] = "ERROR"
    
    # Generate summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY:")
    print("=" * 60)
    
    passed = sum(1 for result in test_results.values() if result == "PASS")
    failed = sum(1 for result in test_results.values() if result == "FAIL")
    errors = sum(1 for result in test_results.values() if result == "ERROR")
    total = len(test_results)
    
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Errors: {errors}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! MCP server has full access to Parrot OS and tools!")
    else:
        print(f"\n⚠ {passed}/{total} tests passed. Review failed tests above.")
    
    return test_results

if __name__ == "__main__":
    asyncio.run(test_mcp_access())