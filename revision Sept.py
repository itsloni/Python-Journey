started = False

while True:
    command = input("> ").lower()
    command.lower()
    if command == "start":
        if started:
            print("Car has already started Papi")
            # started = False
        else:
            started = True
            print("Car Started..Ready to go!")

    elif command == "stop":
        if not started:
            print("Car wasn't even started, so it already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")







