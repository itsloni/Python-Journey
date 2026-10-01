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
full_reset = False

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
            print("Crane has already started and besides an emergency stop has been previously initiated! You have to continue before you can proceed to pick-up.")
            is_started = True
            emergency_switch = True
        # elif not is_started and emergency_switch:
        #     print("There has been an emergency stop! so crane cannot move. To move you must first continue and then move.")

        elif is_started and not emergency_switch:
            print("Crane has already started. Proceed by picking up.")
            is_started = True
            emergency_switch = False
    elif input_state == "pickup":
        if is_started:
            if not is_moving:
                if not dropped_in_shipping_container:
                    if not is_returned:
                        if not is_picked_up and not emergency_switch:
                            print("Crates has been picked up from the conveyor belt and is getting ready to start moving")
                            is_picked_up = True
                            emergency_switch = False
                        elif is_picked_up and not emergency_switch:
                            print("Crane has already Picked-up the crates. Please proceed by moving the crates.")
                            is_picked_up = True
                            emergency_switch = False
                        elif is_picked_up and emergency_switch:
                            print("Crane has already picked-up and besides an emergency stop has been previously initiated! You have to continue before you can proceed to moving.")
                            is_picked_up = True
                            emergency_switch = True
                        elif not is_picked_up and emergency_switch:
                            print("There has been an emergency stop! so crane cannot pickup. To pickup you must first continue and then pickup.")
                            is_picked_up = False
                            emergency_switch = True
                    else:
                        print("Crane cannot pickup when it has been returned. Please start the crane over to then be able pickup the crates.")
                        is_returned = True
                        is_started = False
                        is_picked_up = False
                        is_moving = False
                        dropped_in_shipping_container = False
                        emergency_switch = False
                else:
                    print("Crane cannot pickup when it has already dropped-off in shipping Container. Please return to start and start, before you can then pickup.")
                    is_started = True
                    is_picked_up = True
                    is_moving = True
                    dropped_in_shipping_container = True
                    is_returned = False
                    emergency_switch = False

            elif is_moving:
                print("Crane cannot pickup when it is already moving. Please drop-off, return and then start to pickup.")
                is_picked_up = False
                emergency_switch = False
        else:
            print("You cannot pickup without starting/continueing. Please decide before you pick up.")
    elif input_state == "moving":
        if is_started:
            if is_picked_up:
                if not dropped_in_shipping_container:
                    if not is_returned:
                        if not is_moving and not emergency_switch:
                            print("Crane has started moving the crates to the shipping container. Be at a safe distance.")
                            is_moving = True
                            emergency_switch = False
                        elif is_moving and not emergency_switch:
                            print("Crane has already started moving the crates. Please be at a safe distance")
                            is_moving = True
                            emergency_switch = False
                        elif is_moving and emergency_switch:
                            print("Crane has already moved and besides an emergency stop has been previously initiated! You have to continue before you can proceed to drop-off.")
                            emergency_switch = True
                            is_moving = True
                        elif not is_moving and emergency_switch:
                            print("There has been an emergency stop! so crane cannot move. To move you must first continue and then move.")
                            emergency_switch = True
                            is_moving = False
                    else:
                        print("Crane cannot move when it has been returned. Please start the crane over to pickup before you can then move again.")
                        is_returned = True
                        is_started = False
                        is_picked_up = False
                        is_moving = False
                        dropped_in_shipping_container = False
                        emergency_switch = False
                else:
                    print("Crane cannot move when it has already dropped-off in shipping Container. Please return to start and start then pickup to be able to move")
                    is_started = True
                    is_picked_up = True
                    is_moving = True
                    dropped_in_shipping_container = True
                    is_returned = False
                    emergency_switch = False


            else:
                print("Crane cannot move across the floor if it hasn't picked up the crates yet. Please pick-up first before moving.")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        else:
            print("You cannot move crates without starting the crane. Please start the crane first, then pickup to be able to move.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False

    elif input_state == "drop-off":
        if is_started:
            if is_picked_up:
                if is_moving:
                    if not is_returned:
                        if not dropped_in_shipping_container and not emergency_switch:
                            print("Crane has dropped off the crates at the shipping container, and is ready to return for another start.")
                            dropped_in_shipping_container = True
                            emergency_switch = False
                        elif dropped_in_shipping_container and not emergency_switch:
                            print("Crane has already dropped off crates at the shipping container. Please return.")
                            dropped_in_shipping_container = True
                            emergency_switch = False
                        elif dropped_in_shipping_container and emergency_switch:
                            print("Crane has already moved and besides an emergency stop has been previously initiated! You have to continue before you can proceed to drop-off.")
                            dropped_in_shipping_container = True
                            emergency_switch = True
                        elif not dropped_in_shipping_container and emergency_switch:
                            print("There has been an emergency stop! so crane cannot drop-off. To drop-off you must first continue and then drop-off.")
                            dropped_in_shipping_container = False
                            emergency_switch = True
                    else:
                        print("Crane cannot drop-off when it has returned for a start already. Please start the crane again, pickup, move then you can drop-off.")
                        is_returned = True
                        is_picked_up = False
                        is_started = False
                        is_moving = False
                        dropped_in_shipping_container = False
                        emergency_switch = False

                else:
                    print("You cannot drop-off when you haven't moved the crates or finished moving the crates")
                    is_started = True
                    is_picked_up = True
                    is_moving = False
                    dropped_in_shipping_container = False
                    is_returned = False
                    emergency_switch = False
            else:
                print("You cannot drop-off when you have not picked up the crates in the first place. Please pickup and move, then you can drop-off")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False

        else:
            print("You cannot drop-off when you haven't even started the crane. Please start the crane, pickup, move then you can drop-off.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False
    
    elif input_state == "return":
        if is_started:
            if is_picked_up:
                if is_moving:
                    if dropped_in_shipping_container:
                        if not is_returned and not emergency_switch:
                            print("The Crane has successfully dropped off the crates and has returned to start again.")
                            is_returned = True
                            emergency_switch = False
                        elif is_returned and not emergency_switch:
                            print("Crane has already dropped off the crates and successfully returned back to start.")
                            is_returned = True
                            emergency_switch = False
                        elif not is_returned and emergency_switch:
                            print("There has been an emergency stop! so crane cannot return. To return you must first continue and then return.")
                            is_returned = False
                            emergency_switch = True
                        elif is_returned and emergency_switch:
                            print("Crane has already returned and besides an emergency stop has been previously initiated! You have to continue before you can proceed to start.")
                            is_returned = True
                            emergency_switch = True
                    else:
                        print("Crane has not dropped-off in the shipping container and cannot return. Please drop-off first before you return.")
                        is_started = True
                        is_picked_up = True
                        is_moving = True
                        dropped_in_shipping_container = False
                        is_returned = False
                        emergency_switch = False
                else:
                    print("You cannot return when you haven't even moved the crates or finished moving the crates")
                    is_started = True
                    is_picked_up = True
                    is_moving = False
                    dropped_in_shipping_container = False
                    is_returned = False
                    emergency_switch = False
            else:
                print("You cannot return when you have not picked up the crates in the first place. Please pickup, move, and drop-off then you can return")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        else:
            print("You cannot return when you haven't even started the crane. Please start the crane, pickup, move, drop-off then you can return.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False




    elif input_state == "reset" or input_state == "emergency" or input_state == "continue" or input_state == "stop" or input_state == "resume":
        if input_state == "emergency": #or input_state == "continue":
            if is_started
            if not emergency_switch:
                if is_started:
                    print("Crane has stopped for an emergency. To continue type 'continue'.")
                    is_started = True
                    # is_picked_up = False
                    # is_moving = False
                    # dropped_in_shipping_container = False
                    # is_returned = False
                    emergency_switch = True
                # if is_picked_up:
                #     print("Crane has stopped at pickup stage for an emergency. To continue type 'continue'.")
                #     is_started = True
                #     is_picked_up = False
                #     is_moving = False
                #     dropped_in_shipping_container = False
                #     is_returned = False
                #     emergency_switch = True

                else:
                    print("Emergency cannot be done if crane has not started.Please start first")
                    is_started = False
                    emergency_switch = False
            else:
                print("Emergency switch has already been turned on.")

                    # elif is_picked_up:
                    #     print("Pickup stopped.")
                    #     is_picked_up = False
                    #     emergency_switch = True
                    # elif is_moving:
                    #     print("Moving stopped.")
                    #     is_moving = False
                    #     emergency_switch = True

                # else:
                #     print("Crane cannot halt/stop until it has at least started.")
        elif input_state == "continue":
            if emergency_switch:
                # print("Crane has successfully continued.")
                if is_started:
                    print("Crane has successfully continued.")
                    is_started = True
                    emergency_switch = False
                    if is_picked_up:
                        print("Crane has successfully continued.")
                        is_picked_up = True
                        emergency_switch = False
                        if is_moving:
                            print("Crane has successfully continued.")
                            is_moving = True
                            emergency_switch = False
                else:
                    print("Crane can continue when crane hasn't started and the emergency wouldn't have been able to be on in the frst place."
                          "Please start crane first.")
                    is_picked_up = False
                    emergency_switch = False
                # elif not is_moving:
                #     print("Crane has successfully continued.")
                #     is_moving = True
                #     emergency_switch = False
            else:
                print("Crane cannot run an emergency-continue until emergency is turned on.")

    # elif input_state == "reset":
    #     if is_started:
    #         print("Crane is being reset. Pls start Over.")
    #         break

    else:
        print("Enter valid input. Either you Start, Pickup, Moving, drop-off, or stop(Emergency break")



