#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:42:11 2017

@author: norrisa

base classes for the MazeBuilder application
"""
NORTH = 'n'
SOUTH = 's'
EAST  = 'e'
WEST  = 'w'

class Maze(object):
    """ a maze has:
        contents that are implementation specific
        a current cell (that the player is in)
        a getter and setter for that current cell)
    """
    def __init__(self):
        self.contents = None
        self.currentCell = None

    def getCurrentCell(self):
        return self.currentCell

    def setCurrentCell(self, cell):
        self.currentCell = cell

class OneRoomMaze(Maze):
    """ a one room maze contains only one cell """
    def __init__(self):
        self.currentCell = Cell(0,0)
        self.contents = self.currentCell

    #def getCurrentCell(self):
    #    pass

    #def setCurrentCell(self):
    #    pass
    
class ListMaze(Maze):
    """ a one-dimensional maze using a python list to store cells """
    def __init__(self, numCells = 4):
        # initialize list of cells
        contents = []
        for i in range(numCells):
            # set x coordinate (y coord is always zero)
            contents.append(Cell(i, 0))
        # start at the beginning
        self.currentCell = contents[0]
        self.currentCellNum = 0
    
    def getCurrentCell(self):
        pass
    
    def getCurrentCellNum(self):
        return self.currentCellNum
    
    def setCurrentCell(self, cell):
        # note: if you pass it a cell not already in the maze
        # this breaks the internal consistency of the maze
        # (and raises ValueError when trying to set currentCellNum)
        self.currentCell = cell
        self.currentCellNum = self.contents.index(cell)
    
    def setCurrentCellNum(self, cellNum):
        # set the current cell by number
        # todo: handle bad input (for a cellNum not found)
        self.currentCellNum = cellNum
        self.currentCell = self.contents[cellNum]
    

class Cell(object):
    """ A cell has:
        a row and column location
        a list of linked cells
        a north/south/east/west neighbors,
        stored in a dictionary
        (neighbors are not necessarily linked,
        if your west neighbor is not in links,
        that means there is a wall in the way)
        
    """
    def __init__(self, row= -1, col= -1):
        self.row = row
        self.col = col
        self.links = []
        self.neighbors = {}
    def __str__(self):
        return "cell@ ("+str(self.row)+","+str(self.col)+")"
    # accessors for row/col    
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    # getters/setters for neighbors
    def get_neighbor(self, dir):
        # setdefault returns the value, or None
        # if not present
        if dir in self.neighbors.keys():
            return self.neighbors[dir]
        
    def set_neighbor(self, dir, cell):
        self.neighbors.setdefault(dir,cell)
    

# test samples
# part 1: cell
c1 = Cell(0,0)
c2 = Cell(0,1)
c2.set_neighbor('n',c1)
c1.set_neighbor('s',c2)

# part 2: OneRoomMaze
mazeOneRoom = OneRoomMaze()

# part 3: ListMaze
mazeFiveRooms = ListMaze(5)
