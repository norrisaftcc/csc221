# -*- coding: utf-8 -*-
"""
The Student class.
"""

class Student(object):
    
  
    def __init__(self, id, firstName, lastName, program, gpa):
        """ constructor """
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.program = program
        self.gpa = gpa
        
    
    def __str__(self):
        """ string representation """
        text = str(self.id) + " " + self.firstName + " " + self.lastName
        text += " " + self.program + " " + str(self.gpa)
        return text
    

