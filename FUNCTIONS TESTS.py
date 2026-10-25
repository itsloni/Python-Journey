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
print(log_beta)


