# ==============================================================================
# CHALLENGE: The Firewall Log Parser (Cybersecurity Edition)
# ==============================================================================
#
# #### THE SCENARIO
# Your SIEM has captured a raw list of recent network traffic connection attempts.
# Your SOAR playbook needs to parse this traffic data to organize it for a security analyst.
#
# #### THE RULES
# 1. Malicious IPs (marked with "MALICIOUS_") must be blocked and put at the absolute top of the threat feed.
# 2. Suspicious IPs (marked with "SUSPICIOUS_") must be investigated next.
# 3. Clean traffic (regular IPs with no prefix) goes to the bottom of the report.
# 4. No duplicate alerts! If an IP scans the network 100 times, it should only appear once.
#
# #### INSTRUCTIONS
# 1. Do NOT use set().
# 2. Use loops, condition testing, and dynamic list methods.
# 3. Do NOT hardcode any IP addresses in your logic. It must be completely data-driven.
#
# #### EXPECTED OUTPUT
# When printed, your flat threat_feed must look exactly like this:
# ['MALICIOUS_185.220.101.5', 'MALICIOUS_45.146.164.22', 'SUSPICIOUS_10.0.0.99', 'SUSPICIOUS_193.56.28.11', '192.168.1.50', '172.16.0.5', '192.168.1.75']
# ==============================================================================

# Raw network traffic from the SIEM
traffic_logs = [
    "192.168.1.50", "SUSPICIOUS_10.0.0.99", "MALICIOUS_185.220.101.5",
    "192.168.1.50", "MALICIOUS_185.220.101.5", "172.16.0.5",
    "MALICIOUS_45.146.164.22", "SUSPICIOUS_10.0.0.99", "192.168.1.75",
    "SUSPICIOUS_193.56.28.11"
]
# Your job is to generate this final, flat list
threat_feed = []

# --- YOUR CODE GOES HERE ---
malicious_log = []
suspicious_log = []
regular_log = []

for logs in traffic_logs:
    if logs.startswith("MALICIOUS_"):
        if logs not in malicious_log:
            malicious_log.append(logs)
    elif logs.startswith("SUSPICIOUS_"):
        if logs not in suspicious_log:
            suspicious_log.append(logs)
    else:
        if logs not in regular_log:
            regular_log.append(logs)
threat_feed.extend(malicious_log)
threat_feed.extend(suspicious_log)
threat_feed.extend(regular_log)
# --- END OF YOUR CODE ---

print(threat_feed)
