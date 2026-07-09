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
