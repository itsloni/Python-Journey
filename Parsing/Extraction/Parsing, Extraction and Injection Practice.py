# ==============================================================================
# CHALLENGE 1: THE ACTIVE APPLIANCE ROTATION TIMELINE
# ------------------------------------------------------------------------------
# SCENARIO: You are managing a list of primary firewall device hostnames.
#
# TASKS:
# 1. Slice the 'firewalls' list to extract the first 3 items and store them
#    in a new list named 'legacy_zone'.
# 2. Insert the string "NGFW_Core_Secure" at the very front (Index 0) of the
#    original 'firewalls' list.
# 3. Append the string "Cloud_WAF_05" to the very end of 'firewalls'.
# 4. Use a list method to completely clear out the 'temporary_buffer' list.
# ==============================================================================
from asyncio import log

firewalls = ["FW_Edge_01", "FW_Internal_02", "FW_DMZ_03", "FW_Backup_04"]
temporary_buffer = ["Packet_Dump_A", "Packet_Dump_B"]

# [WRITE YOUR CHALLENGE 1 CODE HERE]
legacy_zone = []
#legacy_zone = firewalls[:3] # You can actually just create the new extracted list directly without creating an empty list first.
# legacy_zone.append(firewalls[0:3]) # This will extract the list but also extract the bracket of the list which turns the new list created a nested list.
legacy_zone.extend(firewalls[0:3]) # Use .extend() when you're extracting directly from a list into another list so it's flat.
#[hostname for hostnames in firewalls if hostnames != firewalls[3]] # I don't know how to use this comprehension lol.

firewalls.insert(0,"NGFW_Core_Secure")
firewalls.append("Cloud_WAF_05")
temporary_buffer.clear()

print("--- CHALLENGE 1 RESULTS ---")
print(f"Legacy Zone: {legacy_zone if 'legacy_zone' in locals() else 'Not Found'}")
print(f"Updated Firewalls: {firewalls}")
print(f"Cleared Buffer: {temporary_buffer}\n\n")

# ==============================================================================
# CHALLENGE 2: THE SECURE METADATA OVERHAUL
# ------------------------------------------------------------------------------
# SCENARIO: You receive an unorganized single endpoint log artifact.
#
# TASKS:
# 1. Update the existing key "threat_level" to the uppercase string "HIGH".
# 2. Create a brand-new key in the 'log_entry' dictionary called "identity_block".
# 3. Set the value of "identity_block" to a new dictionary dynamically extracting
#    root values:
#    - "user" must pull the value stored in the root-level key "raw_user".
#    - "ip" must pull the value stored in the root-level key "raw_ip".
# 4. Permanently delete the messy root-level keys "raw_user" and "raw_ip".
# ==============================================================================

log_entry = {
    "artifact_id": "ART_7721",
    "threat_level": "medium",
    "raw_user": "malicious_actor_x",
    "raw_ip": "185.220.101.9"
}

# [WRITE YOUR CHALLENGE 2 CODE HERE]

log_entry["threat_level"] = "HIGH"
log_entry["identity_block"] = {
    "user" : log_entry["raw_user"],
    "ip" : log_entry["raw_ip"]
}
del log_entry["raw_user"]
del log_entry["raw_ip"]

print("--- CHALLENGE 2 RESULTS ---")
print(f"Overhauled Log Entry: {log_entry}\n\n")


# ==============================================================================
# CHALLENGE 3: WILD CARD HEADER & HARDENING CASTING
# ------------------------------------------------------------------------------
# SCENARIO: You process static authentication tokens and raw streaming payloads.
#
# TASKS:
# 1. Use Tuple Unpacking with a wildcard star (*) to split 'raw_payload'.
#    - Assign the first item to 'event_id'.
#    - Assign the second item to 'status_code'.
#    - Capture all remaining variable items into a list named 'trailing_hex_data'.
# 2. Convert the mutable list 'approved_operators' into a completely hardened,
#    unchangeable tuple named 'immutable_whitelist'.
# ==============================================================================

raw_payload = ("EVNT_4002", 200, "0x4A", "0xBF", "0x12", "0xEE")
approved_operators = ["sys_admin_dee", "security_bot_01", "soc_lead_vlad"]

# [WRITE YOUR CHALLENGE 3 CODE HERE]

event_id, status_code, *trailing_hex_data = raw_payload
immutable_whitelist = tuple(approved_operators)

print("--- CHALLENGE 3 RESULTS ---")
print(f"Event ID: {event_id if 'event_id' in locals() else 'Not Found'}")
print(f"Status Code: {status_code if 'status_code' in locals() else 'Not Found'}")
print(f"Trailing Hex: {trailing_hex_data if 'trailing_hex_data' in locals() else 'Not Found'}")
print(f"Hardened Whitelist Type: {type(immutable_whitelist) if 'immutable_whitelist' in locals() else 'Not Found'}")
print(f"Hardened Whitelist Content: {immutable_whitelist if 'immutable_whitelist' in locals() else 'Not Found'}\n\n")


# ==============================================================================
# CHALLENGE 4: THE THREAT TIMELINE EMBEDDED PIPELINE
# ------------------------------------------------------------------------------
# SCENARIO: You parse an enterprise alert dict payload containing a history list.
#
# TASKS:
# 1. Loop through the list stored inside 'alert_packet' under "incident_history".
# 2. Use Mosh's Loop Header Unpacking Shortcut to unpack each inner tuple
#    directly inside the 'for' loop declaration line into: 'timestamp', 'port', and 'is_malicious'.
# 3. Inside the loop, check the condition: If 'is_malicious' is True AND the
#    'port' is exactly 22, append the 'timestamp' string to 'quarantine_timestamps'.
# 4. OUTSIDE the loop entirely, check your evidence list. If 'quarantine_timestamps'
#    holds 2 or more elements, change the 'global_lockdown' flag to True.
# ==============================================================================

alert_packet = {
    "sensor_node": "AWS_US_EAST_01",
    "incident_history": [
        ("01:15:00", 22, True),
        ("01:18:22", 443, False),
        ("01:20:45", 22, True),
        ("01:25:10", 80, True)
    ]
}


quarantine_timestamps = []
global_lockdown = False

# [WRITE YOUR CHALLENGE 4 CODE HERE]
for history in alert_packet['incident_history']:
timestamp = history[0]
port = int(history[1])
is_malicious = history[2]
print(timestamp)


#
# print("--- CHALLENGE 4 RESULTS ---")
# print(f"Quarantine Timestamps: {quarantine_timestamps}")
# print(f"GLOBAL LOCKDOWN ACTIVE: {global_lockdown}\n\n")


# ==============================================================================
# CHALLENGE 5: THE GRAND POTLUCK NESTED ATTACK DICTIONARY MAPPER
# ------------------------------------------------------------------------------
# SCENARIO: You are tracking a "potluck" list of attack tuples containing:
#           (attacker_ip, targeted_port).
#
# TASKS:
# 1. Loop through the 'alert_potluck' list and unpack the tuples directly into
#    independent variables 'ip' and 'port'.
# 2. Inside the loop, check if the 'ip' is NOT currently a key in your
#    'reconnaissance_map' dictionary. If it is a brand-new IP, initialize a nested
#    dictionary for it matching this exact blueprint:
#    reconnaissance_map[ip] = {"hit_count": 0, "attacked_ports": []}
# 3. For EVERY hit (whether it's a new IP or an existing one), dynamically update
#    that specific IP's inner tracking data:
#    - Increment its nested "hit_count" by 1.
#    - Append the current 'port' string into its nested "attacked_ports" list.
# ==============================================================================

alert_potluck = [
    ("45.33.22.11", "Port_22"),
    ("185.220.101.5", "Port_443"),
    ("45.33.22.11", "Port_80"),
    ("192.168.1.100", "Port_3389"),
    ("45.33.22.11", "Port_22")
]

reconnaissance_map = {}

# [WRITE YOUR CHALLENGE 5 CODE HERE]



#
# print("--- CHALLENGE 5 RESULTS ---")
# import json
# print(json.dumps(reconnaissance_map, indent=4))
# ==============================================================================
