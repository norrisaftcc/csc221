# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:30:40 2017

@author: noyesc0779
"""

# maze2

class Maze(object):
    """ a maze has:
        contents that are implementation specific
        a current cell (that the player is in)
        a getter and setter for that current cell)
    """
    def __init__(self):
        self.contents = []
        self.currentCell = None

    def getCurrentCell(self):
        return self.currentCell

    def setCurrentCell(self, cell):
        self.currentCell = cell



class Cell(object):
    """ A cell has:
        an id
        a list of linked cells
    """
    def __init__(self, id='No Name'):
        self.id = id
        self.prev = None
        self.next= None
    def __str__(self):
        return "cell@ ("+str(self.id)+")"
    # accessors for id  
    def get_id(self):
        return self.id
    
    def link_next(self, cell):
        self.next = cell
    
    def link_prev(self, cell):
        self.prev = cell
    
    # unlink not implemented
    

c1 = Cell(1)
c2 = Cell(2)
c1.link_next(c2)
c2.link_prev(c1)

m = Maze()
m.contents.append(c1)
m.contents.append(c2)

# test
myLoc = c1
print(myLoc)
myLoc = myLoc.next
print(myLoc)
myLoc = myLoc.prev
print(myLoc)