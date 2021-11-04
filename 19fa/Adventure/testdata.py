# -*- coding: utf-8 -*-
"""
Ideas for text adventure data structures
"""

# we could use lists
kitchen = ["Kitchen","This is the kitchen"]
livingRoom = ["Living Room","There's a dusty sofa here."]
bedroom = ["Bedroom","There is a creepy doll here."]

rooms = [kitchen, livingRoom, bedroom]

for room in rooms:
    print("You are in", room[0])
    print("Description:", room[1])
    print()
    print("Moving to next room...")
    
# we could use dictionaries
kitchenDescription = "This is the kitchen"
kitchenExits = {"east":"Living Room"}
kitchenInfo = [kitchenDescription, kitchenExits]

lrDescription = "There's a dusty sofa here."
lrExits = {
                "west":"Kitchen",
                "south":"Bedroom"}
lrInfo = [lrDescription, lrExits]

bedroomDescription = "There is a creepy doll here."
bedroomExits = {"north":"Living Room"}
bedroomInfo = [bedroomDescription, bedroomExits]
    
roomDict = {
        "Kitchen": kitchenInfo,
        "Living Room": lrInfo,
        "Bedroom": bedroomInfo
        }


