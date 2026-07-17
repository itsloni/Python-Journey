# CHALLENGE 3: Standard Object Modeling (Encapsulation)
#
# Prompt: Model a digital user profile template for a corporate VPN gatekeeper. The system
# needs to track individual employee connections by their name. Every profile must
# automatically track its active session duration (starting at 0 minutes) and an
# access status (starting as "CONNECTED"). Write an internal capability for this
# profile to log a disconnection alert, which permanently updates its access status
# to "DISCONNECTED". Test your architecture by creating a profile for "employee_sarah"
# and triggering a disconnection.

class VpnGate:
    def __init__(self, user_name):
        self.user_name = user_name
        self.active_session = 0
        self.access_status = "CONNECTED"

    def disconnection_alert(self):
        self.access_status = "DISCONNECTED"
        ban = f"ALERT!: {self.user_name}, Your Connection's lost. Status: {self.access_status}"
        return ban

user_profile = VpnGate("employee_sarah")
outcome = user_profile.disconnection_alert()
print(outcome)
