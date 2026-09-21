# ======================================================================
# TECHNICAL ASSESSMENT: SMART HOME SECURITY CONTROLLER STATE MACHINE
# ======================================================================
#
# BACKGROUND
# You are tasked with building a state machine for a smart home security
# hub via a command-line interface. The system monitors two critical
# components: an alarm system and a physical front door.
#
# INITIAL SYSTEM STATE
# When the program initializes, the security system must start in its
# safest default mode:
# - The alarm system is deactivated.
# - The front door is secured (closed).
#
# FUNCTIONAL REQUIREMENTS
# Implement an interactive loop that continuously accepts string commands
# from standard input. The program must handle case-insensitive inputs
# and execute the following conditional logic:
#
# 1. "arm"
#    - If the alarm is already activated, notify the user.
#    - If the alarm is deactivated, activate it and notify the user.
#
# 2. "disarm"
#    - If the alarm is already deactivated, notify the user.
#    - If the alarm is activated, deactivate it and notify the user.
#
# 3. "open"
#    - If the door is already open, notify the user.
#    - If the door is closed, transition the door to open.
#      CRUCIAL EDGE CASE: If the door is opened while the alarm system
#      is currently activated, the system must immediately trigger a
#      high-priority breach alert to the screen and terminate the
#      entire application execution instantly.
#    - If the door is opened while the alarm system is deactivated,
#      simply notify the user that the door opened successfully.
#
# 4 "close"
#    - If the door is already closed, notify the user.
#    - If the door is open, transition the door to closed and notify
#      the user.
#
# 5. "exit"
#    - Gracefully break the control loop and terminate the program.
#
# 6. Invalid Input
#    - If the user types anything else, display a generic error message
#      indicating an unrecognized command and prompt again.
#
# INTERVIEWER'S INSTRUCTIONS
# - Design the logic using your choice of boolean flags to track the states.
# - Ensure your variable names are clean, professional, and self-documenting.
# - Watch your nesting levels to avoid writing messy code.
# ======================================================================
#
#
alarm_system_deactivated = True
front_door_closed = True

while True:
    users_input = input("> ").lower()
    if users_input == "arm":
        if alarm_system_deactivated:
            print("Alarm system activated")
            alarm_system_deactivated = False
        else:
            print("Alarm system is already activated")

    elif users_input == "disarm":
        if not alarm_system_deactivated:
            print("Alarm system is deactivated")
            alarm_system_deactivated = True
        else:
            print("Alarm system already deactivated")

    elif users_input == "open":
        if front_door_closed:
            if alarm_system_deactivated == False:
                print("EMERGENCY BREACH!!!")
                break
            else:
                print("Front door opened")
                front_door_closed = False
                # alarm_system_deactivated = False
        else:
            print("Front door already opened")

    elif users_input == "close":
        if not front_door_closed:
            print("Front door closed")
            front_door_closed = True
        else:
            print("front door already closed")