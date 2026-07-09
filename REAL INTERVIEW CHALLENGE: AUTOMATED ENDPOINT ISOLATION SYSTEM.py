# REAL INTERVIEW CHALLENGE: AUTOMATED ENDPOINT ISOLATION SYSTEM
#
# SCENARIO:
# You are an automation engineer protecting a corporate network. Hackers often
# target individual employee laptops (endpoints) with malware. Your team needs a
# system that can track the health of these endpoints, register when a threat
# is found, and determine if the laptop should be isolated from the network.
#
# There are thousands of standard employee laptops on the network, but some belong
# to executives (CEOs, CFOs) which are classified as High-Value Targets (HVT).
# If an executive laptop is compromised, it requires an immediate automated lockout.
#
# YOUR TASK:
# Read the goals below. Design the class architecture, choose your tools,
# manage the data attributes, determine your methods, and handle the logic
# entirely on your own using the 4-step framework.
#
# THE GOALS & CONSTRAINTS:
# 1. Design a system that represents a standard employee laptop. It needs to know
#    its own device name (e.g., "laptop-finance-01") when it is created.
# 2. It must track its own live security status. By default, every laptop starts
#    the day as "SECURE" and has a threat count of 0.
# 3. The laptop needs an action to record when a security sensor finds malware.
#    Every time malware is found, its threat count increases by 1. If its threat
#    count hits 3 or more, its security status changes permanently to "COMPROMISED".
# 4. Design an upgraded profile for an executive's laptop (High-Value Target).
#    It shares the exact same properties as a regular laptop, but it has one extra
#    strict rule: the very first time malware is found on it, its security status
#    must instantly change to "CRITICAL_ALERT".
# 5. The system needs an assessment check that evaluates the current security status
#    of any device and returns a True/False decision on whether the network should
#    isolate that endpoint. If the status is "COMPROMISED" or "CRITICAL_ALERT",
#    it returns True. Otherwise, it returns False.
#
# TEST BENCH (Outside the Class):
# Simulate an incident response test on an executive's laptop named "exec-ceo-macbook".
# Record one malware threat on it. Then, run your assessment check to retrieve the
# True/False isolation decision, unpack the result, and print it to the screen!


class Endpoint:
    def __init__(self, laptop_name):
        self.laptop_name = laptop_name
        self.live_security_status = "SECURE"
        self.threat_count = 0

    def malware(self):
        self.threat_count += 1
        if self.threat_count >= 3:
            self.live_security_status = "COMPROMISED!"

    def assessment(self):
        if self.live_security_status == "COMPROMISED!" or self.live_security_status == "CRITICAL_ALERT":
            return True
        else:
            return False


class Exec(Endpoint):
    def malware(self):
        self.threat_count += 1
        if self.threat_count >= 1:
            self.live_security_status = "CRITICAL_ALERT"



laptop1 = Exec("exec-ceo-macbook")
laptop1.malware()
should_isolate = laptop1.assessment()

print(f"should we isolate this device: {should_isolate}")
print(f"Current device status: {laptop1.live_security_status}")
