#Test 1
alert_payload = {
    "alert_id": "ALRT_1092",
    "severity": "HIGH",
    "socket_connection": ("192.168.10.45", 8080, "TCP")
}

target_ip, port, protocol = alert_payload["socket_connection"]

print(f"Extracted IP: {target_ip}")
print(f"Extracted Port: {port}")
print(f"Extracted Protocol: {protocol}")


# Test 2
monitored_endpoints = [
    {"hostname": "Workstation_01", "status": "Secure"},
    {"hostname": "Server_Prod_02", "status": "Under_Review"},
    {"hostname": "Gateway_Edge_03", "status": "Secure"}
]

monitored_endpoints[1]["hardened_config"] = ("MFA_REQUIRED", 90)
print(monitored_endpoints)

# TEST 3
#
user_security_profile = {
    "username": "analyst_dee",
    "clearance": "L2",
    "recent_blocks": ["BLOCK_IP_45", "BLOCK_DOMAIN_XYZ"]
}

user_security_profile["recent_blocks"].append("BLOCK_MALWARE_URL")

print(user_security_profile)

#TEST 4
device_profile = {
    "node_id": "NODE_SWITCH_99",
    "location": "HQ_Rack_B",
    "network_settings": {
        "ip_address": "10.1.5.20",
        "subnet": "255.255.255.0",
        "legacy_protocol": "Telnet_Insecure"
    }
}

del device_profile["network_settings"]["legacy_protocol"]
#
# #or
# del does not work with .get()
# del device_profile.get("network_settings", {}).get("legacy_protocol") # This does not go with del its only used for reading like data no writing or deleting
print(device_profile)

# TEST FIVE
alert_packet = {
    "incident_id": "INC_8831",
    "severity": "CRITICAL",
    "connection_history": [
        ("192.168.1.12", 80, 1),
        ("45.33.22.11", 22, 5),
        ("10.0.0.55", 443, 2),
        ("185.220.101.5", 22, 4)
    ]
}

flagged_ips = []

for packets in alert_packet["connection_history"]:
    src_ip = packets[0]
    dst_port = packets[1]
    multiplier = packets[2]
    if dst_port == 22:
        flagged_ips.append(src_ip)

print(f"Flagged Intrusion IPs: {flagged_ips}")


#Test six
connection_logs = [
    {
        "connection_id": "CONN_01",
        "session_metadata": ["alex_admin", 443, 8200]
    },
    {
        "connection_id": "CONN_02",
        "session_metadata": ["guest_user", 80, 6000]
    },
    {
        "connection_id": "CONN_03",
        "session_metadata": ["vlad_dev", 443, 1200]
    },
    {
        "connection_id": "CONN_04",
        "session_metadata": ["unknown_actor", 443, 9500]
    }
]

exfiltration_suspects = []
quarantine_protocol_active = False
for logs in connection_logs:
    username, port_number, bytes_transferred = logs["session_metadata"]
    if port_number == 443:
        if bytes_transferred > 5000:
            exfiltration_suspects.append(username)

if len(exfiltration_suspects) > 0:
    quarantine_protocol_active = True

print(f"Exfiltration Suspects: {exfiltration_suspects}")
print(f"QUARANTINE PROTOCOL ACTIVE: {quarantine_protocol_active}")


num_converter = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
}
number = input("Input a number or multiple no's from 1 - 3: ")
output = " "
for num in  number:
        output += num_converter.get(num, "!") + " "
print(output)
#
#
# Test 7 on dictionaries
comment = input("input an emoji with colon ':' and brackets ')' or '(' :> ")
comment_word = comment.split(" ")
comment_converter = {
    ":)" : "happy",
    ":(" : "sad"
}

output = ""
for word in comment_word:
    output += comment_converter.get(word, "Huh?") + " "
print(output)





