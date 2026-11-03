#
# CHALLENGE 1: Pure Functions & Input Verification
#
# Prompt: Write a standalone Python function that accepts a string input representing a
# network packet size in bytes. The function must safely convert this input to an integer
# to verify if it is a safe size. If the size is over 1500 bytes, it should flag it as an
# abnormal packet. It must handle situations gracefully where a user inputs a non-numeric
# string (like text) without crashing the program, treating invalid inputs as size 0.
# Test your function with the invalid string input "MALFORMED_DATA".
#
def network_packet(packet_size):
    if packet_size.isdigit():
        packet_size_int = int(packet_size)
        if packet_size_int == 0 or packet_size_int > 1500:
            abnormal = f"This Packet is an abnormal/Invalid Packet"
            return abnormal
        


user_input = input("Enter Packet size: ")
print(network_packet(user_input))