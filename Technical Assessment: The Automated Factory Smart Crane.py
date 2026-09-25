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

while True:
    input_state = input("> ").lower()
    if input_state == "start":
        if not is_started:
            print("Smart crane started, getting ready to pickup")
            is_started = True
        else:
            print("Crane has already started. Proceed by picking up.")
    elif input_state == "pickup":
        if is_started:
            if not is_picked_up and not is_moving:
                print("Crates has been picked up from the conveyor belt and is getting ready to start moving")
                is_picked_up = True
            else:
                print("Crane has already Picked-up. Proceed by Moving the crates.")



