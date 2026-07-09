# REAL INTERVIEW CHALLENGE: AUTOMATED PHISHING EMAIL DEFENDER
#
# SCENARIO:
# Your company's email server is being blasted with phishing emails trying to steal
# employee passwords. You need to build an automated containment system.
#
# Every time a suspicious email arrives, your system must analyze it, assign a risk
# level, track if it has malicious links, and update an internal safety score.
#
# YOUR TASK:
# Create a class named PhishingAnalyzer that sets up an email assessment profile,
# checks the content for danger signs, and updates the corporate alert dashboard.
#
# THE GOALS & CONSTRAINTS:
# 1. The class blueprint must accept two initial pieces of data when an email object is born:
#    - The sender_address (e.g., "urgent@paypal-security.com")
#    - The email_body (e.g., "Click here to reset your bank password immediately!!")
#
# 2. Every email object born must also start with a default danger_score integer of 0,
#    and a default tracking status boolean named contains_malicious_link set to False.
#
# 3. Create an action method named scan_content inside your class:
#    - It must clean the email_body string by converting it to lowercase.
#    - If the words "click here" OR "password" exist inside the email_body, it must
#      add 50 points to the object's internal danger_score, and change the
#      contains_malicious_link status to True.
#    - If the sender_address does NOT end with the official company domain ".com",
#      it must add an extra 25 points to the internal danger_score.
#
# 4. Create another action method named get_incident_report inside your class:
#    - This method needs to evaluate the final internal danger_score and RETURN a tuple
#      containing two strings: (risk_level, recommended_action).
#    - If danger_score is 75 or higher, return: ("CRITICAL", "DELETE_EMAIL_AND_BLOCK_SENDER")
#    - If danger_score is 50, return: ("MEDIUM", "QUARANTINE_FOR_REVIEW")
#    - For anything lower, return: ("LOW", "DELIVER_TO_INBOX")
#
# TEST BENCH (Outside the Class):
# Test your architecture by simulating an incoming attack with this data:
# Sender: "security@netf1ix-billing.org"
# Body: "Your account is suspended. CLICK HERE to update your password."
#
# Run your scanning actions, retrieve the returned tuple report, unpack the
# report into separate variables, and print the results to the screen!

class PhishingAnalyzer:
    def __init__(self,sender_address, email_body):
        self.sender_address = sender_address
        self.email_body = email_body
        self.danger_score = 0
        self.contains_malicious_link = False

    def scan_content(self):
        lower_case =  self.email_body.lower()
        scan1 = "click here" in lower_case
        scan2 = "password" in lower_case
        if scan1 or scan2:
            self.danger_score += 50
            self.contains_malicious_link = True
        if not self.sender_address.endswith(".com"):
            self.danger_score += 25

    def get_incident_report(self):
        if self.danger_score >= 75:
           action = "CRITICAL", "DELETE_EMAIL_AND_BLOCK_SENDER"
        elif self.danger_score == 50:
            action = "MEDIUM", "QUARANTINE_FOR_REVIEW"
        else:
            action = "LOW", "DELIVER_TO_INBOX"
        return action

email_to_check = PhishingAnalyzer("security@netf1ix-billing.org","Your account is suspended. CLICK HERE to update your password.")
email_to_check.scan_content()
risk, recommended_plan = email_to_check.get_incident_report()

print(f"The risk is: {risk}")
print(f"Recommended plan is: {recommended_plan}")