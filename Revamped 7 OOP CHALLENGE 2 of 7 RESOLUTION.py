# CHALLENGE 2: Dictionary-Based Threat Lookups
#
# Prompt: Build an autonomous alert categorizer using a standalone function. The function
# should accept a threat type string. It must look up this threat type in a reference data
# structure containing known mapping categories (e.g., "phishing" maps to "Email Security",
# "ddos" maps to "Network Security", and "malware" maps to "Endpoint Security"). The function
# should return the correct category name, or return "Unknown Security Domain" if the threat
# isn't listed. Demonstrate it works by passing it a threat type.
#
# --------------------------------------------------------------------------------

def alert_categorizer(threat_type):
    


