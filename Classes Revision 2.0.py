from ipaddress import ip_address


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10 #These are attributes. They belong to a class.
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 1
print(point2.x)
point1.move()
point1.draw()


# CONSTRUCTORS

class Point:
    def __init__(self, x, y):#sSo this is the constructor and it's a function that gets called at the time of creating an object
        self.x = x # This is literally the same as point1.x = 10 just that the constructor take in the parameter
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)
print(point1.x, point1.y)


# Practice
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name} ")

loni = Person("Loni")
loni.talk()
bob = Person("Bob")
bob.talk()

# ==============================================================================
# CHALLENGE 1: THE NETWORK FIREWALL OBJECT BLUEPRINT
# ==============================================================================

# [ARCHITECT YOUR FIREWALL CLASS HERE]
class Firewall:
    def __init__(self, ip_address, device_name):
        self.ip_address = ip_address
        self.device_name = device_name
        self.is_active = True

    def trigger_emergency_block(self):
        self.is_active = False
        alert = f"CRITICAL: {self.device_name} ({self.ip_address}) HAS BEEN SHUT DOWN!"
        return alert

# Pipeline Execution:
# Creating an instance (object) from your blueprint
perimeter_fw = Firewall("192.168.1.1", "Edge_Firewall")

print("----- CHALLENGE 1 INITIAL STATE -----")
print(f"Device: {perimeter_fw.device_name}")
print(f"IP: {perimeter_fw.ip_address}")
print(f"Is Active Status: {perimeter_fw.is_active}\n")

# Triggering the internal object logic engine
alert_msg = perimeter_fw.trigger_emergency_block()

print("----- CHALLENGE 1 POST-ALERT STATE -----")
print(alert_msg)
print(f"Final Is Active Status: {perimeter_fw.is_active}\n\n")



#CHALLENGE 2
# ==============================================================================
# CHALLENGE 2: THE AUTOMATED USER PRIVILEGE AUDITOR
# ==============================================================================
# SCENARIO: Build a UserSession object blueprint that tracks an employee's
#           access logs and privilege levels dynamically.
#
# GOAL:
# 1. Architect a class named 'UserSession' with a constructor (__init__) that
#    accepts: 'username' and 'role'.
# 2. Automatically initialize a third tracking property named 'access_log'
#    as a baseline empty mutable list ([]).
# 3. Design a custom method inside named 'log_access_attempt' that accepts
#    a single parameter named 'resource_name'.
#    - Append 'resource_name' directly into the object's internal 'access_log' list.
#    - If 'role' is exactly "Guest" AND the 'resource_name' contains the word
#      "Admin", return: "SECURITY WARNING: Guest user {username} targeted an Admin resource!"
#    - Otherwise, return: "Access request recorded successfully."
#
# PIPELINE REQUIREMENT:
# You must write your own execution code below the class. Create an object for
# "clerk_jane" with the role "Guest". Call the method multiple times (one target
# should be "Admin_Database_Root"), and print your final logs to verify the output!
# ==============================================================================

# [ARCHITECT YOUR CLASS AND YOUR ENTIRE EXECUTION PIPELINE COMPLETELY AUTONOMOUSLY BELOW]

class UserSession:
    def __init__(self, user, role):
        self.user = user
        self.role = role
        self.access_log = []

    def log_access_attempt(self, resource_name):
        # self.resource_name = resource_name
        self.access_log.append(resource_name)
        if self.role == "Guest" and "Admin" in resource_name:
            warning = f"SECURITY WARNING: Guest user {self.user} targeted an Admin resource!"
            return warning
        else:
            success = f"Access request recorded successfully."
            return success


session = UserSession("clerk_jane", "Guest")
print(session.log_access_attempt("Guest"))
print(session.log_access_attempt("Guest"))
print(session.log_access_attempt("Admin_Database_Root"))
print(session.log_access_attempt("Guest"))




