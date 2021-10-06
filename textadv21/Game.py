# CSC 221
# Text Adventure
# norrisa
# 10/1/21

from Room import Room
#import Player


"""
Version history:
    v1 - built using Room references (basically a graph). 
        downside: you have to create all rooms, then link
        them together afterwards.
        
    v2 - used constant room IDs to make it possible to add
        and link rooms in one pass. 
        downside: "this looks like BASIC" (from the peanut gallery)
        
    v3 - realization: if the Room names are unique, that's a
        unique ID. I therefore changed
        the container for all Rooms to be a dictionary --
        now it's easy enough to look up the room by name.


"""

class Game:
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
      (TODO: Read these from a file in future)
    - call loop()
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        #self.player = player.Player()
        self.rooms = { } # stored in dictionary
        self.here = None # TODO: move this to Player
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
     

    def __str__(self):
        pass

    def __repr__(self):
        pass


    def setup(self):
        """ setup(): create a graph of rooms for play. """
        # just a test -- needs work
        bedroom = Room( "Bedroom", 
                   "This is an average bedroom.",
                   { "north": "Bathroom",
                     "south": "Living Room"} )
    
        #print(bedroom)
        
        livingRoom = Room ( "Living Room",
                           "A TV, sofa, and game console are here.",
                           { "north" : "Bedroom" } )
        #print(livingRoom)
        
        bathroom = Room ( "Bathroom", 
                         "Somebody left the toothpaste uncapped again.",
                         { "south" : "Bedroom" } )
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        self.rooms = { bedroom.name: bedroom, 
                    livingRoom.name: livingRoom,
                    bathroom.name: bathroom }
        
        self.here = bedroom # starting location

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            # Can we go in the chosen direction from here?
            if self.here.exits.get(direction) == None:
                print("You can't go that way.")
            else:   
                # this key does exist
                newRoomName = self.here.exits[direction]
                newRoom     = self.rooms[newRoomName]
                self.here   = newRoom
                if self.isVerbose:
                    self.here.describe()
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        
        else: # first word is verb
            print("I don't know how to", words[0])


def main():
    game = Game()
    game.setup()
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
