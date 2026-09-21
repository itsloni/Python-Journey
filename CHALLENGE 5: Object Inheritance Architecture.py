# CHALLENGE 5: Object Inheritance Architecture
#
# Prompt: Create an identity classification structure for servers in a cloud infrastructure.
# Write a base system that models a general server, storing its unique hostname when created
# and providing a shared action to output a simple heartbeat diagnostic message. Build a
# specialized child system for an active Database Server that inherits everything from the
# general server template. The Database Server must possess an additional unique capability
# to output a specialized database health check signal. Demonstrate your child system successfully
# executing both the general heartbeat and the unique database check.

class Identifier:
    def __init__(self, identity):
        self.identity = identity
        self.health = "GOOD"
        self.diagnostic = f"Currently running Diagnostics on {self.identity}"

    def diagnostic_message(self):
        print("Hello!")
        return self.diagnostic


class DatabaseServer(Identifier):
    def diagnostic_health(self):
        if self.identity.endswith(".exe"):
            self.health = f"[ALERT!!]Database Server running on {self.identity}"
        else:
            self.health = f"[SAFE]Database Server running on {self.identity}"
        return self.health

unique_hostname = input("Hosts name: ")
classifier = DatabaseServer(unique_hostname)
print(classifier.diagnostic_message())
print(classifier.diagnostic_health())

