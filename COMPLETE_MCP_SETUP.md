# Complete MCP Configuration for Cursor

This document provides a comprehensive MCP (Model Context Protocol) setup for Cursor IDE, including your custom Parrot OS server and many other useful MCP servers.

## 🚀 Quick Start

1. **Run the setup script:**
   ```bash
   ./cursor-mcp-complete-setup.sh
   ```

2. **Restart Cursor IDE** to load the new configuration

3. **Test the setup** by asking me to use various MCP tools

## 📋 MCP Servers Included

### Core Servers (No API Keys Required)

| Server | Description | Tools |
|--------|-------------|-------|
| **parrot-os** | Your custom Parrot OS security server | `run_command`, `get_system_info`, `list_directory`, `read_file`, `write_file`, `copy_file`, `delete_path` |
| **filesystem** | File system operations | File/directory management, search, read/write |
| **git** | Git repository management | Commit, push, pull, branch operations, history |
| **memory** | Persistent memory storage | Store/retrieve information across sessions |
| **fetch** | HTTP requests and web scraping | GET/POST requests, web content retrieval |
| **time** | Date and time utilities | Current time, timezone operations, date formatting |

### Optional Servers (Require API Keys)

| Server | Description | Required API Key |
|--------|-------------|------------------|
| **brave-search** | Web search using Brave Search API | `BRAVE_API_KEY` |
| **everart** | AI image generation | `EVERART_API_KEY` |
| **gdrive** | Google Drive integration | Google OAuth credentials |
| **github** | GitHub repository management | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| **slack** | Slack workspace integration | `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN` |
| **weather** | Weather information | `OPENWEATHER_API_KEY` |
| **puppeteer** | Web browser automation | None (requires Chrome/Chromium) |
| **sqlite** | SQLite database operations | None |
| **postgres** | PostgreSQL database operations | `POSTGRES_CONNECTION_STRING` |

## 🔧 Configuration Details

### File Location
- **Cursor MCP Config**: `~/.cursor/mcp.json`
- **Parrot OS Server**: `/home/ben/Documents/parrot mcp/`

### Parrot OS Server Features
Your custom Parrot OS MCP server provides:

- **Security Tools Access**: nmap, aircrack-ng, sqlmap, hydra, wireshark
- **System Management**: Process monitoring, system information
- **File Operations**: Advanced file management with security context
- **Command Execution**: Safe shell command execution with working directory support

## 🔑 API Key Configuration

To enable optional servers, add your API keys to the environment variables in `~/.cursor/mcp.json`:

### Brave Search
```bash
# Get API key from: https://brave.com/search/api/
export BRAVE_API_KEY="your-brave-api-key-here"
```

### GitHub
```bash
# Create token at: https://github.com/settings/tokens
export GITHUB_PERSONAL_ACCESS_TOKEN="your-github-token-here"
```

### Weather
```bash
# Get API key from: https://openweathermap.org/api
export OPENWEATHER_API_KEY="your-openweather-api-key-here"
```

### Everart
```bash
# Get API key from: https://everart.ai/
export EVERART_API_KEY="your-everart-api-key-here"
```

### Google Drive
1. Create credentials at: https://console.cloud.google.com/
2. Download JSON file to `~/.credentials/gdrive-credentials.json`
3. The server will create `~/.credentials/gdrive-token.json` automatically

### Slack
1. Create app at: https://api.slack.com/apps
2. Get Bot Token and App Token
3. Set environment variables:
   ```bash
   export SLACK_BOT_TOKEN="xoxb-your-bot-token"
   export SLACK_APP_TOKEN="xapp-your-app-token"
   ```

### PostgreSQL
```bash
export POSTGRES_CONNECTION_STRING="postgresql://username:password@localhost:5432/database"
```

## 🧪 Testing Your Setup

### Test Core Servers
Ask me to:
- "List files in the current directory" (filesystem)
- "Show git status" (git)
- "Store this information in memory" (memory)
- "Fetch content from a website" (fetch)
- "What time is it?" (time)
- "Run a security scan" (parrot-os)

### Test Parrot OS Server
Ask me to:
- "Show system information"
- "Run nmap on localhost"
- "List security tools available"
- "Check network interfaces"

## 🔧 Troubleshooting

### Common Issues

1. **MCP servers not loading**
   - Restart Cursor IDE
   - Check `~/.cursor/mcp.json` syntax
   - Verify Node.js and npm are installed

2. **Parrot OS server not working**
   - Ensure virtual environment is activated
   - Check Python dependencies: `pip install -r requirements.txt`
   - Verify file paths in configuration

3. **API key errors**
   - Check environment variables are set correctly
   - Verify API keys are valid and have proper permissions
   - Some servers may need additional setup (OAuth, etc.)

### Debug Commands

```bash
# Test MCP server installation
npx @modelcontextprotocol/server-filesystem --version

# Test Parrot OS server
cd "/home/ben/Documents/parrot mcp"
source venv/bin/activate
python -c "import mcp; print('MCP available')"

# Check Cursor configuration
cat ~/.cursor/mcp.json | jq .
```

## 📚 Advanced Usage

### Custom Server Development
You can add more custom MCP servers by:
1. Creating a new server script
2. Adding it to `~/.cursor/mcp.json`
3. Following the MCP protocol specification

### Server Management
- **Enable/Disable**: Comment out servers in `mcp.json`
- **Update**: Use `npx -y @modelcontextprotocol/server-name@latest`
- **Monitor**: Check Cursor's MCP logs for errors

## 🎯 Use Cases

### Security Research
- Use `parrot-os` for penetration testing
- Combine with `fetch` for web reconnaissance
- Store findings in `memory` for persistence

### Development Workflow
- Use `git` for version control
- Use `filesystem` for file management
- Use `github` for repository operations
- Use `memory` for project context

### Data Analysis
- Use `sqlite` or `postgres` for database operations
- Use `fetch` for data collection
- Use `filesystem` for data storage

### Content Creation
- Use `everart` for AI-generated images
- Use `fetch` for research
- Use `memory` for content planning

## 🔄 Updates

To update all MCP servers:
```bash
# Update all servers to latest versions
npx -y @modelcontextprotocol/server-filesystem@latest
npx -y @modelcontextprotocol/server-git@latest
# ... repeat for other servers
```

## 📞 Support

- **MCP Documentation**: https://modelcontextprotocol.io/
- **Cursor MCP Guide**: https://docs.cursor.com/mcp
- **Parrot OS Tools**: Your custom server documentation

---

**Note**: This configuration provides a comprehensive MCP setup. You can customize it by adding/removing servers based on your specific needs.
