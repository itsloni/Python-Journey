cloud_alerts = [
    {
        "server_name": "AWS_Prod_DB",
        "base_severity": 10,
        "network_tuple": ("192.168.1.50", True, 3)
    },
    {
        "server_name": "Public_Facing_Web",
        "base_severity": 8,
        "network_tuple": ("45.33.22.11", False, 4)
    },
    {
        "server_name": "Internal_HR_Portal",
        "base_severity": 5,
        "network_tuple": ("10.0.0.12", False, 2)
    },
    {
        "server_name": "Cloud_Gateway_01",
        "base_severity": 9,
        "network_tuple": ("185.220.101.5", False, 3)
    }
]

critical_breaches = []
minor_breaches = []
firewall_lockdown_active = False

for alert in cloud_alerts:
    alert_server_name = alert["server_name"]
    server_name = alert_server_name
    alert_severity = alert["base_severity"]
    severity = alert_severity
    alert_network_tuple = alert["network_tuple"]
    ip = alert_network_tuple[0]
    is_blocked = alert_network_tuple[1]
    multiplier = alert_network_tuple[2]

    if is_blocked == False:
        fate = severity * multiplier
        if fate >= 25:
            critical_breaches.append(server_name)
        elif fate < 25:
            minor_breaches.append(server_name)

if len(critical_breaches) > 0:
    firewall_lockdown_active = True

print(f"Critical Systems Leaking: {critical_breaches}")
print(f"Minor Vulnerabilities: {minor_breaches}")
print(f"FIREWALL AUTOMATED LOCKDOWN STATUS: {firewall_lockdown_active}")


