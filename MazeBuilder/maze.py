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
c1 = Cell(0,0)
c2 = Cell(0,1)
c2.set_neighbor('n',c1)
c1.set_neighbor('s',c2)