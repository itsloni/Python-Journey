# CHALLENGE: Advanced SIEM Alert Generator (Nested Dictionary Edition)
# #### THE SCENARIO
# Your SOC (Security Operations Center) receives a raw feed of login attempts.
# Your job is to process these logs into a highly detailed security tracker.
# For every unique username, you need to track TWO things:
# 1. The total number of login attempts (an integer counter).
# 2. A list of the specific status results ("SUCCESS" or "FAILED").
#
# #### THE RULES
# 1. Use a single loop to process the raw login_logs list.
# 2. For each user, initialize a nested dictionary with "attempts" and "results".
# 3. For every log seen, increment their "attempts" by 1 and append the status
#    to their "results" list.
# 4. Do NOT use set() or hardcode any usernames.
# #### EXPECTED OUTPUT
# When you print user_tracker at the end, it must look exactly like this:
# {
#   'tunde_admin': {'attempts': 3, 'results': ['FAILED', 'FAILED', 'SUCCESS']},
#   'amara_soc': {'attempts': 2, 'results': ['SUCCESS', 'FAILED']},
#   'guest_user': {'attempts': 1, 'results': ['FAILED']}
# }
# Raw authentication logs from the domain controller
import pprint
login_logs = [
    ("tunde_admin", "FAILED"),
    ("amara_soc", "SUCCESS"),
    ("tunde_admin", "FAILED"),
    ("guest_user", "FAILED"),
    ("tunde_admin", "SUCCESS"),
    ("amara_soc", "FAILED")
]

user_tracker = {}

# --- YOUR CODE GOES HERE ---
for name, status in login_logs:
    if name not in user_tracker:
        user_tracker[name] = {
            "Attempt" : 0,
            "Results" : []
        }
    user_tracker[name]["Attempt"] += 1
    user_tracker[name]["Results"].append(status)
pprint.pprint(user_tracker, indent = 4)

# --- END OF YOUR CODE ---

