# challenge_text = """
# The Challenge: The Smart Home Security System 🏠🔒
# You are building the control panel software for a high-tech smart home.
# The homeowner can type commands into the panel to control the house.
#
# You must track two completely separate systems at the same time:
# 1. The Alarm System (Armed or Disarmed)
# 2. The Front Door Lock (Locked or Unlocked)
#
# The Initial Setup (When the game starts):  alarm_off = True
# * The system starts with the Alarm Disarmed.
# * The system starts with the Front Door Unlocked. door_unlocked = True
#
# The Rules Your Code Must Enforce:
# * Arming the Alarm: The user can type arm. If it is already armed, yell at them.
#   If it is disarmed, arm it.
# * The Security Lockout Rule: If the alarm is Armed, the user cannot unlock the front door!
#   If they try to type unlock while the alarm is active, the system should sound a
#   warning and refuse to unlock the door.
# * Locking the Door: The user can type lock. If the door is already locked, tell them.
#   If it is unlocked, lock it. (Locking the door is allowed whether the alarm is on or off).
# * Unlocking the Door: The user can type unlock. They can only unlock it if the door
#   is currently locked AND the alarm is disarmed.
# * Turning off the Alarm: The user can type disarm. If it is already off, tell them.
#   If it is on, turn it off.
#
# Include a help command to show the options, an exit command to close the program,
# and a catch-all safety net for when they type completely random words.
# """
#
# print(challenge_text)

alarm_armed = False
door_locked = False

help = """The Rules Your Code Must Enforce:
Arming the Alarm: The user can type arm. If it is already armed, yell at them. 
If it is disarmed, arm it.
The Security Lockout Rule: If the alarm is Armed, the user cannot unlock the front door! 
If they try to type unlock while the alarm is active, the system should sound a 
warning and refuse to unlock the door.
Locking the Door: The user can type lock. If the door is already locked, tell them. 
If it is unlocked, lock it. (Locking the door is allowed whether the alarm is on or off).
Unlocking the Door: The user can type unlock. They can only unlock it if the door 
is currently locked AND the alarm is disarmed.
Turning off the Alarm: The user can type disarm. If it is already off, tell them. 
If it is on, turn it off.
"""
prompt = ""
while True:
    prompt = input("system cmd>: ").lower()
    if prompt == "arm":
        if not alarm_armed:
            print("Alarm has been Armed")
            alarm_armed = True
        else:
            print("Alarm is already Armed before Broski!")

    elif prompt == "unlock":
        if alarm_armed:
            print("Warning: Door can't be unlocked, Disarm alarm first!")
            alarm_armed = True
        else:
            print("Door Unlocked!")
            door_locked = False
            alarm_armed = False
    elif prompt == "lock":
        if not door_locked:
            print("The door is now locked!")
            door_locked = True
        else:
            print("The door has already been locked!")
    elif prompt == "disarm":
        if alarm_armed:
            print("The alarm has been disarmed")
            alarm_armed = False
        else:
            print("It's disarmed already lol!")
    elif prompt == "help":
        print(help)
    elif prompt == "exit":
        break
    else:
        print("Input Correct Command!")



# My First Try but merged 2 systems together
# alarm_disarmed_unlocked = True
# door_unlocked = True
#
# help = """The Rules Your Code Must Enforce:
# Arming the Alarm: The user can type arm. If it is already armed, yell at them.
# If it is disarmed, arm it.
# The Security Lockout Rule: If the alarm is Armed, the user cannot unlock the front door!
# If they try to type unlock while the alarm is active, the system should sound a
# warning and refuse to unlock the door.
# Locking the Door: The user can type lock. If the door is already locked, tell them.
# If it is unlocked, lock it. (Locking the door is allowed whether the alarm is on or off).
# Unlocking the Door: The user can type unlock. They can only unlock it if the door
# is currently locked AND the alarm is disarmed.
# Turning off the Alarm: The user can type disarm. If it is already off, tell them.
# If it is on, turn it off.
# """
# prompt = ""
# while True:
#     prompt = input("system cmd>: ").lower()
#     if prompt == "arm":
#         if alarm_disarmed_unlocked:
#             print("Alarm has been Armed")
#         else:
#             print("Alarm is already Armed Broski!")
#             alarm_disarmed_unlocked = False
#     elif prompt == "unlock":
#         if alarm_disarmed_unlocked:
#             print("You can't unlock the door!")
#         else:
#             print("Door has been unlocked!")
#             alarm_disarmed_unlocked = True
#     elif prompt == "lock":
#         if alarm_disarmed_unlocked:
#             print("Door has been locked!")
#             alarm_disarmed_unlocked = False
#         else:
#             print("The door has been locked")
#     elif prompt == "disarm":
#         if alarm_disarmed_unlocked:
#             print("It is already off lol!")
#         else:
#             print("The alarm has be disarmed!")
#             alarm_disarmed_unlocked = True
#     elif prompt == "help":
#         print(help)
#     elif prompt == "exit":
#         break
#     else:
#         print("Input Correct Command!")