# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:14:40 2017

@author: norrisa

as previous network, but simplified
by the use of the numpy library
(in particular, the dot product function)
"""

import numpy as np

weights = np.array([0.1, 0.2, 0])

def neural_network(input, weights):
    pred = input.dot(weights)
    return pred

toes  = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

# input corresponds to every entry
# for first game of the season
input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network (input, weights)

print(pred)
