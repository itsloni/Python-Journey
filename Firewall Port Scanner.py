# The "Firewall Port Scanner" Challenge.
# This next cybersecurity challenge simulates a
# network firewall detecting unauthorized port scanning activity.
# Your Goal
# Write a loop that scans a list of network ports. Your firewall must look
# for a specific, dangerous signature: a specific forbidden port being hit,
# or too many total unusual ports accessed.
# #The Inputs (Your Data)'
# Test your loop logic against both feeds to ensure it adapts automatically.)
# The Logic Rules
# 1.)Loop through the active port_log list.
# 2.)If the loop encounters the forbidden port 4444,
# instantly print: [BLOCKED] Malicious port 4444 detected! Drop connection. and stop the loop (break).
# 3.)Use a Python for-else block so that if the loop completes scanning the entire list safely without hitting 4444,
# it prints: [SAFE] Network traffic cleared by Firewall.
FORBIDDEN_PORT = 4444 #(A common malicious backdoor port)
# DATA FEED A: Normal Network Traffic
#port_log = [80, 443, 22, 80, 443]
# DATA FEED B: Hacker Activity Detected!
port_log = [80, 443, 4444, 22]

for logs in port_log:
    if logs == FORBIDDEN_PORT:
        print("[BLOCKED] Malicious port 4444 detected! Drop connection.")
        break
else:
    print("[SAFE] Network traffic cleared by Firewall.")


