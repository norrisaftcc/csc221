# MyGame - implements game specific functions
from Game import Game
from Room import Room
from Player import Player
from Item import Item



class MyGame(Game):
    """ the Game class should be subclassed to add
    game specific features, including the world setup. 
    """
    
    def setup(self):
        """ Load your own rooms in the method of your choosing.
        Consider a GameLoader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms = loader.setup()
        
        # starting location
        self.here = self.rooms["Bedroom"]
        # Let's do a turn 1 look , to orient the player
        self.here.describe()
        
        
    
        
    
    
    
    
    
class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate file.
    """
    def setup(self):
        bedroom = Room( "Bedroom", 
           "This is an average bedroom.",
           { "north": "Bathroom",
             "south": "Living Room"} )
    
        #print(bedroom)
        
        livingRoom = Room ( "Living Room",
                           "A TV, sofa, and game console are here.",
                           { "north" : "Bedroom",
                            "east" : "Kitchen" } )
        #print(livingRoom)
        
        bathroom = Room ( "Bathroom", 
                         "Somebody left the toothpaste uncapped again.",
                         { "south" : "Bedroom" } )
        
        kitchen = Room ("Kitchen",
                        "There are the usual appliances, but no food.",
                        {"west" : "Living Room"} ) 
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        rooms = { bedroom.name: bedroom, 
                    livingRoom.name: livingRoom,
                    bathroom.name: bathroom,
                    kitchen.name: kitchen }
        
        # Add some items to the rooms
        phone = Item("phone","it's yours.")
        bedroom.addItem(phone)
        
        key = Item("key", "for the front door.")
        kitchen.addItem(key)
        
        sword = Item("sword","best $20 you spent at the flea market.")
        livingRoom.addItem(sword)
                
        return rooms 
        
        
# Startup
def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()

