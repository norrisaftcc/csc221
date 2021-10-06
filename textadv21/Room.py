# CSC 221
# Text Adventure
# norrisa
# 10/1/21



class Room:
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    """

    def __init__(self):
        """ Initialize an empty room"""
        self.name = "Empty Room"
        self.description = "No description"
        self.exits = {}

        
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        return text

 #   def __repr__(self):  # we're not using this yet
 #       pass


    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.             
            
            



def main():
    """
    Currently used for testing.
    TODO: uimplement doctests. """
    bedroom = Room( "Bedroom", 
                   "This is an average bedroom.",
                   { "North": "Bathroom",
                     "South": "Living Room"} )
    
    #print(bedroom)
    
    livingRoom = Room ( "Living Room",
                       "A TV, sofa, and game console are here.",
                       { "North" : "Bedroom" } )
    #print(livingRoom)
    
    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { bedroom.name: bedroom, 
                livingRoom.name: livingRoom}
    
    # Test out movement
    loc = bedroom
    print("Starting room:")
    loc.describe()
    
    print ("Heading South...")
    loc = roomDict[loc.exits["South"]] # find room to South, go there
    loc.describe()
    
    print ("Heading North...")
    loc = roomDict[loc.exits["North"]] # find room to North, go there
    loc.describe()

if __name__ == "__main__":
    main()
