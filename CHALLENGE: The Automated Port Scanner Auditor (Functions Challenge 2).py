
network_inventory = [
    ("Web_Server_A", 443),
    ("File_Share", 21),
    ("Mail_Server", 22),
    ("Legacy_Router", 23),
    ("Web_Server_A", 443),
    ("File_Share", 21)
]

def audit_network(data_list):
    tracker = {
        "SECURE_HOSTS" : [],
        "UNSAFE_HOSTS" : [],
    }

    for data, port in data_list:
        if port == 21 or port == 23:
            if data not in tracker["UNSAFE_HOSTS"]:
                tracker["UNSAFE_HOSTS"].append(data)
        elif port == 22 or port == 443:
            if data not in tracker["SECURE_HOSTS"]:
                tracker["SECURE_HOSTS"].append(data)

    return tracker

audit_result = audit_network(network_inventory)
print(audit_result)
