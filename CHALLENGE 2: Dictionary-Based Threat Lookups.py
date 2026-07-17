# CHALLENGE 2: Dictionary-Based Threat Lookups
#
# Prompt: Build an autonomous alert categorizer using a standalone function. The function
# should accept a threat type string. It must look up this threat type in a reference data
# structure containing known mapping categories (e.g., "phishing" maps to "Email Security",
# "ddos" maps to "Network Security", and "malware" maps to "Endpoint Security"). The function
# should return the correct category name, or return "Unknown Security Domain" if the threat
# isn't listed. Demonstrate it works by passing it a threat type.



def lookup(word):
    word_case = word.lower()
    threat_reference_list = {
        "phishing": "Email Security",
        "ddos": "Network Security",
        "malware": "Endpoint Security"
     }
# Instead of you using the if/else and elif ... that's bulky use the code below instead.
#     if word_case == "phishing":
#         output = threat_reference_list["phishing"]
#     elif word_case == "ddos":
#         output = threat_reference_list["ddos"]
#     elif word_case == "malware":
#         output = threat_reference_list["malware"]
#     elif word_case == "exit":
#         exit()
#     else:
#         output = "Unknown Security Domain"
#     return output
    return threat_reference_list.get(word_case, "Unknown Security Domain")


while True:
    threat_input = input("What is the threat type? (or 'exit'): ").strip()
    if threat_input.lower() == "exit":
        print("Exited")
        break
    threat_type = lookup(threat_input)
    print(threat_type)