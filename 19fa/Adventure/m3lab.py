from room import Room

start = Room("The Void","You should never see this room...")
livingRoom = Room("Living Room","Filled with dust.")
diningRoom = Room("Dining Room","Filled with dust.")
hall = Room ("Hall","There is an old clock here.")
den = Room ("Den","Filled with old sofas.")
kitchen = Room("Kitchen","A kitchen.")


house = [start, livingRoom, diningRoom, hall, den, kitchen]

for room in house:
    print("Moving to a new room...")
    print (room)
    
    
