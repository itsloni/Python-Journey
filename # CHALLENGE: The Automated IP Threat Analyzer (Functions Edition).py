# ==============================================================================
# CHALLENGE: The Automated IP Threat Analyzer (Functions Edition)
# ==============================================================================
#
# #### THE SCENARIO
# You are writing a reusable Python tool for a SOAR playbook. Instead of writing
# code that only works on one specific list, you need to build a reusable function.
#
# Your function must accept a list of logs, sieve through them to find the
# MALICIOUS IPs, filter out any duplicates, and return a clean summary dictionary.
#
# #### THE RULES
# 1. Define a function named 'analyze_threats' that accepts ONE parameter (the log list).
# 2. Inside the function, use a loop to find strings starting with "MALICIOUS_".
# 3. Prevent duplicates! Only add each malicious IP to your tracking list once.
# 4. Your function must RETURN a dictionary structured exactly like this:
#    {"status": "ALERT", "malicious_hosts": [the clean list of bad IPs]}
# 5. Do NOT use set() or hardcode any values. Use your dynamic list/dict methods!
#
# #### EXPECTED OUTPUT
# When you pass the test logs into your function and print the result, it must look like this:
# {'status': 'ALERT', 'malicious_hosts': ['MALICIOUS_185.220.101.5', 'MALICIOUS_45.146.164.22']}
# ==============================================================================

# Raw logs feeding into the automation platform


# --- YOUR CODE GOES HERE ---
# 1. Use 'def' to create your function named analyze_threats
# 2. Write your loop and bucket logic inside the function
# 3. Use the 'return' keyword to send back the final dictionary summary



def analyze_threats(log_list):
    tracking_list = {
                    "status": "ALERT",
                    "malicious_hosts": []
                }
    for ip in log_list:
        if ip.startswith("MALICIOUS_"):
            if ip not in tracking_list["malicious_hosts"]:
                tracking_list["malicious_hosts"].append(ip)

    return tracking_list

firewall_logs = [
        "192.168.1.50", "MALICIOUS_185.220.101.5", "172.16.0.5",
        "MALICIOUS_45.146.164.22", "192.168.1.50", "MALICIOUS_185.220.101.5"
    ]
automation_result = analyze_threats(firewall_logs)
print(automation_result)



# This line runs your function using the firewall_logs and prints the output

