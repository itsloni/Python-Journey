# CHALLENGE 4: State Monitoring & Variable Modification
#
# Prompt: Design an automated system to track an active network port profile. The system
# must register a port by its integer number when created, and automatically track its
# data transfer volume starting at 0 Megabytes. The profile needs an action to record
# when data passes through it, adding the specific number of transferred Megabytes to
# its total volume. If the port's total volume ever exceeds 10,000 Megabytes, it must
# automatically shift its network priority status to "THROTTLED". Simulate a massive
# file transfer that pushes a port over the limit and verify its state updates.

class PortNetwork:
    def __init__(self, port_profile):
        self.port_profile = port_profile
        self.port_profile_int = int(port_profile)
        self.data_transfer_volume = 0
        self.priority_status = "NORMAL"

    def data_passage(self, transferred_bytes):
        self.data_transfer_volume += transferred_bytes
        if self.data_transfer_volume > 10000:
            self.priority_status = "THROTTLED"
            action = f"Alert!: Port {self.port_profile_int} has exceeded 10,000 Megabytes. STATUS: Network priority status has been set to {self.priority_status}"
        else:
            action = f"Port {self.port_profile_int} is within normal range. STATUS: {self.priority_status}"

        return action

while True:
    try:
        port_num = input("Input port number: ")
        profile = PortNetwork(port_num)
        while True:
            print(profile.data_passage(90000))
            break

    except ValueError:
        print("Pls input a valid port type")