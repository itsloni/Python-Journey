# ==============================================================================
# 🧠 THE MULTI-LAYER INCIDENT RESPONSE CHALLENGE
# ==============================================================================
#
# YOUR GOAL:
# Write an automated network monitor using a 'while' loop. Inside, use a
# 'for' loop to scan incoming network packets. If a critical threat is found,
# shut down the entire system using logical operators (and / or).
#
# ------------------------------------------------------------------------------
# ⚙️ THE LOGIC RULES (Your Blueprint)
# ------------------------------------------------------------------------------
#
# 1. TRACKING VARIABLES: Before any loops, create a tracker variable:
#    failed_logins = 0
#
# 2. THE OUTER SHELL: Create a boolean flag to keep your system running:
#    system_active = True
#    Use a 'while system_active:' loop to keep the monitor alive.
#
# 3. THE SCANNER: Inside the while loop, use a for loop to unpack the data:
#    for port, status in network_stream:
#
# 4. THE SECURITY ENGINE (Inside the for loop):
#    - RULE A: If port is equal to FORBIDDEN_PORT AND status is "Success",
#      a hacker breached the backdoor!
#    - RULE B: If status is equal to "Failed", add 1 to your failed_logins counter.
#      Then check if failed_logins is >= MAX_ALLOWED_FAILURES.
#
# 5. THE KILL SWITCH: If Rule A OR Rule B is triggered:
#    - Print a critical emergency warning.
#    - Set system_active = False (to stop the while loop).
#    - Use 'break' to instantly exit the for loop.
#
# 6. THE CLEARANCE: Attach an 'else:' block directly to your inner 'for' loop.
#    If the loop finishes checking all packets safely without a break,
#    print: "[INFO] All packets cleared."
#    Then set system_active = False so the program closes cleanly.
#
# ------------------------------------------------------------------------------
# CODE BELOW THIS LINE:
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 📥 THE INPUTS (Your Configuration and Live Data)
# ------------------------------------------------------------------------------
#Configuration constants
system_active = True
FORBIDDEN_PORT = 4444
MAX_ALLOWED_FAILURES = 3
failed_logins = 0

# Simulated stream of incoming network events
# Each item is a tuple: (port_number, login_status)
network_stream = [
    (80, "Success"),
    (443, "Success"),
    (22, "Failed"),
    (80, "Success"),
    (4444, "Success"),  # Threat 1: Malicious backdoor port accessed successfully!
    (80, "Failed"),     # Threat 2: Failed login
    (80, "Failed"),     # Threat 3: Failed login
    (80, "Failed")      # Threat 4: Failed login (3rd failure!)
]
while system_active:
    for port, status in network_stream:
        if port == FORBIDDEN_PORT and status == "Success":
            print("Hacker Breacher Backdoor Successfully!")
            system_active = False
            break
        elif status == "Failed":
            failed_logins += 1
            if failed_logins >= MAX_ALLOWED_FAILURES:
                print("Failed Login")
                system_active = False
                break
    else:
        print("[INFO] All packets cleared.")
        system_active = False
