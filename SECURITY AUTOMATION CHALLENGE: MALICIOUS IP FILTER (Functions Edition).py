# SECURITY AUTOMATION CHALLENGE: MALICIOUS IP FILTER
#
# CONTEXT: You are building an automated script to parse incoming network traffic.
# Your task is to write a function that screens an IP address against a list of
# known malicious IPs and checks if the connection attempt exceeds safe limits.
#
# INSTRUCTIONS:
# 1. Create a function named check_ip_security that takes two parameters: ip_address and connection_count.
# 2. Inside the function, define a list named malicious_ips containing at least 3 dummy malicious IP strings.
# 3. Determine if the input ip_address exists inside your malicious_ips list (Save this True/False result).
# 4. Check if the connection_count is strictly greater than 100 attempts (Save this True/False result).
# 5. Determine a final security action string:
#    - If it is malicious OR over 100 attempts, set the action to "BLOCK_TRAFFIC".
#    - Otherwise, set the action to "ALLOW_TRAFFIC".
# 6. Return all THREE results simultaneously from the function: the malicious check, the count check, and the action string.
# 7. Outside the function, call check_ip_security using an IP and a count of your choice.
# 8. Unpack the three returned values into three separate variables.
# 9. Print each variable on its own line to verify the automation logic runs correctly.

def check_ip_security(ip_address, connection_count):
    malicious_ips = ["192.168.1.50", "10.0.0.99", "172.16.254.1"]

    is_malicious = ip_address in malicious_ips
    is_over_limit = int(connection_count) > 100

    if is_malicious or is_over_limit:
        action = "BLOCK_TRAFFIC"
    else:
        action = "ALLOW_TRAFFIC"

    return is_malicious, is_over_limit, action

is_bad_ip, is_over_count, final_action = check_ip_security("192.168.1.50", 1000)

print(is_bad_ip, end=" ")
print(is_over_count, end=" ")
print(final_action)



