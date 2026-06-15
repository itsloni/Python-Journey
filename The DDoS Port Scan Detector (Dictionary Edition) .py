# ==============================================================================
# CHALLENGE: The DDoS Port Scan Detector (Dictionary Edition)
# ==============================================================================
#
# #### THE RULES
# 1. Count the occurrences of every single IP address using a dictionary tracker.
# 2. Any IP address that appears THREE (3) or more times is a threat.
# 3. Add those threat IPs into the final ddos_block_list.
#
# #### EXPECTED OUTPUT
# When printed, your ddos_block_list must look exactly like this:
# ['185.220.101.5', '192.168.1.50']
# ==============================================================================

packet_logs = [
    "192.168.1.50", "10.0.0.99", "185.220.101.5",
    "192.168.1.50", "185.220.101.5", "172.16.0.5",
    "185.220.101.5", "10.0.0.99", "192.168.1.50",
    "192.168.1.75"
]

# Step 1: Use this dictionary to count the IPs tracker = {}
ip_tracker = {}

# Step 2: Use this list for the final bad actors
ddos_block_list = []

# --- YOUR CODE GOES HERE ---
for logs in packet_logs:
    if logs not in ip_tracker:
        ip_tracker[logs] = 0
    ip_tracker[logs] += 1
for tracker_logs, number in ip_tracker.items():
    if number >= 3:
        ddos_block_list.append(tracker_logs)

print(ddos_block_list)
# --- END OF YOUR CODE ---

