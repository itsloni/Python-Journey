# Interviewer: "We need you to build the terminal controller
# for an automated shipping crane inside a manufacturing factory.
# The crane picks up heavy crates from a conveyor belt, moves
# them across the floor, drops them into a shipping container,
# and returns. If the crane drops a crate while moving, or
# crashes into a wall, it could cause millions in damages.
# Build a state machine that handles starting the crane, picking up,
# moving, dropping off, and handling emergency overrides safely.
# Let's see your code."
is_started = False
is_picked_up = False
is_moving = False
dropped_in_shipping_container = False
is_returned = False
emergency_switch = False

while True:
    input_state = input("> ").lower()
    if input_state == "start":
        if not is_started and not emergency_switch:
            print("Smart crane is turned on and has started, getting ready to pickup")
            is_started = True
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False
        elif is_started and emergency_switch:
            print("Crane cannot start after an Emergency start stop it must continue.")
            emergency_switch = True
        else:
            print("Crane has already started. Proceed by picking up.")
    elif input_state == "pickup":
        if is_started:
            if not emergency_switch:
                if not is_picked_up and not is_moving:
                    print("Crates has been picked up from the conveyor belt and is getting ready to start moving")
                    is_picked_up = True
                    is_moving = False
                elif is_picked_up and not is_moving:
                    print("Crane has already Picked-up the crates. Please proceed by moving the crates.")
            elif emergency_switch:
                print("Crane pickup has stopped to proceed to moving You must continue.")
                is_picked_up = False
                emergency_switch = True
        else:
            print("You cannot pickup without starting/continueing. Please decide before you pick up.")
    elif input_state == "moving":
        if is_started:
            if is_picked_up:
                if not emergency_switch:
                    if not is_moving and not dropped_in_shipping_container:
                        print("Crane has started moving the crates to the shipping container. Be at a safe distance.")
                        is_moving = True
                        dropped_in_shipping_container = False
                    else:
                        print("Crane has already started moving the crates. Please be at a safe distance")
                else:
                    print("Crane moving has had an emergency stop! To proceed please type continue.")
                    emergency_switch = True
                    is_moving = False
            else:
                print("Crane cannot move across the floor if it hasn't picked up the crates yet. Please pick-up first.")
                is_picked_up = False
                is_moving = False
                emergency_switch = False
        else:
            print("You cannot move crates without starting the crane. Please start the crane first.")
            is_started = False
            is_picked_up = False
            is_moving = False
            emergency_switch = False

    elif input_state == "drop-off":
        if is_started:
            if is_moving:
                if not is_picked_up:
                    print("Crane has already Dropped off . Ready to restart.")

                else:
                    print("Crane has dropped off crates successfully at the shipping container and is returning for another start.")
                    print("Crane cycle ended and is ready to start again.")
                    is_picked_up = False
                    is_started = False
                    is_moving = False
            else:
                print("You cannot drop-off when you haven't moved the crates or finished moving the crates")
        else:
            print("You cannot drop-off when you haven't even started/continued the crane. Please start/continue.")

    elif input_state == "halt" or input_state == "stop" or input_state == "continue":
        if input_state == "halt" or input_state == "stop":
            if is_started and not emergency_switch:
                # if is_started:
                print("Crane has come to a halt and is ready to restart when you initiate continue.")
                is_started = False
                is_picked_up = False
                is_moving = False
                emergency_switch = True
                # elif is_picked_up:
                #     print("Pickup stopped.")
                #     is_picked_up = False
                #     emergency_switch = True
                # elif is_moving:
                #     print("Moving stopped.")
                #     is_moving = False
                #     emergency_switch = True

            else:
                print("Crane cannot halt/stop until it has at least started.")
        elif input_state == "continue":
            if is_started == False and emergency_switch:
                # print("Crane has successfully continued.")
                if not is_started:
                    print("Crane has successfully continued.")
                    is_started = True
                    emergency_switch = False
                elif not is_picked_up:
                    print("Crane has successfully continued.")
                    is_picked_up = True
                    emergency_switch = False
                elif not is_moving:
                    print("Crane has successfully continued.")
                    is_moving = True
                    emergency_switch = False
            else:
                print("Crane cannot continue until it has been stopped/halted.")

    elif input_state == "reset":
        if is_started:
            print("Crane is being reset. Pls start Over.")
            break

    else:
        print("Enter valid input. Either you Start, Pickup, Moving, drop-off, or stop(Emergency break")



