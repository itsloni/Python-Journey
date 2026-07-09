# REAL INTERVIEW CHALLENGE: CLOUD NETWORK ACCESS SECURITY
#
# SCENARIO:
# You are automating identity access management for a cloud environment (like AWS or Azure).
# You need to track different types of user profiles. Every user has a name and needs
# to be logged, but administrative users get special system-wide clearance powers
# that regular guests do not have.
#
# YOUR TASK:
# Write a system using inheritance that tracks a base user profile and upgrades
# it for an administrative user.
#
# THE GOALS & CONSTRAINTS:
# 1. Create a base parent class named CloudUser.
# 2. The CloudUser constructor must accept a username string when it is born
#    and save it to an attribute.
# 3. CloudUser must have a normal action method named log_activity that prints:
#    "[LOG] User {username} performed a basic action."
# 4. Create a child class named AdminUser that inherits everything from CloudUser.
# 5. The AdminUser child class must have its own unique action method named
#    override_system_access that prints:
#    "[CRITICAL] Admin {username} bypassed firewall protocols!"
#
# TEST BENCH (Outside the Class):
# - Create an administrative user object named admin1 with the username "cyber_commander".
# - Call the inherited basic log activity method on admin1 first.
# - Call the unique admin override method on admin1 second.


class CloudUser:
    def __init__(self,username):
        self.username = username

    def log_activity(self):
        print(f"[LOG] User {self.username} performed a basic action.")


class AdminUser(CloudUser):
    def override_system_access(self):
        print(f"[CRITICAL] Admin {self.username} bypassed firewall protocols!")

admin1 = AdminUser("cyber_commander")
admin1.log_activity()
admin1.override_system_access()