#!/usr/bin/env python3
"""
Script to use MCP tools to explore Parrot OS tools and utilities.
"""

import asyncio
from main import run_command, list_directory, get_system_info

async def explore_parrot_tools():
    """Use MCP tools to explore Parrot OS tools."""
    print("🔧 Exploring Parrot OS Tools using MCP Server")
    print("=" * 60)
    
    # First, get system info to understand the environment
    print("\n1. System Information:")
    system_info = await get_system_info()
    print(system_info[:300] + "...")
    
    # Explore common tool directories
    directories_to_explore = [
        "/usr/bin",      # Main system binaries
        "/usr/sbin",     # System administration binaries
        "/opt",          # Optional software (often security tools)
        "/bin",          # Essential system binaries
        "/sbin",         # System administration binaries
    ]
    
    for directory in directories_to_explore:
        print(f"\n2. Exploring {directory}:")
        try:
            listing = await list_directory(directory)
            # Count the number of tools/files
            lines = listing.split('\n')
            file_count = len([line for line in lines if line.strip() and 'file' in line])
            dir_count = len([line for line in lines if line.strip() and 'dir' in line])
            
            print(f"   Found {file_count} files, {dir_count} directories")
            
            # Show first 10 items
            first_items = lines[:10]
            for item in first_items:
                if item.strip():
                    print(f"   {item}")
            if len(lines) > 10:
                print(f"   ... and {len(lines) - 10} more items")
                
        except Exception as e:
            print(f"   Error accessing {directory}: {e}")
    
    # Look for specific security tool directories
    print("\n3. Security Tool Directories:")
    security_dirs = [
        "/usr/share/wireshark",
        "/usr/share/metasploit",
        "/usr/share/nmap",
        "/usr/bin/nmap",
        "/usr/bin/aircrack-ng",
        "/usr/bin/hydra",
        "/usr/bin/sqlmap",
        "/usr/bin/john",
    ]
    
    for tool_path in security_dirs:
        result = await run_command(f"ls -la {tool_path} 2>/dev/null || echo 'Not found'")
        if "Not found" not in result:
            print(f"   ✓ {tool_path} exists")
        else:
            print(f"   ✗ {tool_path} not found")
    
    # Count total tools in /usr/bin
    print("\n4. Counting tools in /usr/bin:")
    count_result = await run_command("ls /usr/bin | wc -l")
    print(f"   Total tools in /usr/bin: {count_result.strip()}")
    
    # Get some popular tool categories
    print("\n5. Tool Categories Overview:")
    categories = {
        "Network Tools": "netstat|ifconfig|ip|ping|traceroute|nmap|tcpdump",
        "Security Tools": "aircrack|metasploit|wireshark|john|hashcat|sqlmap|hydra",
        "Forensics Tools": "autopsy|sleuthkit|binwalk|foremost|volatility",
        "Crypto Tools": "gpg|openssl|ssh|ssl|encrypt|decrypt",
        "System Tools": "top|htop|ps|df|du|free|vmstat|iostat"
    }
    
    for category, pattern in categories.items():
        result = await run_command(f"ls /usr/bin | grep -E '{pattern}' | wc -l")
        count = result.strip()
        print(f"   {category}: {count} tools")

if __name__ == "__main__":
    asyncio.run(explore_parrot_tools())