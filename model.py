# -*- coding: utf-8 -*-
"""
model.py created on Wed Feb 13 20:23:59 2019

@author: Danielle Sinnett, student number 200827672

This is the first version of the agent based modelling portfolio.
It sets up two agents, walks them one step in a 100 x 100 grid and
calculates the Euclidian distance between them.

To run it:
1. Download this file
2. Open it with the Python Shell
3. Select Run, then Run Module

This will display the starting locations of the variables at 50 50, the
the location of agents 1 and 2 after walking one step from randomly generated
starting locations, and the distance between them.

You will then be returned to the command prompt.

Copyright (c) School of Geography,
University of Leeds, Leeds, West Yorkshire, LS2 9JT
All rights reserved.

This code is provided under the Academic Academic Free License v. 3.0.
For details, please see the http://www.opensource.org/licenses/AFL-3.0.
"""
# Make the x and y variables
y0 = 50
x0 = 50
print (y0)
print (x0)

# Import random module
import random

# Set up variables to start at random coordinates in a 100x100 grid (agent 1)
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Random walk one step
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
print (y0, x0)

# Set up variables to start at random coordinates in a 100x100 grid (agent 2)
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Random walk one step
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
print (y1, x1)

# Calculate Euclidian distance between agents
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print (answer)
