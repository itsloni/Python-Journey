# CHALLENGE 1: Pure Functions & Input Verification
#
# Prompt: Write a standalone Python function that accepts a string input representing a
# network packet size in bytes. The function must safely convert this input to an integer
# to verify if it is a safe size. If the size is over 1500 bytes, it should flag it as an
# abnormal packet. It must handle situations gracefully where a user inputs a non-numeric
# string (like text) without crashing the program, treating invalid inputs as size 0.
# Test your function with the invalid string input "MALFORMED_DATA".


def packet_verifier(value):
    try:
       if value.isdigit():
            converted_packet = int(value)
            if converted_packet > 1500:
                action = "ABNORMAL packet!"
                return action
            elif converted_packet <= 1500:
                action = "NORMAL packet"
                return action
       elif value.lower() == "exit":
           exit()
       else:
           if not value.isdigit():
               raise ValueError

    except ValueError:
        error = "Invalid Input... size 0"
        return error
    except SystemExit:
        cancel = "Exited Successfully"
        return cancel
while True:
    network_packet = input("Enter your network Packet size in bytes: ")
    verified = packet_verifier(network_packet)
    if verified == "Exited Successfully":
        break
    else:
        print(verified)


