command = ""
started = False
while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Starting car")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Stopping the car")
    elif command == "help":
        print("""
              START - TO START THE CAR
              STOP - TO STOP THE CAR
              QUIT - TO QUIT THE GAME
              """)
    elif command == "quit":
        break
    
    else:
        print("Enter correct command!")    
    