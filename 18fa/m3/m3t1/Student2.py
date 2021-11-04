# -*- coding: utf-8 -*-
"""
The Student class. 
This version uses Java style getters and setters
"""

class Student(object):
    
  
    def __init__(self, id, firstName, lastName, program, gpa):
        """ constructor """
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._program = program
        self._gpa = gpa
        
    
    def __str__(self):
        """ string representation """
        text = str(self._id) + " " + self._firstName + " " + self._lastName
        text += " " + self._program + " " + str(self._gpa)
        return text
    
    # getters and setters
    def getId(self):
        return self._id
    
    def setId(self, id):
        self._id = id
        
    def getFirstName(self):
        return self._firstName
    
    def setFirstName(self, firstName):
        self._firstName = firstName
        
    def getLastName(self):
        return self._lastName
    
    def setLastName(self, lastName):
        self._lastName = lastName
    

