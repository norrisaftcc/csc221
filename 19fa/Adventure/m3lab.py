from room import Room

kitchen = Room("Kitchen","A kitchen.")
bedroom = Room("Bedroom","A bedroom.")
livingRoom = Room("Living Room","Filled with dust.")

house = [kitchen, bedroom, livingRoom]

for room in house:
    print("Moving to a new room...")
    print (room)
    
