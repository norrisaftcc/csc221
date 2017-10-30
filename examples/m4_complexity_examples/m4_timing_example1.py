# csc 221
# m4 - timing example 1
# norrisa

"""
Prints running time for problem sizes
These sample problems simply double in size
from Lambert's "Fundamentals of Python: Data Structures"
"""

import time

def main():
    problemSize = 1000000 # 1 million
    # this use of print() plugs in variables into %
    # much like format() does
    print("%12s%16s" % ("Problem Size", "Seconds"))
    for count in range(5):
        start = time.time()
        # algorithm work begins
        do_algorithm(problemSize)
        # algorithm work ends
        elapsed = time.time() - start

        print("%12d%16.3f" % (problemSize, elapsed))
        problemSize *= 2 # doubled
    print("Finished")


def do_algorithm(problemSize):
    """ a dummy algorithm of the given size. """
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1

# begin
main()
        
