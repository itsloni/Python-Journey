prompt = ""
Help = """ 
start - to start the car
stop - to stop the car
quit - to exit 
"""
start =  "Car started....Ready to go !"
stop = "Car stopped."
is_started = False


while prompt != "quit":   # You can just say While True:
    prompt = input(">").lower()
    if prompt == "start":
        if not is_started:
            print(start)
            is_started = True
        else:
            print("The Car has already started you dimwit!")
    elif prompt == "stop":
        if is_started:
            print(stop)
            is_started = False
        else:
            print("The Car has already stopped you dimwit!")
    elif prompt == "help":
        print(Help)
    elif prompt == "quit":
        break
    else:
        print("I don't understand that...")




