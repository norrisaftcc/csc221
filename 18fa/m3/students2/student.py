# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:21:54 2018

@author: norrisa8373
"""

class Student:
    def __init__(self, first_name, last_name, numCredits, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.numCredits = numCredits
        self.gpa = gpa
        
    def __str__(self):
        return self.first_name, self.last_name, self.numCredits, self.gpa
