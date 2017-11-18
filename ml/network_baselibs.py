# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:07:18 2017

@author: norrisa

simple neural network (baseball) using std python libraries
"""

# calculate weighted sum
def w_sum(a,b):
    assert(len(a) == len(b))
    
    output = 0
    
    for i in range(len(a)):
        output += (a[i] * b[i])
    
    return output

weights = [0.1, 0.2, 0]

def neural_network(input, weights):
    
    pred = w_sum(input, weights)
    
    return pred

toes  = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# input corresponds to every entry
# for first game of the season
input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network (input, weights)

print(pred)