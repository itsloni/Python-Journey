# ==============================================================================
# 🧠 DDOS TRAFFIC ANALYZER CHALLENGE
# ==============================================================================
#
# YOUR GOAL:
# Analyze a raw packet log to isolate malicious IP addresses that are part of
# a Distributed Denial of Service (DDoS) attack. Track everything dynamically
# using your new dictionary superpowers.
#
# ------------------------------------------------------------------------------
# ⚙️ THE SECURITY RULES
# ------------------------------------------------------------------------------
#
# 1. THE ATTACKER CRITERIA:
#    An IP address is considered an attacking bot ONLY IF it sends a "POST"
#    request AND receives a 404 server response code.
#
# 2. THE THRESHOLD:
#    If an IP address matches that exact malicious criteria 3 or more times,
#    it must be flagged as an active DDoS Attacker.
#
# 3. THE SUMMARY REPORT:
#    - Print a list of the flagged attacker IPs and the total number of
#      malicious requests they committed.
#    - Secure the reporting logic so that if the log finishes and NO attackers
#      crossed the threshold, it prints: "[INFO] Network traffic stable."
#
# ------------------------------------------------------------------------------
# WRITE YOUR SCALABLE, DICTIONARY-DRIVEN CODE BELOW:
# ==============================================================================

packet_log = [
    ("192.168.1.50", "GET", 200),
    ("185.220.101.5", "POST", 404),
    ("185.220.108.5", "POST", 404),
    ("185.220.108.5", "POST", 404),
    ("185.220.108.5", "POST", 404),
    ("185.220.108.5", "POST", 404),
    ("185.220.108.5", "POST", 404),
    ("192.168.1.50", "GET", 200),
    ("185.220.101.5", "POST", 404),
    ("142.250.190.46", "GET", 200),
    ("185.220.101.5", "POST", 404),
    ("185.220.101.9", "POST", 404),
    ("185.220.100.5", "POST", 404),
    ("185.220.101.5", "GET", 200),
    ("192.168.1.75", "GET", 200),
    ("185.220.101.5", "POST", 404)
]
flagged_attacker_ips = {}

for source_ip, request_type, server_response_code in packet_log:
    if request_type == "POST" and server_response_code == 404:
        if source_ip not in flagged_attacker_ips:
            flagged_attacker_ips[source_ip] = 0
        flagged_attacker_ips[source_ip] += 1


attack_found = False

for source_ip, num_malicious_requests in flagged_attacker_ips.items():
    if num_malicious_requests >= 3:
        print(f"[ALERT]!! {num_malicious_requests} Active DDoS Attacks from {source_ip} IP address!")
        attack_found = True
if not attack_found:
    print("[INFO] Network traffic stable")



