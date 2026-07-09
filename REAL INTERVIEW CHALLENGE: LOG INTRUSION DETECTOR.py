# REAL INTERVIEW CHALLENGE: LOG INTRUSION DETECTOR
#
# Scenario:
# You are protecting an API gateway. Hackers are trying to guess user passwords
# (Brute Force attack) or steal database access (SQL Injection).
#
# Your Task:
# Write a function called analyze_access_attempt that takes two inputs:
# a request_payload (string sentence) and a fail_count (integer or string).
#
# The Goals & Constraints:
# 1. If the request_payload contains the malicious SQL phrase "select * from", it is a high-risk security threat.
# 2. If the fail_count is 5 or more, it is a brute force threat.
# 3. The function must evaluate these threats and output whether an SQL attack was detected (True/False),
#    whether a brute force attack was detected (True/False), and a final mitigation action string:
#    - If BOTH threats are true, the action must be "PERMANENT_IP_BAN".
#    - If ONLY the SQL attack is true, the action must be "BLOCK_REQUEST".
#    - If ONLY the brute force attack is true, the action must be "TEMPORARY_LOCKOUT".
#    - If everything is clean, the action must be "ALLOW_ACCESS".
# 4. Return all three results from your function, unpack them outside, and print them.
#
# Test Data to use outside your function:
# - Test Payload: "SELECT * FROM users WHERE id = 1"
# - Test Fail Count: 6

def analyze_access_attempt(request_payload, fail_count):
    request_payload = request_payload.lower()

    malicious_phrase = "select * from" in request_payload
    brute_force = int(fail_count) >= 5

    if malicious_phrase and brute_force:
        action_response = "PERMANENT_IP_BAN"
    elif malicious_phrase and not brute_force:
        action_response = "BLOCK_REQUEST"
    elif not malicious_phrase and brute_force:
        action_response = "TEMPORARY_LOCKOUT"
    else:
        action_response = "ALLOW_ACCESS"

    return malicious_phrase, brute_force, action_response

request, count, action = analyze_access_attempt("SELECT * FROM users WHERE id = 1", "6")
print(request, end=" ")
print(count, end=" ")
print(action)


