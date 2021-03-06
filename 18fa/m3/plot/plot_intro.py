#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:51:30 2018

@author: norrisa
"""

# anaconda comes with matplotlib. if you're using idle you'll need to use
# pip to install it

from pylab import plot, show, savefig
import random

x = [1, 2, 3, 4]
y = [2, 3, 3, 4]

#myPlot = plot(x,y)
# if you generate multiple graphs, you need to use show() for each
# anaconda defaults to showing the final one, which is useful
# for testing a one-off plot. In general, use show()

# every time you call show() the existing plot is erased

#show()
a = []
b = []
for i in range(20):
    a.append(i)
    b.append(random.randint(0,10))
#myPlot = plot(x,y)
#show()
# we have many options for how our plot looks

    

# plot lines between points
#plot(a, b)
#show()

# plot lines between points, with round marker on points
#plot(a, b, marker='o')
#show()
# plot just the points with a x marker

plot(a, b, marker='x')
show()

# we'll save a plot to a png
# since we previously called show(), we need to make a new plot
plot(a, b, marker='x')
savefig("mygraph2.png")
