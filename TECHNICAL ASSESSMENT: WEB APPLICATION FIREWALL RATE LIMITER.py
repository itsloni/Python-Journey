# TECHNICAL ASSESSMENT: WEB APPLICATION FIREWALL RATE LIMITER
#
# INSCENARIO & OBJECTIVE:
# Attackers often launch Distributed Denial of Service (DDoS) attacks against web servers
# by sending a massive flood of HTTP requests in a short period. You need to write a
# Python script that models a Web Application Firewall (WAF) rate limiter.
#
# The application monitors incoming traffic profiles. Every traffic profile represents
# an IP address. The system must track the volume of requests coming from each IP.
# Standard web visitors are allowed to browse normally, but if their request volume
# reaches a threshold of 100 requests, their traffic state must be updated to flagged.
#
# Our API routes also receive automated background data sync traffic from verified
# corporate API keys. Because API keys process data in bulk, they are allowed a
# much higher threshold and should only be flagged if their request volume hits 1000 requests.
#
# The rate limiter must be able to evaluate any active traffic profile and output
# a boolean decision on whether the WAF should deploy a CAPTCHA challenge to that IP.
# A CAPTCHA should be deployed only if the traffic state is currently flagged.
#
# Verify your system architecture by simulating an automated background data sync profile
# that has received 1050 incoming requests. Run the evaluation to see if a CAPTCHA
# challenge is required, and output the final decision.


class Waf:
    def __init__(self,ip_address):
        self.ip_address = ip_address
        self.volume_threshold = 0
        self.traffic_state = "Normal"
        self.rate_limiter = False

    def flagged(self):
        self.volume_threshold += 1
        if self.volume_threshold >= 100:
            self.traffic_state = "flagged"
            self.rate_limiter = True
            return True
        else:
            return False

    def assessment(self):
        if self.traffic_state == "flagged":
            action = f"Capture challenge must be deployed to {self.ip_address}"

        else:
            action = f"Capture challenge not needed for {self.ip_address}"
        return action


class Apiroutes(Waf):
    def flagged(self):
        self.volume_threshold += 1
        if self.volume_threshold >= 1000:
            self.traffic_state = "flagged"
            self.rate_limiter = True
            return True
        else:
            return False

ip2 = Apiroutes("192.168.1.1")
for i in range(1050):
    ip2.flagged()
ip1 = Waf("199.437.091")
for p in range(101):
    ip1.flagged()

print(f"Should WAF be deployed here? {ip1.rate_limiter}")
print(f"Final Volume: {ip1.volume_threshold}")
print(f"Traffic State: {ip1.traffic_state}")
print(ip1.assessment())

print(f"Should WAF be deployed here? {ip2.rate_limiter}")
print(f"Final Volume: {ip2.volume_threshold}")
print(f"Traffic State: {ip2.traffic_state}")
print(ip2.assessment())



