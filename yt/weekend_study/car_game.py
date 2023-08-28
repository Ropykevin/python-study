# car game
# help
# start
# stop
# quit
# "idon t understand that "
command=""
started=False
while True !="quit":
    command=input("> ").lower()
    if command=="start":
        if started:
            print(" car is already started")
        else:
            started=True
            print("car started...")
    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit the game           
        """)
    elif command=="stop":
        if not started:
            print(" car already stopped")
        else:
            started=False
            print("car stopped.")
    elif command=="quit":
        print("quit successfuly")
        break
    else:
        print("I don't understand you")
