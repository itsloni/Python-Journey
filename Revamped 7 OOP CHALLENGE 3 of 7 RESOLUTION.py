# CHALLENGE 3: Standard Object Modeling (Encapsulation)
#
# Prompt: Model a digital user profile template for a corporate VPN gatekeeper. The system
# needs to track individual employee connections by their name. Every profile must
# automatically track its active session duration (starting at 0 minutes) and an
# access status (starting as "CONNECTED"). Write an internal capability for this
# profile to log a disconnection alert, which permanently updates its access status
# to "DISCONNECTED". Test your architecture by creating a profile for "employee_sarah"
# and triggering a disconnection.

class VpnGatekeeper:
    def __init__(self,employee):
        self.employee = employee
        self.active_session = 0
        self.access_status = "CONNECTED"

    def counter(self, time_passed):
        self.active_session += time_passed
        minutes = f"{self.active_session} minutes"
        return minutes

    