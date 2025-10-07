#!/usr/bin/env python3
"""
Detailed exploration of Parrot OS security tools using MCP.
"""

import asyncio
from main import run_command, list_directory

async def detailed_security_exploration():
    """Detailed exploration of security tools."""
    print("🔍 Detailed Security Tools Exploration")
    print("=" * 60)
    
    # Explore /opt directory in detail
    print("\n1. Security Tools in /opt:")
    opt_listing = await list_directory("/opt")
    print(opt_listing)
    
    # Check specific security tool directories
    security_dirs = [
        "/opt/Awesome-Hacking",
        "/opt/BloodHound", 
        "/opt/Covenant",
        "/opt/Empire",
        "/opt/PayloadsAllTheThings",
        "/opt/Red-Teaming-Toolkit",
        "/opt/Scanners-Box",
        "/opt/impacket",
        "/opt/microsoft",
        "/opt/nuclei"
    ]
    
    print("\n2. Detailed Security Tool Directories:")
    for directory in security_dirs:
        print(f"\n   {directory}:")
        try:
            dir_content = await list_directory(directory)
            lines = dir_content.split('\n')
            if len(lines) > 5:
                print(f"   Contains {len(lines)} items (showing first 5):")
                for item in lines[:5]:
                    if item.strip():
                        print(f"     {item}")
                print(f"     ... and {len(lines)-5} more")
            else:
                for item in lines:
                    if item.strip():
                        print(f"     {item}")
        except Exception as e:
            print(f"     Error: {e}")
    
    # List popular security tools
    print("\n3. Popular Security Tools Available:")
    security_tools = [
        "nmap", "metasploit", "wireshark", "aircrack-ng", "hydra",
        "sqlmap", "john", "hashcat", "burpsuite", "nikto",
        "dirb", "gobuster", "enum4linux", "smbclient", "responder",
        "wifite", "reaver", "wash", "tshark", "tcpdump"
    ]
    
    available_tools = []
    for tool in security_tools:
        result = await run_command(f"which {tool} 2>/dev/null || echo 'not found'")
        if "not found" not in result:
            available_tools.append(tool)
    
    print(f"   Found {len(available_tools)} out of {len(security_tools)} popular security tools:")
    for tool in available_tools:
        print(f"     ✓ {tool}")
    
    # Get tool versions
    print("\n4. Tool Versions:")
    for tool in available_tools[:10]:  # Check first 10
        version_result = await run_command(f"{tool} --version 2>&1 | head -1 || echo 'Version check failed'")
        print(f"   {tool}: {version_result.strip()}")
    
    # Count tools by category
    print("\n5. Detailed Tool Counts:")
    categories = {
        "Wireless Tools": "aircrack|reaver|wash|wifite|kismet|wavemon",
        "Web App Tools": "sqlmap|nikto|dirb|gobuster|wapiti|wpscan",
        "Network Scanners": "nmap|masscan|zmap|netdiscover|angryip",
        "Password Tools": "hydra|john|hashcat|crunch|cewl|medusa",
        "Forensics Tools": "autopsy|sleuthkit|binwalk|foremost|volatility|bulk_extractor",
        "Exploitation Tools": "metasploit|armitage|beef|social-engineer-toolkit"
    }
    
    for category, pattern in categories.items():
        result = await run_command(f"ls /usr/bin /usr/sbin | grep -E '{pattern}' | wc -l")
        count = result.strip()
        print(f"   {category}: {count} tools")

if __name__ == "__main__":
    asyncio.run(detailed_security_exploration())