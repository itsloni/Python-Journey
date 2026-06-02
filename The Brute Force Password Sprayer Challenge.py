# ==============================================================================
# 🧠 THE BRUTE-FORCE PASSWORD SPRAYER CHALLENGE
# ==============================================================================
#
# YOUR GOAL:
# Analyze an authentication log to flag a sophisticated "Password Spraying"
# cyberattack. Track everything dynamically using your dictionary skills.
#
# ------------------------------------------------------------------------------
# 📥 THE INPUTS (Your Raw Authentication Data)
# ------------------------------------------------------------------------------

# Format: (timestamp, employee_username, authentication_status, source_ip)
# auth_log = [
#     ("09:00", "alice_admin", "Success", "192.168.1.15"),
#     ("09:01", "bob_finance", "Failed",  "185.45.22.9"),   # Threat IP tries Bob
#     ("09:02", "charlie_hr",  "Failed",  "185.45.22.9"),   # Threat IP tries Charlie
#     ("09:03", "david_dev",   "Failed",  "185.45.22.9"),   # Threat IP tries David
#     ("09:04", "eve_sales",   "Success", "192.168.1.20"),
#     ("09:05", "frank_exec",  "Failed",  "185.45.22.9"),   # Threat IP tries Frank
#     ("09:06", "grace_ops",   "Failed",  "104.244.42.1"),  # Random single failure
#     ("09:07", "bob_finance", "Success", "192.168.1.22")
# ]

# ------------------------------------------------------------------------------
# ⚙️ THE SECURITY RULES
# ------------------------------------------------------------------------------
#
# 1. THE ATTACKER CRITERIA:
#    In a traditional brute-force attack, a hacker hits ONE account many times.
#    In a "Password Spraying" attack, a hacker uses ONE bad IP address to try
#    a common password against MANY DIFFERENT user accounts to fly under the radar.
#
#    Your engine must count how many times a single 'source_ip' causes an
#    authentication status of "Failed".
#
# 2. THE THRESHOLD:
#    If a single 'source_ip' triggers a "Failed" status 4 or more times
#    across the entire log, flag that IP as an active 'Password Sprayer'.
#
# 3. THE SUMMARY REPORT:
#    - Print a critical alert showing any flagged malicious IP addresses
#      and the exact count of failed attempts they generated.
#    - Ensure that if the log is clean and no IP addresses hit the threat
#      threshold, it prints: "[INFO] Authentication traffic clean."
#
# ------------------------------------------------------------------------------
# WRITE YOUR CODE BELOW:
# ==============================================================================


auth_log = [
    ("09:00", "alice_admin", "Success", "192.168.1.15"),
    ("09:01", "bob_finance", "Failed",  "185.45.22.9"),   # Threat IP tries Bob
    ("09:02", "charlie_hr",  "Failed",  "185.45.22.9"),   # Threat IP tries Charlie
    ("09:03", "david_dev",   "Failed",  "185.45.22.9"),   # Threat IP tries David
    ("09:04", "eve_sales",   "Success", "192.168.1.20"),
    ("09:05", "frank_exec",  "Failed",  "185.45.22.9"),   # Threat IP tries Frank
    ("09:06", "grace_ops",   "Failed",  "104.244.42.1"),  # Random single failure
    ("09:07", "bob_finance", "Success", "192.168.1.22")
]
num_triggers_per_ip = {}

for timestamp, employee_username, authentication_status, source_ip in auth_log:
    if authentication_status == "Failed":
        if source_ip not in num_triggers_per_ip:
            num_triggers_per_ip[source_ip] = 0
        num_triggers_per_ip[source_ip] += 1

log_clean = True

for flagged_ip, occurrence in num_triggers_per_ip.items():
    if occurrence >= 4:
        log_clean = False
        print(f"[ALERT]!! {occurrence} Failed attempts detected from {flagged_ip} IP addresses!!")
if log_clean:
    print("[INFO] Authentication traffic clean.")