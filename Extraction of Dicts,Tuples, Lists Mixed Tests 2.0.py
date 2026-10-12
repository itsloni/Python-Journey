#Test 1
#
# alert_payload = {
#     "alert_id": "ALRT_1092",
#     "severity": "HIGH",
#     "socket_connection": ("192.168.10.45", 8080, "TCP")
# }
#
# target_ip, port, protocol = alert_payload["socket_connection"]
#
# print(f"Extracted IP: {target_ip}")
# print(f"Extracted Port: {port}")
# print(f"Extracted Protocol: {protocol}")


# Test 2

monitored_endpoints = [
    {"hostname": "Workstation_01", "status": "Secure"},
    {"hostname": "Server_Prod_02", "status": "Under_Review"},
    {"hostname": "Gateway_Edge_03", "status": "Secure"}
]

monitored_endpoints[1]["hardened_config"] = ("MFA_REQUIRED", 90)



print(monitored_endpoints)
