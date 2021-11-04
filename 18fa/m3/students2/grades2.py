# -*- coding: utf-8 -*-
"""
grades1
norrisa
2nd attempt at reading students.csv
using a dictionary
"""

def read_students(filename):
    """
    input: filename, a string
    output: list of names and a dictionary mapping names to grades
    """
    names = []
    grades = {}
    gradesFile = open(filename,'r')
    for line in gradesFile:
        # each line has multiple items
        record = line.strip().split(',')
        name = record[0]
        grade = record[2]
        # add the name to name list
        names.append(name)
        grades[name] = grade
        
    gradesFile.close()
    return names, grades

def main():
    
    names, grades = read_names('students.csv')

    # loop through students
    for student in names:
        print (student)
    
    
if __name__ == "__main__":
    main()

