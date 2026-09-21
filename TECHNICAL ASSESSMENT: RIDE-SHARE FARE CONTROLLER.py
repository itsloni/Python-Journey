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
picked_passenger = False
waited_for_passenger = False
surge_price = 0
base_fares = 20

while True:
    status = input("> ").lower()
    if status == "start" or status == "end" or status == "drop-off":
        if status == "start":
            if not active_trip:
                print("Driver enroute")
                active_trip = True
                while True:
                    surge_cost = input("Is there currently a surge? enter (Y)/(N): ").lower()
                    if not active_surge:
                        if surge_cost == "y":
                            surge_price += 10
                            print("Surge cost locked in.")
                            active_surge = True
                            break
                        elif surge_cost == "n":
                            print("alright no surge.")
                            active_surge = False
                            break
                        else:
                            print("Please enter a valid response, (Y)/(N).")
            else:
                print("Driver already enroute.")

        elif status == "end" or status == "drop-off":
            if active_trip and picked_passenger:
                if active_surge:
                    total_fares = base_fares + surge_price
                    print(f"Your ride has ended and your Total price is ${total_fares}")
                    break
                else:
                    total_fares = base_fares
                    print(f"Your ride has ended and your Total price is ${total_fares}")
                    break
            else:
                print("You can't end/drop-off. You can only cancel.")

    elif status == "waiting":
        if active_trip:
            if not waited_for_passenger:
                print("Waiting for passenger")
                active_trip = True
                waited_for_passenger = True
            else:
                print("Already Waiting for passenger or picked up passenger already. Please confirm and try again.")
        else:
            print(" Car never stopped to wait, or is already waiting for passenger.")

    elif status == "continue" or status == "pickup":
        if active_trip and waited_for_passenger == True:
            if picked_passenger == False:
                print("Driver has picked passenger and continued")
                # active_trip = True
                picked_passenger = True
            else:
                print("Driver has already picked the passenger. Pls confirm and try again.")
        else:
            print("Driver never waited or Driver has already picked the passenger. Pls confirm and try again.")

    elif status == "cancel":
        if active_trip:
            if picked_passenger == True:
                driver_response = input("""
Are you sure?, You currently have a passenger with you.
be sure to know that you will loose your money!")(Y)/(N): 
""").lower()
                if driver_response == "y":
                    fares = 0
                    print("Cancelling ride.")
                    print(f"Your ride has ended and your Total price is ${fares}")
                    active_trip = False
                    break
                elif driver_response == "n":
                    print("Alright you Just go on with the ride, when you reach destination you end.")
                else:
                    print("Please enter invalid response.")
            else:
                driver_response = input("Beware,You haven't gotten a passenger. Are you sure? (Y)/(N): ").lower()
                if driver_response == "y":
                    print("Cancelling ride.")
                    fares = 0
                    print(f"Your ride has ended and your Total price is ${fares}")
                    active_trip = False
                    break
                elif driver_response == "n":
                    print("Alright you Just go on with the ride, when you reach destination you end.")
                else:
                    print("Please enter invalid response.")
        else:
            print("Already Canceled.")

    else:
        print("Invalid input")




