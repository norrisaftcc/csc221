# house.py
# a House contains Rooms

from room import Room



class House:
    ''' a House contains multiple Room objects '''

    def __init__(self):
        ''' create the house '''
        start = Room("The Void","You should never see this room...")
        livingRoom = Room("Living Room","Filled with dust.")
        diningRoom = Room("Dining Room","Filled with dust.")
        hall = Room ("Hall","There is an old clock here.")
        den = Room ("Den","Filled with old sofas.")
        kitchen = Room("Kitchen","A kitchen.")

        self.rooms = [start, livingRoom, diningRoom, hall, den, kitchen]
        

        
        
