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

# [ARCHITECT YOUR USERSESSION CLASS HERE]




# Pipeline Execution:
# Creating a user instance from your blueprint
session_alpha = UserSession("clerk_jane", "Guest")

# Executing safe access logs
msg_1 = session_alpha.log_access_attempt("Finance_Public_Dashboard")
msg_2 = session_alpha.log_access_attempt("HR_Holiday_Calendar")

# Executing a suspicious access trigger
msg_3 = session_alpha.log_access_attempt("Admin_Database_Root")

print("----- CHALLENGE 2 RESULTS -----")
print(f"Log 1 Status: {msg_1}")
print(f"Log 2 Status: {msg_2}")
print(f"Log 3 Status: {msg_3}")
print(f"Complete Session History for {session_alpha.username}: {session_alpha.access_log}")
