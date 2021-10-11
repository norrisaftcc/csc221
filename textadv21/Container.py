# Container class
# should be able to add, remove, list, and 
# (optionally) transfer items
#
# we moved using a dictionary so we can easily
# do name lookups
from Item import Item

class Container:
    """ This class only handles collections of Items. """
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
        self.contents[item.name] = item
        
    def remove(self, item):
        if item in self.contents:
            self.contents.remove(item)

    def moveItemTo(self, item, destination):
        
        destination.add(item)
        self.remove(item)
        
    def listContents(self):
        for key in self.contents:
            print(key)
 
        
def main():
     """ test code"""
     
     
 
    
 
if __name__ == "__main__":
    main()
     
     
     