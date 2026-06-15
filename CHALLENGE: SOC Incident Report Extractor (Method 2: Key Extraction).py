# ==============================================================================
# CHALLENGE: SOC Incident Report Extractor (Method 2: Key Extraction)
# ==============================================================================
#
# #### THE SCENARIO
# A high-priority security alert has been triggered by your firewall. The SIEM
# has generated a pre-built JSON data packet (stored below as 'incident_report').
#
# Your job as a Security Automation Engineer is to write a script that digs into
# this specific pre-built dictionary and extracts key pieces of evidence for the
# human analysts.
#
# #### THE RULES
# 1. Do NOT loop through the whole packet to count items. This data is already pre-built.
# 2. Use direct key lookup with square brackets (e.g., dictionary["key"]) to grab the data.
# 3. Save the requested pieces of data into the four specific variables provided below.
#
# #### YOUR SPECIFIC GOALS (Extract these 4 items):
# - Goal 1: Get the 'severity' level of the incident.
# - Goal 2: Get the 'target_ip' that was attacked.
# - Goal 3: Get the FIRST malicious domain name listed in the indicators list.
# - Goal 4: Get the 'status' code of the firewall response.
# ==============================================================================

# Pre-built JSON data packet from the SIEM
incident_report = {
    "incident_id": "INC-2026-8891",
    "severity": "CRITICAL",
    "details": {
        "attacker_origin": "Unknown",
        "target_ip": "10.0.4.15",
        "firewall_response": {
            "action_taken": "BLOCKED",
            "status": "SUCCESS_CODE_200"
        }
    },
    "threat_intel": {
        "malware_family": "Ransomware.LockBit",
        "indicators": ["bad-domain.xyz", "malicious-site.com", "hacker-cnc.net"]
    }
}

extracted_severity = incident_report["severity"]
extracted_target_ip = incident_report["details"]["target_ip"]
extracted_first_domain = incident_report["threat_intel"]["indicators"][0]
extracted_firewall_status = incident_report["details"]["firewall_response"]["status"]

print(f"Severity Level:  {extracted_severity}")
print(f"Target IP Address: {extracted_target_ip}")
print(f"First Bad Domain:  {extracted_first_domain}")
print(f"Firewall Status:   {extracted_firewall_status}")
