#  The PlotYou are investigating a potential Insider Threat (a malicious employee trying to steal corporate data).
#  A security agent has scraped a log of user activities from the company's file server.
#  Your job is to analyze this data stream and flag suspicious behavior.

#⚙️ The Security RulesYour script must process the activity_log stream and enforce these rules:
# 1.) The Exfiltration Rule: If any single employee performs a "Download" action on a "High" sensitivity
# file 3 or more times across the log, they must be flagged immediately as a data thief.

# 2.) The Clearance Rule: If the log is fully scanned and no employee breaches the Exfiltration Rule,
# the system must report that the internal network is clean.

# 3.) The Summary: Your program must print the names of any flagged employees,
# alongside the total number of high-sensitivity downloads they committed.


# The raw activity stream
# Format: (employee_name, action_performed, file_sensitivity_level)
activity_log = [
    ("Alice", "Login", "Low"),
    ("Bob", "Read", "Low"),
    ("Alice", "Read", "Medium"),
    ("Charlie", "Login", "Low"),
    ("Bob", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Bob", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Alice", "Download", "High"),
    ("Bob", "Download", "High"),
    ("Charlie", "Download", "Low"),
    ("Bob", "Download", "High")
]

#num__high_downloads = 0
data_thief = {}

for name, status, sensitivity in activity_log:
    if status == "Download" and sensitivity == "High":
        if name not in data_thief:
            data_thief[name] = 0
        data_thief[name] += 1
for name, violations in data_thief.items():
    if violations >= 3:
        print(f"Thief Detector: {name},{violations}")














# SHOWING MY GROWTH AS I INITIALLY HARDCODED MY WAY IN BUT AFTER HOURS FINALLY REALISED    TEH MISSING PIECE "DICTIONARIES"
# AND I CREATED A DATA DRIVEN AUTOMATIC INSIDER THREAT DETECTOR SOFTWARE.




  # num_Bob_high_downloads = 0
# num_charlie_high_downloads = 0
# num_alice_high_downloads = 0
# num_of_downloads = []
# data_thief = []

# num_individual = 0
# for individual, status, severity in activity_log:
#     if severity == "High" and status == "Download":
#         if individual == "Alice":
#             num_alice_high_downloads += 1
#             if num_alice_high_downloads >= 3:
#                 data_thief.append(individual)
#                 num_of_downloads.append(num_alice_high_downloads)
#         if individual == "Bob":
#             num_Bob_high_downloads += 1
#             if num_Bob_high_downloads >= 3:
#                 data_thief.append(individual)
#                 num_of_downloads.append(num_Bob_high_downloads)
#         if individual == "Charlie":
#             num_charlie_high_downloads += 1
#             if num_charlie_high_downloads >= 3:
#                 data_thief.append(individual)
#                 num_of_downloads.append(num_charlie_high_downloads)
# if data_thief:
#     print(f"The Data thief: {data_thief}  and the number of high-sensitivity downloads is {num_of_downloads}")
# else:
#     print("Internal Network is Clean.")

