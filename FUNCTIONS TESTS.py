# ==============================================================================
# FUNCTION TEST 1: THE AUTOMATED IP SANITIZER
# ------------------------------------------------------------------------------
# SCENARIO: Clean messy network logs by stripping trailing/leading whitespaces.
#
# TASKS:
# 1. Define a function named 'clean_ip_address' that accepts a single parameter
#    named 'raw_ip'.
# 2. Inside the function, strip the whitespace from the string.
# 3. Use 'return' to send the cleaned IP string back out.
# ==============================================================================

# [WRITE YOUR TEST 1 FUNCTION HERE]
def clean_ip_address(raw_ip):
    cleaned_ip = raw_ip.strip(" ")
    return cleaned_ip

# Pipeline Execution:
messy_input = "   192.168.1.105   "
sanitized_result = clean_ip_address(messy_input)

print("-----TEST 1-----")
print(f"Sanitized IP Output: '{sanitized_result}'\n\n")



# ==============================================================================
# FUNCTION TEST 2: THE THREAT MULTIPLIER CALCULATOR
# ------------------------------------------------------------------------------
# SCENARIO: You are writing a calculator that scores vulnerability risks.
#           It accepts multiple numeric values and calculates an exploit score.
#
# TASKS:
# 1. Define a function named 'calculate_exploit_score' that accepts exactly
#    two parameters: 'base_severity' and 'multiplier'.
# 2. Inside the function, multiply 'base_severity' by 'multiplier'.
# 3. Return the final product integer back to the pipeline.
# ==============================================================================

# [WRITE YOUR TEST 2 FUNCTION HERE]

def calculate_exploit_score(base_severity, multiplier):
    calculation = base_severity * multiplier
    return calculation

# Pipeline Execution:
score_1 = calculate_exploit_score(8, 3)
score_2 = calculate_exploit_score(5, 4)

print("-----TEST 2-----")
print(f"Calculated Score 1: {score_1}")
print(f"Calculated Score 2: {score_2}\n\n")


# ==============================================================================
# FUNCTION TEST 3: THE AUTOMATED PORT MONITOR WITH DEFAULT CONFIGS
# ------------------------------------------------------------------------------
# SCENARIO: You want a function that formats network connection logs. By default,
#           most administrative traffic goes over Port 22, but your function
#           must allow other ports to be passed in optionally.
#
# TASKS:
# 1. Define a function named 'format_connection_log' that accepts two parameters:
#    - 'ip_address' (a standard parameter)
#    - 'port' (a DEFAULT parameter pre-set to the integer 22)
# 2. Inside the function, use an f-string to return a string message matching
#    this exact structural layout: "ALERT: Connection from {ip_address} on port {port}"
# 3. Use 'return' to send that string payload back out.
# ==============================================================================

# [WRITE YOUR TEST 3 FUNCTION HERE]
def format_connection_log(ip_address, port=22):
    message = f"ALERT: Connection from {ip_address} on port {port}"
    return message

# Pipeline Execution:
# Run 1: Utilizing the default port value
log_alpha = format_connection_log("192.168.1.50")

# Run 2: Overriding the default port with a custom value
log_beta = format_connection_log("10.0.0.12", 443)

print("-----TEST 3-----")
print(log_alpha)
print(f"{log_beta}\n\n")


# ==============================================================================
# FUNCTION TEST 4: THE MALICIOUS LOG FILTER APPLIANCE
# ------------------------------------------------------------------------------
# SCENARIO: You want to build a reusable filtering tool. It must accept a raw list
#           of log statuses and return a clean, processed list of only the failures.
#
# TASKS:
# 1. Define a function named 'filter_malicious_logs' that accepts a single
#    parameter named 'log_list'.
# 2. Inside the function, initialize an empty evidence list named 'failures'.
# 3. Write a 'for' loop to iterate through the incoming 'log_list'.
# 4. If a log string equals "failed", append it to your 'failures' list.
# 5. Use 'return' to send the completed 'failures' list back out of the function.
# ==============================================================================

# [WRITE YOUR TEST 4 FUNCTION HERE]
def filter_malicious_logs(raw_traffic_logs):
    failures = []
    for logs in raw_traffic_logs:
        all_logs = logs.lower()
        if all_logs == "failed":
            failures.append(all_logs)
    return failures

# Pipeline Execution:
raw_traffic_logs = ["success", "failed", "success", "failed", "failed", "success"]
isolated_threats = filter_malicious_logs(raw_traffic_logs)

print("-----TEST 4-----")
print(f"Isolated Threats List: {isolated_threats}\n\n")


# ==============================================================================
# FUNCTION TEST 5: THE ASSET SECURITY VERDICT GATING
# ------------------------------------------------------------------------------
# SCENARIO: You are building an access gating mechanism. The function receives
#           a complete user account dictionary and evaluates their privilege level.
#
# TASKS:
# 1. Define a function named 'is_admin_account' that accepts a single parameter
#    named 'user_dict'.
# 2. Inside the function, extract the value inside the key "role".
# 3. Write a condition: If the role equals the string "Administrator",
#    return the boolean True.
# 4. Otherwise, return the boolean False.
# ==============================================================================

# [WRITE YOUR TEST 5 FUNCTION HERE]

def is_admin_account(user_dict):
    safe_user_dict = user_dict["role"].lower()
    if safe_user_dict == "administrator":
        scan = f"{user_dict["username"]} is an Administrator"
        return scan, True

    else:
        scan = f"{user_dict['username']} is not Administrator but {user_dict["role"]}"
        return scan, False


# Pipeline Execution:
account_alpha = {"username": "vlad_ops", "role": "Administrator", "dept": "IT"}
account_beta = {"username": "jane_clerk", "role": "Guest", "dept": "Finance"}

verdict_alpha = is_admin_account(account_alpha)
verdict_beta = is_admin_account(account_beta)


print("-----TEST 5-----")
print(f"Account Alpha Admin Status: {verdict_alpha}")
print(f"Account Beta Admin Status: {verdict_beta}\n\n")


# ==============================================================================
# FUNCTION TEST 6: THE CENTRAL LOG COUNT ENRICHMENT ENGINE
# ------------------------------------------------------------------------------
# SCENARIO: You are writing an auditing tool that flags suspicious logins. Every
#           time a login fails, your function must append the user to an evidence
#           list and track the global damage counter.
#
# TASKS:
# 1. Define a function named 'process_security_event' that accepts exactly
#    three parameters: 'user', 'status', and 'evidence_list'.
# 2. Inside the function, write a condition: If the 'status' string equals
#    the value "failed", use a list method to append 'user' to the 'evidence_list'.
# 3. Use 'return' to send the updated 'evidence_list' object back to the main script.
# ==============================================================================

# [WRITE YOUR TEST 6 FUNCTION HERE]
def process_security_event(user, status, evidence_list = []):
    # evidence_list = []
    safe_status = status.lower()
    if safe_status == "failed":
        evidence_list.append(user)
    return evidence_list


# Pipeline Execution:
threat_roster = []

# Event 1: Normal user login succeeds
threat_roster = process_security_event("alex_dev", "success", threat_roster)

# Event 2: Attacker fails a login
threat_roster = process_security_event("hacker_bot_1", "failed", threat_roster)

# Event 3: Another attacker fails a login
threat_roster = process_security_event("unknown_guest", "failed", threat_roster)

print("-----TEST 6-----")
print(f"Final Global Threat Roster: {threat_roster}")
print(f"Total High-Risk Events Documented: {len(threat_roster)}\n\n")


# ==============================================================================
# FUNCTION TEST 7: THE FIREWALL ACL RULE GENERATOR
# ==============================================================================
# SCENARIO: You are building an automated Access Control List (ACL) system.
#           Your tool takes raw networking parameters and wraps them into a
#           standard terminal command string that can be pushed to a firewall router.
#
# GOAL: Architect a function named 'generate_acl_rule' that takes an IP and a
#       port, formats them into a clean rule string, and returns it.
#       - If the port is exactly 80 or 443, the action is "ALLOW".
#       - For any other port, the action is "DENY".
#       - The function must return an f-string formatted precisely as:
#         "RULE SET: {action} traffic from {ip_address} on port {port_num}"
# ==============================================================================

# [ARCHITECT YOUR FUNCTION SEVEN BELOW]
def generate_acl_rule(ip_address, port_num):
    if port_num == 80 or port_num == 443:
        action = "ALLOW"
        router_rule = f"RULE SET: {action} traffic from {ip_address} on port {port_num}"
        return router_rule

    else:
        action = "DENY"
        router_rule = f"RULE SET: {action} traffic from {ip_address} on port {port_num}"
        return router_rule

# Pipeline Execution Values:
rule_alpha = generate_acl_rule("192.168.1.25", 443)
rule_beta = generate_acl_rule("45.33.22.11", 22)
rule_gamma = generate_acl_rule("10.0.0.55", 80)

print("-----TEST 7-----")
print(rule_alpha)
print(rule_beta)
print(f"{rule_gamma}\n\n")


# ==============================================================================
# FUNCTION TEST 8: THE LIVE BULK INTEL SCANNER
# ==============================================================================
# SCENARIO: You are writing a core function for a threat assessment pipeline.
#           The function receives a list of raw network packet dictionaries and
#           must dynamically extract indicators.
#
# GOAL: Architect a function named 'scan_network_traffic' that accepts a single
#       parameter representing a list of packets.
#       - Inside the function, evaluate each packet dictionary.
#       - If a packet has a key "type" equal to "Malicious", look up its "risk"
#         integer score.
#       - If that "risk" score is greater than 7, extract the "source" IP string
#         and collect it into an internal evidence list.
#       - Your function must return the final evidence list of flagged IPs.
# ==============================================================================

# [ARCHITECT YOUR FUNCTION EIGHT BELOW]
def scan_network_traffic(list_of_packets):
    evidence_list = []
    for packets in list_of_packets:
        packets_type_case = packets["type"].lower()
        if packets_type_case == "malicious":
            if packets["risk"] > 7:
                




# Pipeline Execution Values:
traffic_batch = [
    {"source": "192.168.1.50", "type": "Safe", "risk": 2},
    {"source": "45.33.22.11", "type": "Malicious", "risk": 9},
    {"source": "10.0.0.12", "type": "Safe", "risk": 1},
    {"source": "185.220.101.5", "type": "Malicious", "risk": 8},
    {"source": "192.168.1.200", "type": "Malicious", "risk": 5}
]

flagged_threats = scan_network_traffic(traffic_batch)

print("-----TEST 8-----")
print(f"Flagged Threat IPs: {flagged_threats}")
