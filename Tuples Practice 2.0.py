#Tuples Test 1
#
network_socket = ("192.168.1.250", 443, "HTTPS")

ip, port, protocol = network_socket

print("-----CHALLENGE 1-----")
print(f"Targeting IP: {ip}")
print(f"Connecting on Port: {port}")
print(f"Using Protocol: {protocol}\n\n")
from logging import critical

#Tuples Test 1
#
system_config = ("Production_Server", "AES_256", "Port_22_Closed")

if system_config[1] == "AES_256":
    print("-----CHALLENGE 2-----")
    print(f"{"ENCRYPTION HARDENED"}\n\n")
else:
    print("-----CHALLENGE 2-----")
    print(f"{"WEAK CRYPTO DETECTED"}\n\n")

# TEST 3
#
log_payload = ("2026-10-12_01:35:00", "SIG_992", "DATA_CHUNK_A", "DATA_CHUNK_B", "HEX_VALUE_C")
timestamp, *raw_data_block = log_payload

print("-----CHALLENGE 3-----")
print(f"Isolated Timestamp: {timestamp}")
print(f"Data Block Packed: {raw_data_block}\n\n")


#TEST 4
#
alert_codes = ("ERR_401", "ERR_403", "ERR_200", "ERR_403", "ERR_CRITICAL", "ERR_403")

error_403_count = alert_codes.count("ERR_403")
critical_index = alert_codes.index("ERR_CRITICAL")

print("-----CHALLENGE 4-----")
print(f"ERR_403 total occurrences: {error_403_count}")
print(f"Critical error sits at index position: {critical_index}\n\n")

#TEST 5

admin_list = ["root_user", "sys_admin_vlad", "global_ops_dee"]

hardened_admins = tuple(admin_list)

print("-----CHALLENGE 5-----")
print(f"Hardened Secure Tuple: {hardened_admins}")
print(f"Data type verified: {type(hardened_admins)}\n\n") #First time using type
