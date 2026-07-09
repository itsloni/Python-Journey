# REAL INTERVIEW CHALLENGE: CLOUD DATABASE ACCESS AUDITOR
#
# SCENARIO:
# You are an automation architect protecting a banking database. You need to log
# who accesses sensitive client data and automatically flag suspicious behaviors.
#
# Standard data queries are normal, but some database users are designated as
# "Service Accounts" (automated bots). Automated bots have strict access limits
# because if a bot gets hijacked by a hacker, it will steal data at warp speed.
#
# YOUR TASK:
# Read the requirements below. Design the class structure, manage the data
# properties, determine your methods, and handle the logic on your own.
#
# THE REQUIREMENTS:
# 1. Design a system that represents a standard DatabaseUser. It needs to accept
#    a profile_name string (e.g., "analyst_john") when it is created.
# 2. Every user profile starts the day with an internal query_count of 0, and a
#    security_standing string set to "CLEAR".
# 3. The user needs an action method to log when they run a database query.
#    Every time they run a query, their query_count goes up by 1. If their
#    query_count hits 5 or more, their security_standing must change to "SUSPICIOUS".
# 4. Design an upgraded profile for a ServiceAccount bot user that inherits everything
#    from the standard DatabaseUser. Bots have a zero-tolerance policy: the very
#    first time it runs a query (query_count >= 1), its security_standing must
#    instantly change to "HIGH_RISK_BOT_ACTIVITY".
# 5. The system needs an audit check method that returns a True/False decision on
#    whether the system should temporarily lock out that account. If the standing
#    is "SUSPICIOUS" or "HIGH_RISK_BOT_ACTIVITY", return True. Otherwise, return False.
#
# TEST BENCH (Outside the Class):
# Simulate a security audit on a Service Account bot named "data_backup_bot".
# Log one query attempt on it. Run your audit check to retrieve the True/False
# lockout decision, unpack the result into a variable, and print it to the screen!

class DatabaseUser:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.query_count = 0
        self.security_standing = "CLEAR"

    def database_query(self):
        self.query_count += 1
        if self.query_count >= 5:
            self.security_standing = "SUSPICIOUS"

    def audit_checker(self):
        if self.security_standing == "SUSPICIOUS" or self.security_standing == "HIGH_RISK_BOT_ACTIVITY":
            return True
        else:
            return False

class ServiceAccounts(DatabaseUser):
    def database_query(self):
        self.query_count += 1
        if self.query_count >= 1:
            self.security_standing = "HIGH_RISK_BOT_ACTIVITY"

service_bot = ServiceAccounts("data_backup_bot")
service_bot.database_query()

audit = service_bot.audit_checker()

print(f"Is this user Dangerous? {audit}")
print(f"What's the security standing? {service_bot.security_standing}")