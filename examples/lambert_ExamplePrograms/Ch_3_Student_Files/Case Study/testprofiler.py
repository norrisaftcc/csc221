from profiler import Profiler
from algorithms import selectionSort, bubbleSort, bubbleSort2, insertionSort

p = Profiler()
'''
p.test(selectionSort, size = 15, comp = True,
       exch = True, trace = True)
'''
testSample = int(input('Size of list to test? '))

# test against multiple functions
algs = [selectionSort, bubbleSort, bubbleSort2, insertionSort]
for alg in algs:
    p.test(alg, size = testSample, comp = True,
       exch = True, trace = True)
    