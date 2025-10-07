#!/usr/bin/env python3
"""
WiFi Security Analyzer Tool

This tool analyzes netsh wlan show networks output to identify
networks with weak security configurations.
"""

import re
from typing import Dict, List, Tuple

class WiFiSecurityAnalyzer:
    def __init__(self):
        self.security_levels = {
            'WPA3': {'rating': 5, 'risk': 'Very Low', 'description': 'Latest standard, strongest security'},
            'WPA2-Enterprise': {'rating': 4, 'risk': 'Low', 'description': 'Enterprise-grade with RADIUS'},
            'WPA2': {'rating': 4, 'risk': 'Low', 'description': 'AES encryption, strong for home use'},
            'WPA': {'rating': 3, 'risk': 'Medium', 'description': 'Better than WEP but outdated'},
            'WEP': {'rating': 1, 'risk': 'Critical', 'description': 'Easily crackable, obsolete'},
            'Open': {'rating': 0, 'risk': 'Critical', 'description': 'No encryption, high risk'}
        }
        
        self.vulnerable_patterns = [
            (r'WEP', 'WEP encryption - easily crackable'),
            (r'Open', 'No encryption - extremely vulnerable'),
            (r'TKIP', 'TKIP cipher - vulnerable to attacks'),
            (r'WPA\b.*TKIP', 'WPA with TKIP - weak combination'),
            (r'WPS.*Enabled', 'WPS enabled - PIN attack vulnerable')
        ]
    
    def analyze_netsh_output(self, netsh_output: str) -> Dict:
        """Analyze netsh wlan show networks output"""
        networks = []
        current_network = {}
        
        lines = netsh_output.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Detect new network section
            if line.startswith('SSID '):
                if current_network:
                    networks.append(self._analyze_network(current_network))
                current_network = {'ssid': line.split(':', 1)[1].strip()}
            
            # Parse network details
            elif ':' in line and current_network:
                key, value = [part.strip() for part in line.split(':', 1)]
                current_network[key.lower()] = value
        
        # Add the last network
        if current_network:
            networks.append(self._analyze_network(current_network))
        
        return {
            'networks': networks,
            'vulnerable_networks': [net for net in networks if net['security_rating'] <= 2],
            'total_networks': len(networks),
            'vulnerable_count': len([net for net in networks if net['security_rating'] <= 2])
        }
    
    def _analyze_network(self, network: Dict) -> Dict:
        """Analyze individual network security"""
        ssid = network.get('ssid', 'Unknown')
        auth = network.get('authentication', '').lower()
        cipher = network.get('cipher', '').lower()
        
        # Determine security level
        security_rating = 3  # Default to medium
        security_type = 'Unknown'
        vulnerabilities = []
        
        # Check for specific patterns
        if 'open' in auth:
            security_rating = 0
            security_type = 'Open'
            vulnerabilities.append('No encryption')
        elif 'wep' in auth:
            security_rating = 1
            security_type = 'WEP'
            vulnerabilities.append('WEP encryption (easily crackable)')
        elif 'wpa2' in auth:
            security_rating = 4
            security_type = 'WPA2'
            if 'tkip' in cipher:
                security_rating = 2
                vulnerabilities.append('WPA2 with TKIP (weakened)')
        elif 'wpa' in auth:
            security_rating = 3
            security_type = 'WPA'
            if 'tkip' in cipher:
                security_rating = 2
                vulnerabilities.append('WPA with TKIP (vulnerable)')
        
        # Check signal strength
        signal = network.get('signal', '0%')
        try:
            signal_strength = int(signal.replace('%', ''))
        except:
            signal_strength = 0
        
        return {
            'ssid': ssid,
            'authentication': network.get('authentication', 'Unknown'),
            'cipher': network.get('cipher', 'Unknown'),
            'signal': signal,
            'security_type': security_type,
            'security_rating': security_rating,
            'vulnerabilities': vulnerabilities,
            'signal_strength': signal_strength,
            'risk_level': self._get_risk_level(security_rating)
        }
    
    def _get_risk_level(self, rating: int) -> str:
        """Convert rating to risk level"""
        if rating >= 4:
            return 'Low'
        elif rating == 3:
            return 'Medium'
        elif rating == 2:
            return 'High'
        else:
            return 'Critical'
    
    def generate_report(self, analysis: Dict) -> str:
        """Generate security assessment report"""
        report = []
        report.append("📊 WiFi Security Assessment Report")
        report.append("=" * 40)
        report.append(f"Total networks found: {analysis['total_networks']}")
        report.append(f"Vulnerable networks: {analysis['vulnerable_count']}")
        report.append("")
        
        if analysis['vulnerable_networks']:
            report.append("🔴 HIGH-RISK NETWORKS:")
            report.append("-" * 20)
            for net in analysis['vulnerable_networks']:
                report.append(f"SSID: {net['ssid']}")
                report.append(f"  Security: {net['authentication']} ({net['cipher']})")
                report.append(f"  Risk: {net['risk_level']}")
                if net['vulnerabilities']:
                    report.append(f"  Vulnerabilities: {', '.join(net['vulnerabilities'])}")
                report.append(f"  Signal: {net['signal']}")
                report.append("")
        else:
            report.append("✅ No high-risk networks found")
            report.append("")
        
        report.append("📈 All Networks Summary:")
        report.append("-" * 25)
        for net in analysis['networks']:
            risk_icon = "🔴" if net['risk_level'] == 'Critical' else "🟡" if net['risk_level'] == 'High' else "🟢"
            report.append(f"{risk_icon} {net['ssid']:20} {net['risk_level']:8} ({net['authentication']})")
        
        return "\n".join(report)

# Example usage and test
def main():
    analyzer = WiFiSecurityAnalyzer()
    
    print("🔍 WiFi Security Analyzer")
    print("=" * 25)
    print("This tool helps analyze netsh wlan show networks output")
    print("")
    print("Usage:")
    print("1. Open Windows Command Prompt as Administrator")
    print("2. Run: netsh wlan show networks")
    print("3. Copy the output and paste it here")
    print("4. Type 'END' on a new line when finished")
    print("")
    
    # Get input from user
    print("Paste netsh output below:")
    input_lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            input_lines.append(line)
        except EOFError:
            break
    
    netsh_output = "\n".join(input_lines)
    
    if not netsh_output.strip():
        print("No input provided. Using example data...")
        # Example data for testing
        netsh_output = """
SSID 1 : HomeNetwork
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP
    Signal                  : 85%

SSID 2 : OpenCafe
    Network type            : Infrastructure
    Authentication          : Open
    Encryption              : None
    Signal                  : 60%

SSID 3 : OldRouter
    Network type            : Infrastructure
    Authentication          : WEP
    Encryption              : WEP
    Signal                  : 45%

SSID 4 : NeighborWifi
    Network type            : Infrastructure
    Authentication          : WPA-Personal
    Encryption              : TKIP
    Signal                  : 70%
        """
    
    # Analyze and report
    analysis = analyzer.analyze_netsh_output(netsh_output)
    report = analyzer.generate_report(analysis)
    
    print("\n" + "=" * 50)
    print(report)

if __name__ == "__main__":
    main()