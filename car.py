carStarted = False
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if carStarted:
            print("Car is already started!")
        else:
            print("Car started")
            carStarted = True

    elif command == "stop":
        if not carStarted:
            print("Car is already stopped!")
        else:
            print("Car has stopped")
            carStarted = False

    elif command == "help":
        print("""
start - 
stop - 
quit - 
        """)
    elif command == "quit":
        break
    else:
        print("Sorry wrong")
