# ULTIMATE CAPSTONE: INDUSTRIAL SIEM LOG ANALYSER
#
# CONTEXT: Security Information and Event Management (SIEM) systems read massive
# text logs from servers all over the world. Your script needs to analyze a log string,
# look for security threat keywords, extract the server status, and determine an action.
#
# INSTRUCTIONS:
# 1. Create a function named analyze_siem_log that takes one parameter: log_message (a string).
# 2. Inside the function, define a list named threat_keywords containing: "exploit", "malware", "bruteforce".
# 3. Clean and break down the input log_message:
#    - Convert the entire log_message to lowercase.
#    - Split the log_message into a list of individual words named log_words.
# 4. Use a list comprehension to check each word in log_words. If a word is in threat_keywords,
#    keep it. This will create a list of found threats named detected_threats.
# 5. Create a boolean variable named is_threat_detected. It should be True if your
#    detected_threats list contains one or more items, and False if the list is empty.
# 6. Create a boolean variable named is_server_down. Check if the exact phrase "status_offline"
#    exists anywhere inside the original log_raw string.
# 7. Determine a final string variable named system_action:
#    - If a threat IS detected AND the server IS down, set it to "DISPATCH_INCIDENT_RESPONSE_TEAM".
#    - If a threat IS detected BUT the server IS NOT down, set it to "ISOLATE_SERVER_NODE".
#    - If NO threat is detected BUT the server IS down, set it to "REBOOT_HARDWARE_SYSTEM".
#    - For any other situation, set it to "CONTINUE_MONITORING".
# 8. Return all THREE results simultaneously: is_threat_detected, is_server_down, and system_action.
# 9. Outside the function, test your code by calling analyze_siem_log with this exact string:
#    "CRITICAL: An exploit attempt was detected on server main and now status_offline is triggered."
# 10. Unpack the three returned values into separate variables and print them out.

def analyze_siem_log(log_message):
    threat_keywords = ["exploit", "malware", "bruteforce"]

    log_message= log_message.lower()
    log_words = log_message.split(" ")


    detected_threats = [word for word in log_words if word in threat_keywords]

    is_threat_detected = len(detected_threats) > 0
    is_server_down = "status_offline" in log_message

    if is_threat_detected == True and is_server_down == True:
        system_action = "DISPATCH_INCIDENT_RESPONSE_TEAM"
    elif is_threat_detected and not is_server_down:
        system_action = "ISOLATE_SERVER_NODE"
    elif not is_threat_detected and is_server_down:
        system_action = "REBOOT_HARDWARE_SYSTEM"
    else:
        system_action = "CONTINUE_MONITORING"


    return is_threat_detected, is_server_down, system_action
threat_presence, server_condition, system_response = analyze_siem_log("CRITICAL: An exploit attempt was detected on server main and now status_offline is triggered.")
print(threat_presence, end=" ")
print(server_condition, end=" ")
print(system_response)