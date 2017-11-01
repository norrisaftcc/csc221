# csc 221
# m4 - timing example 2
# runs with examples seen on 10/30
# norrisa

"""
Prints running time for problem sizes
These sample problems simply double in size
original is from Lambert's "Fundamentals of Python: Data Structures"
"""

import time

def main():
    problemSize = 1000000 # 1 million
    #alg = do_algorithm
    alg = constant_alg
    measure(alg,problemSize)
    print ('constant complexity')
    alg = constant_alg
    measure(alg, problemSize) # ** 2)

    print ('logarithmic complexity')
    alg = log_alg
    measure(alg, problemSize) # ** 2)

    print ('linear complexity')
    alg = linear_alg
    measure(alg, problemSize)

    print ('quadratic complexity')
    alg = quad_alg
    measure(alg, 100)

    print ('exponential complexity')
    alg = exp_alg
    measure(alg, 2)


def measure(alg, problemSize):
    """ measure runtime of function alg on a problem
    of size problemSize, problemsize*2... up to *16"""

    print("%12s%16s" % ("Problem Size", "Seconds"))
    for count in range(5):
        start = time.time()
        # algorithm work begins
        alg(problemSize)
        # algorithm work ends
        elapsed = time.time() - start

        print("%12d%16.4f" % (problemSize, elapsed))
        problemSize *= 2 # doubled
    print("Finished\n")


# constant complexity (most of these are uninteresting)

def constant_alg(size):
    """ constant running time """
    work = 1
    work -= 1
    work += 1

# log complexity

def log_alg(size):
    """ convert integer to string. runtime increases with the
    number of digits, which is log10 """
    # intToStr
    i = size
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result

# linear complexity

def linear_alg(problemSize):
    """ a dummy algorithm of the given size.
    complexity grows linearly as it's a single loop """
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1

def linear_alg_2(problemSize):
    """ add characters in a string, string must contain
    decimal digits. also linear runtime. """
    # add_digits
    s = str(problemSize)
    val = 0
    for char in s:
        val += int(char)
    return val

def linear_alg_3(problemSize):
    """ iterative factorial """
    # fact_iter
    n = problemSize
    product = 1
    for i in range (1, n+1):
        product *= 1
    return product

def linear_alg_4(problemSize):
    """ recursive factorial. assume n >= 0"""
    # fact_recur
    def fact_recur(n):
        if n <= 1:
            return 1
        else:
            return n*fact_recur(n - 1)
    fact_recur(problemSize)

# log-linear (log times linear)
# many practical algs use this -- we'll return to it
# example: merge sort

# polynomial complexity
# ex. quadratic complexity

def quad_alg(problemSize):
    work = 1
    for i in range(problemSize):
        for j in range(problemSize):
            work -= 1
            work += 1

# exponential complexity
def exp_alg(problemSize):
    problemSize = 2 ** problemSize
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1


# begin
main()
        
