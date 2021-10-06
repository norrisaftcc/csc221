# Item class

class Item:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    """
     
    def __init__(self, name, description):
         self.name = name
         self.description = description
         
    def __str__(self):
        return self.name + " : " + self.description
        
        
        

# Test code
def main():
    key = Item("key", "It's a bit rusty.")
    
    sword = Item("sword", "It's very shiny.")
    
    stuff = [key, sword]
    for item in stuff:
        print(item)
        
if __name__ == "__main__":
    main()
