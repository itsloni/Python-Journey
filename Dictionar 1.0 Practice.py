# #  evaluating the risk profile of a single corporate server asset.
server_profile = {
    "hostname": "Finance_DB_Prod",
    "vulnerability_count": 4,
    "exposure_factor": 5
}

fate = server_profile["vulnerability_count"] * server_profile["exposure_factor"]

if fate > 15:
    server_profile["status"] = "CRITICAL"
else:
    server_profile["status"] = "MONITORED"

print(f"{server_profile}\n\n")

# The Mitigation Cleanup
firewall_profile = {
    "device_name": "Edge_Firewall_01",
    "vulnerability_count": 5,
    "patched_count": 3,
    "active_alert_id": "ALERT_9921"
}

firewall_profile["patched_count"] *= 2
firewall_profile["vulnerability_count"] -= 2
del firewall_profile["active_alert_id"]

print("--- CHALLENGE 1 RESULTS ---")
print(f"{firewall_profile}\n\n")

# Deep Identity Audit
user_profile = {
    "username": "security_analyst_dee",
    "access_details": {
        "clearance_level": "Top_Secret",
        "role": "Incident_Responder"
    }
}

if user_profile["access_details"]["clearance_level"] == "Top_Secret":
    user_profile["access_details"]["mfa_status"] = "ENFORCED"
else:
    user_profile["access_details"]["mfa_status"] = "OPTIONAL"

print("--- CHALLENGE 2 RESULTS ---")
print(f"{user_profile}\n\n")

#  Threat Intelligence Enrichment
# network_alert = {
#     "alert_id": "ALRT_881",
#     "source_ip": "185.220.101.5"
# }
#
# network_alert["threat_intel"] = {
#     "risk_score" : 8,
#     "malware_family" : "Ransomware"
# }
# print(network_alert)

# The Log Structural Overhaul
api_event = {
    "event_id": "EVNT_1042",
    "actor_user": "admin_vlad",
    "actor_role": "Super_Admin",
    "status": "Success"
}

api_event["identity_block"] = {
    "user" : api_event["actor_user"],
    "role" : api_event["actor_role"],
}
del api_event["actor_user"]
del api_event["actor_role"]

print(api_event)
