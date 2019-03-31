# -*- coding: utf-8 -*-
"""
model5.py created on Wed Feb 13 20:23:59 2019

@author: Danielle Sinnett, student number 200827672

This is the fifth version of the agent based modelling portfolio.
It sets up ten agents, walks them one hundred steps in a 100 x 100 grid, eat
from their environment, share with their neighbours and then plots their final
location in the environment.

To run it:
1. Download this file
2. Download the agent class (agentframework.py) and the input data (in.txt)
   and save them in the same folder as this file
3. Open this file with the Python Shell
4. Select Run, then Run Module

This will display the distance between the ten agents. A pop up box will also
appear displaying the finishing locations of the agents in their environment
on Figure 1.

You will then be returned to the command prompt.

Copyright (c) School of Geography,
University of Leeds, Leeds, West Yorkshire, LS2 9JT
All rights reserved.

This code is provided under the Academic Academic Free License v. 3.0.
For details, please see the http://www.opensource.org/licenses/AFL-3.0.
@author: de-sinnett
"""
# Import random, operator, plotting, timer and csv modules, and Agent Class
import random
import operator
import matplotlib.pyplot
import time
import agentframework
import csv

# Start the clock
start = time.clock()

# Open the input file
f = open('in.txt')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Create an empty list
environment = []

# Read in input data
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

# Create a new empty list
agents = []

# Control how many agents
num_of_agents = 10

# Control number of iterations
num_of_iterations = 100

# Control size of neighbourhood
neighbourhood = 20

# Set up agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents, make them eat, and share with neighbours
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Stop the clock
end = time.clock()
print("time = " + str(end - start))

# Plot the agents and environment
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
