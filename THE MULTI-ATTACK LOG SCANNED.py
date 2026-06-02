# ==============================================================================
# 🧠 UPGRADED CHALLENGE: THE MULTI-ATTACK LOG SCANNED
# ==============================================================================
#
# YOUR NEW GOAL:
# Scan the ENTIRE network stream. Do NOT stop at the first threat.
# Track ALL breaches and failed logins to give the security team a full report.
#
# ------------------------------------------------------------------------------
# 📥 THE INPUTS (Your Configuration and Live Data)
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ⚙️ THE NEW LOGIC RULES (No Breaks!)
# ------------------------------------------------------------------------------
#
# 1. TRACKING VARIABLES:
#    -   (An empty list to store every hacked port we find!)
#
# 2. THE LOOP: Use a single 'for port, status in network_stream:' loop.
#    (We don't even need 'while' or 'break' anymore because we want to see everything!)
#
# 3. THE DETECTION ENGINE (Inside the loop):
#    - Check for Port Breach: If port == FORBIDDEN_PORT OR port == 9999:
#         And if status == "Success":
#             Add that port number to your breached_ports list! (.append(port))
#
#    - Check for Failed Logins: If status == "Failed":
#         Increment your failed_logins counter by 1.
#
# 4. THE FINAL REPORT (Outside the loop, after it completely finishes):
#    - Print a summary of what happened:
#      If any ports were breached, or if failed_logins >= MAX_ALLOWED_FAILURES:
#          Print "[CRITICAL ALERT] System compromised!"
#          Print the list of breached ports.
#          Print the total failed login count.
#      Else:
#          Print "[INFO] System secure. No threats detected."
#
# ------------------------------------------------------------------------------
# WRITE YOUR UPGRADED CODE BELOW:
# ==============================================================================

FORBIDDEN_PORT = 4444
MAX_ALLOWED_FAILURES = 3
failed_logins = 0
failed_logins_ports =[]
breached_ports = []
network_stream = [
    (80, "Success"),
    (4444, "Success"),  # ATTACKER 1: Backdoor breach!
    (22, "Failed"),     # Failed login 1
    (443, "Success"),
    (9999, "Success"),  # ATTACKER 2: Another forbidden port! (Let's catch this too)
    (80, "Failed"),     # Failed login 2
    (80, "Failed")      # Failed login 3 (Max failures reached!)
]
for port, status in network_stream:
    if port == FORBIDDEN_PORT or port == 9999:
        if status == "Success":
            breached_ports.append(port)
    if status == "Failed":
        failed_logins += 1
        failed_logins_ports.append(port)
if breached_ports or failed_logins >= MAX_ALLOWED_FAILURES:
    print("[CRITICAL ALERT] System compromised!")
    if breached_ports:
        print(f"The number of breached ports are: {len(breached_ports)} and They are: {breached_ports}")
    if failed_logins:
        print(f"The number of failed logins are: {failed_logins} and They are: Ports {failed_logins_ports}")
else:
    print("[INFO] System secure. No threats detected.")