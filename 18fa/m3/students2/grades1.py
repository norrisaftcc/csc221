# -*- coding: utf-8 -*-
"""
grades1
norrisa
first attempt at reading students.csv
"""

def read_names(filename):
    """
    input: filename, a string
    output: list of names and list of grades
    """
    names = []
    grades = []
    gradesFile = open(filename,'r')
    for line in gradesFile:
        # each line has multiple items, we only want name
        record = line.strip().split(',')
        # print(record)
        names.append(record[0])
        grades.append(record[2])
    gradesFile.close()
    return names, grades

def main():
    
    names, grades = read_names('students.csv')
    # sort the grades
    #grades.sort()
    
    # loop through students
    for i in range(0, len(names)):
        print(names[i],"\t",grades[i])
    
if __name__ == "__main__":
    main()

