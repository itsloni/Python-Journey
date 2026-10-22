# TEST 1
# # 1. The data we collected from the server
open_ports = [80, 22, 3389, 443]
system_status = "SECURE"
checker = [ ]
for ports in open_ports:
    if ports == 3389:
        checker.append(ports)
        system_status = "COMPROMISED"
# # 4. The Final Report (This runs AFTER the loop is totally done)
print(f"Final Audit Result: port{checker} {system_status}")

#TEST 2
active_users = ["alex", "sarah", "RoOt", "blake"]
banned = []
alert_triggered = False

for user in active_users:
    user = user.lower()
    if user == "root":
        banned.append(user)
        alert_triggered = True

print(f"Security Alert Triggered: {alert_triggered} by banned user: {banned}")

#TEST 3
line_length = 8
divider_line = ""

for line in range(line_length):
    divider_line += "-"

print("SECURITY RE-AUDIT ALERT")
print(divider_line)

#TEST 4
active_users = ["Alex", "Admin_Sarah", "blake", "Dave_ADMIN"]
secure_report = []

for user in active_users:
    clean_user = user.lower()
    if "admin" in clean_user:
        mask = " "
        # Get the length of the original username
        name_length = len(user)
        for count in range(name_length):
            mask += "*"
        secure_report.append(mask)

    else:
        secure_report.append(user)

print(f"Public Secure Report: {secure_report}")

#TEST 5
login_logs = ["failed", "success", "failed", "failed", "success", "failed", "failed", "failed"]
failed_count = 0
account_locked = False

for attempts in login_logs:
    if attempts == "failed":
        failed_count += 1

    elif attempts == "success":
        failed_count = 0

if failed_count >= 3:
    account_locked = True


print(f"Total Failed Attempts: {failed_count}")
print(f"Account Locked Status: {account_locked}")

#TEST six
network_traffic = ["10.0.0.52", "192.168.1.100", "10.0.0.11", "45.33.22.11", "10.0.1.5"]
suspicious_ips = []
alert_triggered = False

for ip in network_traffic:
    if not ip.startswith("10."):
        suspicious_ips.append(ip)
        alert_triggered = True
if suspicious_ips:
    print(f"suspicious ip's are: {suspicious_ips}")

print(f"Alert Status: {alert_triggered}")
print(f"Suspicious IPs Found: {suspicious_ips}")

#TEST 7
# A list containing inner lists: [Username, IP Address, Security Level]
session_data = [
    ["alex_admin", "10.0.0.5", "Admin"],
    ["guest_user_1", "192.168.4.20", "Guest"],
    ["sarah_dev", "10.0.1.12", "Developer"],
    ["unknown_external", "45.33.22.11", "Guest"],
    ["guest_user_2", "10.0.0.99", "Guest"]
]
unauthorized_guests = []
isolation_required = False
# print(session_data[1][0])
for lists in session_data:

    lower = lists[1]
    lower1 = lists[2].lower()

    if lower1.startswith("guest") and not lower.startswith("10."):
            unauthorized_guests.append(lists[0])
if unauthorized_guests:
    isolation_required = True
    print(f"Unauthorized Guests: {unauthorized_guests}")
    print(f"System Isolation Required: {isolation_required}")
# # Write your nested list solution below!

# Test 7.2
login_records = [
    ["security_bot", "IT", 23],
    ["finance_manager_1", "Finance", 9],
    ["accountant_jane", "Finance", 19],
    ["dev_user_4", "Engineering", 21],
    ["billing_clerk_bill", "FINANCE", 22]
]

violators = []
audit_failed = False

for lists in login_records:
    department = lists[1].lower()
    login_hour = int(lists[2])
    if login_hour >= 18 and department == "finance":
        violators.append(lists[0])


if violators:
    audit_failed = True
    print(f"Audit Failed Status: {audit_failed}")
    print(f"Violators List: {violators}")
#
#



# Test7.3
#
vulnerability_report = [
    ["Web_Server_01", "Apache", 8, "Unpatched"],
    ["DB_Server_02", "PostgreSQL", 9, "Patched"],
    ["Mail_Gateway", "Exchange", 5, "Unpatched"],
    ["Backup_Node", "Linux_Kernel", 7, "Unpatched"],
    ["Proxy_Server", "Nginx", 4, "Patched"]
]

emergency_servers = []
system_wide_shutdown = False

for lists in vulnerability_report:
    risk_score = int(lists[2])
    patch_status = lists[3].lower()
    if risk_score >= 7 and  patch_status == "unpatched":
        emergency_servers.append(lists[0])

if len(emergency_servers) >= 2:
    system_wide_shutdown = True
    print(f"Emergency Servers: {emergency_servers}")
    print(f"System-Wide Shutdown Triggered: {system_wide_shutdown}")

# TEST 8
detected_attacks = ["Malware_Injection", "SQL_Injection", "DDoS_Attack"]
compiled_report = "The attacks found were: "

for attacks in detected_attacks:
    if attacks != detected_attacks[-1]:
        compiled_report += f"{attacks}, "
    else:
        compiled_report += f"and {attacks}"
print(compiled_report)

# List Practice 1
firewall_inventory = ["Internal_FW_01", "Legacy_FW_Alpha", "Edge_FW_02"]

firewall_inventory.insert(0, "DMZ_Gateway_Premium")
firewall_inventory.append("Core_FW_03")
firewall_inventory.remove("Legacy_FW_Alpha")

print(firewall_inventory)


#List Practice 2
event_timeline = ["User_Login", "File_Downloaded", "Malware_Executed", "System_Crash", "Logs_Cleared"]
incident_index = event_timeline.index("Malware_Executed")
pre_incident_timeline = event_timeline[:incident_index + 1]

print(f"Incident occurred at index: {incident_index}")
print(f"Isolated Timeline: {pre_incident_timeline}")

##List Practice 3
#
feed_alpha = ["Phishing_URL", "Exploit_ZeroDay", "Malicious_IP"]
feed_beta = ["Exploit_ZeroDay", "Bad_Domain", "Exploit_ZeroDay"]

all_indicators = feed_alpha + feed_beta
zeroday_count = all_indicators.count("Exploit_ZeroDay")

print(f"Combined Indicators: {all_indicators}")
print(f"Total ZeroDay Overlaps: {zeroday_count}")

# The Sanitized Audit Log 4
raw_logs = ["User_Login", "Domain_Controller_Alpha", "File_Access"]
sanitized_logs = raw_logs.copy()
sanitized_logs[1] = "HIDDEN_ASSET"

print(f"Original Raw Logs: {raw_logs}")
print(f"Sanitized Audit Logs: {sanitized_logs}")


# The Memory Buffer Flush five
packet_buffer = ["Packet_01", "Packet_02", "Packet_03", "Packet_04"]

packet_buffer_size = len(packet_buffer)
if packet_buffer_size >= 3:
    print("THRESHOLD EXCEEDED: FLUSHING MEMORY!")
    packet_buffer.clear()
elif packet_buffer_size <= 3:
    print("Buffer Safe.")

print(f"Final Packet Buffer State: {packet_buffer}")
