# REAL INTERVIEW CHALLENGE: BLACKLIST FIREWALL RULE CLASS
#
# Scenario:
# You are developing an automated incident response tool for a corporate firewall.
# When a security system flags an attack, it needs to create a new "Firewall Rule"
# object to track what port is blocked, why it is blocked, and how many times
# that blocked port has been triggered by a hacker.
#
# Your Task:
# Create a class named FirewallRule that builds the rule template, manages
# the rule data, and tracks traffic logs.
#
# The Goals & Constraints:
# 1. Create an __init__ constructor that accepts two parameters: port_number and block_reason.
# 2. Inside the __init__ constructor, build three attributes:
#    - self.port_number (Save the integer or string passed into the parameter).
#    - self.block_reason (Save the string passed into the parameter).
#    - self.hit_count (Set this to a default integer starting placeholder of 0).
# 3. Create a normal method named log_blocked_attempt inside the class:
#    - This method takes no extra parameters except self.
#    - Its job is to increment (add 1 to) the self.hit_count attribute every time it runs.
#    - It should also print a message showing that traffic on that port was dropped.
#
# Outside the Class (Test Bench):
# 1. Create a firewall rule object named rule1 for port 443 with the reason "Malware C2".
# 2. Print the initial rule1.hit_count to verify it starts at 0.
# 3. Simulate two hacker attack attempts by calling rule1.log_blocked_attempt() twice.
# 4. Print rule1.hit_count one last time to verify it updated to 2 in internal memory.

class FirewallRule:
    def __init__(self, port_number, block_reason):
        self.port_number = port_number
        self.block_reason = block_reason
        self.hit_count = 0
    def log_blocked_attempt(self):
        self.hit_count += 1
        print(f"Traffic on port {self.port_number} was dropped due to {self.block_reason}")
rule1 = FirewallRule(433,"Malware C2")
rule1.log_blocked_attempt()
rule1.log_blocked_attempt()
print(f"Total hits: {rule1.hit_count}")


