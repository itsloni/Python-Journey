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
        if not is_picked_up:
            if not is_moving:
                if not dropped_in_shipping_container:
                    # if not is_returned:
                    if not is_started and not emergency_switch:
                        print("Smart crane is turned on and has started, getting ready to pickup")
                        is_started = True
                        emergency_switch = False
                        is_returned = False
                        is_picked_up = False
                        is_moving = False
                        dropped_in_shipping_container = False
                    elif is_started and emergency_switch:
                        print("Crane has already started and besides an emergency stop has been previously initiated! You have to "
                              "continue before you can proceed to pick-up.")
                        is_started = True
                        emergency_switch = True
                        is_returned = False
                        is_picked_up = False
                        is_moving = False
                        dropped_in_shipping_container = False
                    elif is_started and not emergency_switch:
                        print("Crane has already started. Proceed by picking up.")
                        is_started = True
                        emergency_switch = False
                        is_returned = False
                        is_picked_up = False
                        is_moving = False
                        dropped_in_shipping_container = False
                    elif not is_started and emergency_switch:
                        print("Crane can not start because of emergency mode. to move on resume.")
                        is_started = False
                        is_picked_up = False
                        is_moving = False
                        emergency_switch = True
                        is_returned = False
                        dropped_in_shipping_container = False
                    # else:
                    #     print("Crane is back from returned and has now started, ready to e picked-up")
                    #     is_returned = False
                    #     is_started = True
                    #     is_picked_up = False
                    #     is_moving = False
                    #     dropped_in_shipping_container = False
                    #     emergency_switch = False
                    # else:
                    #     print("Crane cannot start when it has been returned. Please start the crane over to then be able pickup the crates.")
                    #     is_returned = True
                    #     is_started = False
                    #     is_picked_up = False
                    #     is_moving = False
                    #     dropped_in_shipping_container = False
                    #     emergency_switch = False
                # elif is_started == True and dropped_in_shipping_container == False and emergency_switch == True:
                #     print("There has been an emergency stop! so crane cannot pickup. To pickup you must first resume.")
                #     emergency_switch = True
                else:
                    print("Crane cannot start when it has already dropped-off in shipping Container. Please return  before you can start.")
                    is_started = True
                    is_picked_up = True
                    is_moving = True
                    dropped_in_shipping_container = True
                    is_returned = False
                    emergency_switch = False
            # elif is_started == True and is_moving == False and emergency_switch == True:
            #     print("There has been an emergency stop! so crane cannot start. To start you must first resume.")
            #     emergency_switch = True
            else:
                print("Crane cannot start when it is already moving with the picked up crates. Please drop-off, return and then start.")
                is_started = True
                is_picked_up = True
                is_moving = True
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        # elif is_started == True and is_picked_up == False and emergency_switch == True:
        #     print("There has been an emergency stop! so crane cannot start. To start you must first resume.")
        #     emergency_switch = True
        elif is_picked_up == False and emergency_switch == True:
            print("There has been an emergency stop! so crane cannot start. To pickup you must first resume.")
        else:
            print("Crane cannot start if it has already picked up the crates. Please proceed by moving, drop-off, and returning before you can then start the crane.")
            is_started = True
            is_picked_up = True
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
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
                            print("Crane has already picked-up and besides an emergency stop has been previously initiated! You have to "
                                  "continue before you can proceed to moving.")
                            is_picked_up = True
                            emergency_switch = True
                        elif not is_picked_up and emergency_switch:
                            print("There has been an emergency stop! so crane cannot pickup. To pickup you must first resume and then pickup.")
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
                    print("Crane cannot pickup when it has already dropped-off in shipping Container. Please return to start and start, "
                          "before you can then pickup,move and proceed to where you will drop-off.")
                    is_started = True
                    is_picked_up = True
                    is_moving = True
                    dropped_in_shipping_container = True
                    is_returned = False
                    emergency_switch = False
            # elif is_started == True and is_moving == False and emergency_switch == True:
            #     print("There has been an emergency stop! so crane cannot pickup. To pickup you must first resume.")
            #     emergency_switch = True


            else:
                print("Crane cannot pickup when it is already moving with the picked up crates. Please drop-off, return and then start to pickup.")
                is_started = True
                is_picked_up = True
                is_moving = True
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        elif is_started == False and emergency_switch == True:
            print("There has been an emergency stop! so crane cannot pickup. To pickup you must first resume.")

        else:
            print("You cannot pickup without starting. Please decide before you pick up.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False

    elif input_state == "moving":
        if is_started:
            if is_picked_up:
                if not dropped_in_shipping_container:
                    if not is_returned:
                        if not is_moving and not emergency_switch:
                            print("Crane has started moving the crates to the shipping container. Be at a safe distance.")
                            is_moving = True
                            emergency_switch = False
                            dropped_in_shipping_container = False
                            is_returned = False
                        elif is_moving and not emergency_switch:
                            print("Crane has already started moving the crates. Please be at a safe distance")
                            is_moving = True
                            emergency_switch = False
                            dropped_in_shipping_container = False
                            is_returned = False
                        elif is_moving and emergency_switch:
                            print("Crane has already moved and besides an emergency stop has been previously initiated! You have to continue before you can proceed to drop-off.")
                            emergency_switch = True
                            is_moving = True
                            dropped_in_shipping_container = False
                            is_returned = False
                        elif not is_moving and emergency_switch:
                            print("There has been an emergency stop! so crane cannot move. To move you must first continue and then move.")
                            emergency_switch = True
                            is_moving = False
                            dropped_in_shipping_container = False
                            is_returned = False
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

            # elif is_started == True and is_picked_up == False and emergency_switch == True:
            #     print("There has been an emergency stop! so crane cannot move. To move you must first continue and then move.")
            #     emergency_switch = True
            #     is_moving = False
            #     dropped_in_shipping_container = False
            #     is_returned = False



            else:
                print("Crane cannot move across the floor if it hasn't picked up the crates yet. Please pick-up first before moving.")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        elif is_started == False and emergency_switch == True:
            print("There has been an emergency stop! so crane cannot move. To move you must first resume.")
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
                            is_returned = False

                        elif dropped_in_shipping_container and not emergency_switch:
                            print("Crane has already dropped off crates at the shipping container. Please return.")
                            dropped_in_shipping_container = True
                            emergency_switch = False
                            is_returned = False
                        elif dropped_in_shipping_container and emergency_switch:
                            print("Crane has already moved and besides an emergency stop has been previously initiated! You have to continue before you can proceed to drop-off.")
                            dropped_in_shipping_container = True
                            emergency_switch = True
                            is_returned = False
                        elif not dropped_in_shipping_container and emergency_switch:
                            print("There has been an emergency stop! so crane cannot drop-off. To drop-off you must first continue and then drop-off.")
                            dropped_in_shipping_container = False
                            emergency_switch = True
                            is_returned = False
                    else:
                        print("Crane cannot drop-off when it has returned for a start already. Please start the crane again, pickup, move then you can drop-off.")
                        is_returned = True
                        is_picked_up = False
                        is_started = False
                        is_moving = False
                        dropped_in_shipping_container = False
                        emergency_switch = False

                # elif is_started == True and is_moving == False:
                #     print("There has been an emergency stop! so crane cannot drop-off. To drop-off you must first resume to continue.")
                #     emergency_switch = True

                else:
                    print("You cannot drop-off when you haven't moved the crates or finished moving the crates")
                    is_started = True
                    is_picked_up = True
                    is_moving = False
                    dropped_in_shipping_container = False
                    is_returned = False
                    emergency_switch = False

            # elif is_started == True and is_picked_up == False and emergency_switch == True:
            #     print("There has been an emergency stop! so crane cannot drop-off. To drop-off you must first continue and then move.")
            #     emergency_switch = True
            #     is_moving = False
            #     dropped_in_shipping_container = False
            #     is_returned = False
            else:
                print("You cannot drop-off when you have not picked up the crates in the first place. Please pickup and move, then you can drop-off")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        elif is_started == False and emergency_switch == True:
            print("There has been an emergency stop! so crane cannot drop-off. To drop-off you must first resume.")


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
                            is_started = False
                            is_moving = False
                            is_picked_up = False
                            dropped_in_shipping_container = False
                        # elif is_returned and not emergency_switch:
                        #     print("Crane has already dropped off the crates and successfully returned back to start.")
                        #     is_returned = True
                        #     emergency_switch = False
                        #     is_started = False
                        #     is_moving = False
                        #     is_picked_up = False
                        #     dropped_in_shipping_container = False
                        elif not is_returned and emergency_switch:
                            print("There has been an emergency stop! so crane cannot return. To return you must first resume and then return.")
                            is_returned = False
                            emergency_switch = True
                            is_started = True
                            is_moving = True
                            is_picked_up = True
                            dropped_in_shipping_container = True

                        # elif is_returned and emergency_switch:
                        #     print("Crane has already returned and besides an emergency stop has been previously initiated! You have to continue before you can proceed to start.")
                        #     is_returned = True
                        #     emergency_switch = True
                        #     is_started = False
                        #     is_moving = False
                        #     is_picked_up = False
                        #     dropped_in_shipping_container = False
                    # elif is_started == True and dropped_in_shipping_container == False and emergency_switch == True:
                    #     print("There has been an emergency stop! so crane cannot return. To return you must first resume to continue.")
                    #     emergency_switch = True
                    else:
                        print("Crane has not dropped-off in the shipping container and cannot return. Please drop-off first before you return.")
                        is_started = True
                        is_picked_up = True
                        is_moving = True
                        dropped_in_shipping_container = False
                        is_returned = False
                        emergency_switch = False

                # elif is_started == True and is_moving == False and emergency_switch == True:
                #     print("There has been an emergency stop! so crane cannot return. To return you must first resume to continue.")
                #     emergency_switch = True
                else:
                    print("You cannot return when you haven't even moved the crates or finished moving the crates")
                    is_started = True
                    is_picked_up = True
                    is_moving = False
                    dropped_in_shipping_container = False
                    is_returned = False
                    emergency_switch = False

            # elif is_started == True and is_picked_up == False and emergency_switch == True:
            #     print("There has been an emergency stop! so crane cannot return. To return you must first resume to continue.")
            #     emergency_switch = True
                # is_moving = False
                # dropped_in_shipping_container = False
                # is_returned = False

            else:
                print("You cannot return when you have not picked up the crates in the first place. Please pickup, move, and drop-off then you can return")
                is_started = True
                is_picked_up = False
                is_moving = False
                dropped_in_shipping_container = False
                is_returned = False
                emergency_switch = False
        elif is_started == False and is_returned == True:
            print("Crane has already returned back  before to start over. Crane can only start.")
            # print("You cannot return when you haven't even started the crane. Please start the crane, pickup, move, drop-off then you can return.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False
        elif is_started == False and emergency_switch == True:
            print("There has been an emergency stop! so crane cannot return. To return you must first resume.")
        else:
            print("Crane has already returned back before to start. Crane can only start. Please start.")
            is_started = False
            is_picked_up = False
            is_moving = False
            dropped_in_shipping_container = False
            is_returned = False
            emergency_switch = False

    elif input_state == "emergency" or input_state == "stop" or input_state == "resume":
        if input_state == "emergency":
            if is_started:
                if not emergency_switch:
                    print("[ALERT!!!] EMERGENCY HAS BEEN INITIATED TO THE CRANE. To resume type 'resume'.")
                    is_started = False
                    emergency_switch = True
                else:
                    print("EMERGENCY switch has already been turned on before. Please resume to leave EMERGENCY mode")
                    is_started = False
                    emergency_switch = True

            else:
                print("Emergency cannot be done if crane has not started.Please start Crane first to initiate an emergency.")
                is_started = False
                emergency_switch = False

        elif input_state == "stop":
            if is_started:
                if not emergency_switch:
                    print("Crane has been stopped. To resume type 'resume'.")
                    is_started = False
                    emergency_switch = True
                else:
                    print("Crane has already been stopped.")
                    is_started = False
                    emergency_switch = True
            else:
                print("Crane cannot stop when it hasn't even started.")
                is_started = False
                emergency_switch = False


        elif input_state == "resume":
            if not is_started:
                if emergency_switch:
                    print("Emergency/stop has ended and Crane has successfully resumed.")
                    is_started = True
                    emergency_switch = False
                else:
                    print("Crane cannot resume because it has not started. Please start Crane first and then initiate an emergency/stop to resume")
                    is_started = False
                    emergency_switch = False
            else:
                print("Emergency/stop has already ended. Please go on with your crane.")
                is_started = True
                emergency_switch = False
    else:
        print("Enter valid input. Either you Start, Pickup, Moving, drop-off, or stop(Emergency break")



