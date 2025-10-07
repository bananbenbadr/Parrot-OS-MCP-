# Installing Node.js and npm for MCP Servers

This guide will help you install Node.js and npm to enable additional MCP servers in Cursor.

## 🚀 Quick Installation

### Option 1: Using Node Version Manager (nvm) - Recommended

```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Reload your shell
source ~/.bashrc

# Install latest LTS Node.js
nvm install --lts
nvm use --lts

# Verify installation
node --version
npm --version
```

### Option 2: Using Package Manager

#### Ubuntu/Debian (Parrot OS)
```bash
# Update package list
sudo apt update

# Install Node.js and npm
sudo apt install -y nodejs npm

# Verify installation
node --version
npm --version
```

#### Alternative: Install latest Node.js
```bash
# Add NodeSource repository
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

# Install Node.js
sudo apt install -y nodejs

# Verify installation
node --version
npm --version
```

### Option 3: Download from Official Site

1. Visit https://nodejs.org/
2. Download the LTS version for Linux
3. Extract and install:
   ```bash
   # Example for Node.js 20.x
   wget https://nodejs.org/dist/v20.10.0/node-v20.10.0-linux-x64.tar.xz
   tar -xf node-v20.10.0-linux-x64.tar.xz
   sudo mv node-v20.10.0-linux-x64 /opt/nodejs
   sudo ln -s /opt/nodejs/bin/node /usr/local/bin/node
   sudo ln -s /opt/nodejs/bin/npm /usr/local/bin/npm
   sudo ln -s /opt/nodejs/bin/npx /usr/local/bin/npx
   ```

## ✅ Verify Installation

After installation, verify everything works:

```bash
# Check versions
node --version  # Should show v18.x.x or higher
npm --version   # Should show 9.x.x or higher
npx --version   # Should show 9.x.x or higher

# Test npm
npm list -g --depth=0

# Test npx
npx --help
```

## 🔧 Install MCP Servers

Once Node.js and npm are installed, you can install MCP servers:

```bash
# Install core MCP servers
npx -y @modelcontextprotocol/server-filesystem --version
npx -y @modelcontextprotocol/server-git --version
npx -y @modelcontextprotocol/server-memory --version
npx -y @modelcontextprotocol/server-fetch --version
npx -y @modelcontextprotocol/server-time --version
```

## 🎯 Update Cursor Configuration

After installing Node.js/npm, you can use the complete MCP configuration:

1. **Copy the complete configuration:**
   ```bash
   cp "/home/ben/Documents/parrot mcp/cursor-mcp-complete-setup.sh" ~/install-mcp.sh
   chmod +x ~/install-mcp.sh
   ./install-mcp.sh
   ```

2. **Or manually update ~/.cursor/mcp.json** with the full configuration from `COMPLETE_MCP_SETUP.md`

## 🐛 Troubleshooting

### Common Issues

1. **Command not found: node/npm**
   - Restart your terminal
   - Check PATH: `echo $PATH`
   - Reinstall Node.js

2. **Permission errors with npm**
   ```bash
   # Fix npm permissions
   mkdir ~/.npm-global
   npm config set prefix '~/.npm-global'
   echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **npx not found**
   - Update npm: `npm install -g npm@latest`
   - Reinstall Node.js with npm included

4. **MCP servers fail to install**
   - Check internet connection
   - Try: `npm cache clean --force`
   - Use: `npx -y @modelcontextprotocol/server-name@latest`

### Verify MCP Server Installation

```bash
# Test individual servers
npx @modelcontextprotocol/server-filesystem --version
npx @modelcontextprotocol/server-git --version
npx @modelcontextprotocol/server-memory --version

# Test with specific directory
npx @modelcontextprotocol/server-filesystem /home/ben/Documents
```

## 📚 Next Steps

1. **Install Node.js/npm** using one of the methods above
2. **Run the complete setup script** to install all MCP servers
3. **Restart Cursor IDE** to load the new configuration
4. **Test the setup** by asking me to use various MCP tools

## 🎉 Benefits

With Node.js/npm installed, you'll have access to:

- **File System Operations**: Advanced file management
- **Git Integration**: Repository management
- **Memory Storage**: Persistent information storage
- **Web Fetching**: HTTP requests and web scraping
- **Time Utilities**: Date and time operations
- **And many more MCP servers!**

Your Parrot OS MCP server will continue to work regardless of Node.js installation, but adding Node.js unlocks many additional powerful tools for Cursor.
