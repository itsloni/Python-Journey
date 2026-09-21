# TECHNICAL ASSESSMENT: RIDE-SHARE FARE CONTROLLER
#
# Interviewer Prompt:
# "We need you to build a terminal-based system for a ride-share driver's app.
# The app tracks whether a driver is currently on a trip or waiting for a passenger.
# It needs to handle starting a ride, applying traffic surge multipliers, ending
# a ride to calculate fares, and handling cancellations safely. Make sure you
# track states carefully so a driver can't cheat the system or cause a crash.
# Let's see your code."

active_trip = False
active_surge = False
surge_price = 0
base_fares = 20

while True:
    status = input("> ").lower()
    if status == "start" or status == "end" or status == "drop-off":
        if status == "start":
            if not active_trip:
                print("Driver enroute")
                active_trip = True
                # while True:
                #     surge_cost = input("Enter your surge cost if applicable: ")
                if not active_surge:
                    surge_cost = input("I sthere currently a surge? enter (Y)/(N): ")
                    if surge_cost == "Y":
                        # surge_cost = int(surge_cost)
                        surge_price += 10
                        print("Surge cost locked in.")
                        active_surge = True

                    elif surge_cost == "N":
                        print("alright no surge.")
                        active_surge = False
                    else:
                        print("Please enter a valid response, (Y)/(N).")
            else:
                print("Driver already enroute.")

        elif status == "end" or status == "drop-off":
            if active_trip:
                if active_surge:
                # if not active_trip:
                    total_fares = base_fares + surge_price
                    print(f"Your ride has ended and your Total price is ${total_fares}")
                    break
                    # else:
                    #     print("You can't end/drop-off. You can only cancel.")
                else:
                    total_fares = base_fares
                    print(f"Your ride has ended and your Total price is ${total_fares}")
                    break
            elif not active_trip:
                print("You can't end/drop-off. You can only cancel.")
    elif status == "waiting":
        if active_trip:
            # if active_surge:
            print("Waiting for passenger")
            active_trip = False
            # active_surge = False
            # else:
            #     print("Already Waiting for passenger")
        else:
            print(" Car never stopped to wait, or is already waiting for passenger.")
    elif status == "continue" or status == "pickup":
        if not active_trip and not active_surge:
            fares += 20
            print("Driver has picked passenger and continued")
            active_surge = True
        else:
            print("Driver never waited or Driver has already picked the passenger. Pls confirm and try again.")

    elif status == "cancel":
        if active_trip:
            print("Cancelling ride")
            fares = 0
            print(f"Your ride has ended and your Total price is ${fares}")
            active_trip = False
            active_surge = True
            break
        else:
            print("Already Canceled.")

    # elif status == "end" or status == "drop-off":
    #     if active_trip and not active_surge:
    #         if not active_trip:
    #             total_fares = fares + surge_price
    #             print(f"Your ride has ended and your Total price is ${total_fares}")
    #             break
    #         else:
    #             print("You can't end/drop-off. You can only cancel.")
    #     else:
    #         print("You can't end/drop-off. You can only cancel.")
    else:
        print("Invalid input")




