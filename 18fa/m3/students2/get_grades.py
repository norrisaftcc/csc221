# csv example

import csv

def read_csv(filename):
	""" 
	input: filename, a string
	output: list of names and list of GPAs
	"""
	studentNames = []
	studentGPAs = []
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			studentNames.append(row[0])
			studentGPAs.append(float(row[2]))
		return studentNames, studentGPAs

def findLowestGrade(grades):
    """
    input: list of grades
    output: the lowest value
    """
    #return min(grades)
    pass

def main():
	"""load file and print names and gpas"""
	names, grades = read_csv('students.csv')
	for i in range(0, len(names)):
        print('{0}\t{1}'.format(names[i],grades[i]))
    
    lowest = findLowestGrade(grades)
    print("lowest GPA is {0}".format(lowest))
		
if __name__ == '__main__':
	main()
	