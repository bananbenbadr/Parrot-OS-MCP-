#!/usr/bin/env python3
"""
Quick overview of the most interesting security tools in Parrot OS.
"""

import asyncio
from main import run_command

async def quick_tool_overview():
    """Quick overview of security tools."""
    print("🔍 Quick Parrot OS Security Tools Overview")
    print("=" * 60)
    
    # Most interesting security tools
    tools = [
        "nmap", "metasploit", "wireshark", "aircrack-ng", "hydra",
        "sqlmap", "john", "hashcat", "burpsuite", "nikto",
        "dirb", "gobuster", "enum4linux", "smbclient", "responder",
        "wifite", "reaver", "wash", "tshark", "tcpdump",
        "msfconsole", "msfvenom", "armitage", "beef-xss", "setoolkit"
    ]
    
    print("\nMost Interesting Security Tools:")
    print("-" * 40)
    
    available = []
    not_available = []
    
    for tool in tools:
        result = await run_command(f"which {tool} 2>/dev/null || echo 'not found'")
        if "not found" not in result:
            available.append(tool)
        else:
            not_available.append(tool)
    
    print(f"✅ Available ({len(available)}):")
    for tool in available:
        print(f"   - {tool}")
    
    print(f"\n❌ Not Available ({len(not_available)}):")
    for tool in not_available:
        print(f"   - {tool}")
    
    # Show some versions
    print(f"\n🔧 Tool Versions:")
    print("-" * 40)
    for tool in available[:8]:
        version = await run_command(f"{tool} --version 2>&1 | head -1 || echo 'Version unknown'")
        print(f"{tool:15}: {version.strip()}")

if __name__ == "__main__":
    asyncio.run(quick_tool_overview())