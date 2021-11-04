
# room.py
# the Room class

# example of use
# kitchen = Room("Kitchen","it's a kitchen")

class Room:
    """ The Room object """
    def __init__ (self, name, description):
        """ create a room object """ 
        self.name = name
        self.description = description
    

    def __str__ (self):
        """ create human readable version """ 
        readable = "Name: " + self.name
        readable += "\n" # new line
        readable += "Description: " + self.description
        return readable

