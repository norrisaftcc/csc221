# -*- coding: utf-8 -*-
"""
CSC 221
M1LAB1 - Double a Number
Name
Date
"""
results = [] # this is global ... for now

def main():
    """Main loop of program."""
    print("This is the double a number program.")
    
    repeat = True
    while repeat == True:
        collectUserInput()
        repeat = repeatOrNot()
    print ("Goodbye.")
    print("Results:",results)
    
    
    
    
def collectUserInput():   
    """Ask user for input, double it, print result"""
    num = int(input("Enter a number: "))
    dbl = doubleANumber(num)
    results.append(num)
    print(num,"doubled is:", dbl)

def repeatOrNot():
    """returns True if the user wants to run again,
    False otherwise"""
    print("1. Enter another number")
    print("2. Exit")
    goAgain = int(input())
    if 1 == goAgain:
        return True
    return False

def doubleANumber(num):
    """input: one number. 
    output. the number * 2."""
    result = num * 2
    return result
    

# traditional magic to invoke main 
if __name__ == "__main__":
    main()
    
    