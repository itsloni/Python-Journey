# SECURITY AUTOMATION CHALLENGE: FIREWALL PORT SCAN DETECTOR
#
# CONTEXT: When hackers attack a network, they usually run a "port scan" to find
# open doors (ports). A safe network looks for unauthorized ports and flags users
# who try to access forbidden areas like port 22 (SSH) or port 3389 (Remote Desktop).
#
# INSTRUCTIONS:
# 1. Create a function named audit_port_access that takes two parameters: port_number and user_role.
# 2. Inside the function, define a list named forbidden_ports containing these integers: 22, 80, 3389.
# 3. Create a boolean variable named is_forbidden that checks if the input port_number exists inside forbidden_ports.
# 4. Create a boolean variable named is_admin_user that checks if the user_role is exactly equal to the string "admin".
# 5. Determine a final security verdict string named alert_level:
#    - If the port IS forbidden AND the user is NOT an admin user, set alert_level to "CRITICAL_ALERT".
#    - If the port IS forbidden BUT the user IS an admin user, set alert_level to "AUTHORIZED_ADMIN_ACCESS".
#    - For any other situation, set alert_level to "SAFE_TRAFFIC".
# 6. Return all THREE results simultaneously: is_forbidden, is_admin_user, and alert_level.
# 7. Outside the function, call audit_port_access using a port number of 22 and a role of "guest".
# 8. Unpack the three returned values into three separate variables.
# 9. Print the variables out to verify your security logic works properly.


def audit_port_access(port_number, user_role):
    forbidden_ports = [22, 80, 3389]

    is_forbidden = int(port_number) in forbidden_ports
    is_admin_user = user_role == "admin"

    if is_forbidden and not is_admin_user:
        alert_level = "CRITICAL_ALERT"
    elif is_forbidden and is_admin_user:
        alert_level = "AUTHORIZED_ADMIN_ACCESS"
    else:
        alert_level = "SAFE_TRAFFIC"

    return is_forbidden, is_admin_user, alert_level

forbidden, admin, risk = audit_port_access("22", "admin")
print(forbidden, end=" ")
print(admin, end=" ")
print(risk)