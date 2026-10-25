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
    
    else:
        return False


# Pipeline Execution:
account_alpha = {"username": "vlad_ops", "role": "Administrator", "dept": "IT"}
account_beta = {"username": "jane_clerk", "role": "Guest", "dept": "Finance"}

verdict_alpha = is_admin_account(account_alpha)
verdict_beta = is_admin_account(account_beta)

print("-----TEST 5-----")
print(f"Account Alpha Admin Status: {verdict_alpha}")
print(f"Account Beta Admin Status: {verdict_beta}\n\n")


