#Tuples Test 1
#
# network_socket = ("192.168.1.250", 443, "HTTPS")
#
# ip, port, protocol = network_socket
#
# print(f"Targeting IP: {ip}")
# print(f"Connecting on Port: {port}")
# print(f"Using Protocol: {protocol}")
from logging import critical

#Tuples Test 1
#
# system_config = ("Production_Server", "AES_256", "Port_22_Closed")
#
# if system_config[1] == "AES_256":
#     print("ENCRYPTION HARDENED")
# else:
#     print("WEAK CRYPTO DETECTED")

# TEST 3
#
# log_payload = ("2026-10-12_01:35:00", "SIG_992", "DATA_CHUNK_A", "DATA_CHUNK_B", "HEX_VALUE_C")
# timestamp, *raw_data_block = log_payload
#
# print(f"Isolated Timestamp: {timestamp}")
# print(f"Data Block Packed: {raw_data_block}")


#TEST 4
#
# alert_codes = ("ERR_401", "ERR_403", "ERR_200", "ERR_403", "ERR_CRITICAL", "ERR_403")
#
# error_403_count = alert_codes.count("ERR_403")
# critical_index = alert_codes.index("ERR_CRITICAL")
# print(f"ERR_403 total occurrences: {error_403_count}")
# print(f"Critical error sits at index position: {critical_index}")

#TEST 5

admin_list = ["root_user", "sys_admin_vlad", "global_ops_dee"]

hardened_admins = tuple(admin_list)

print(f"Hardened Secure Tuple: {hardened_admins}")
print(f"Data type verified: {type(hardened_admins)}")
