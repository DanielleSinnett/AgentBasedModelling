# -*- coding: utf-8 -*-
"""
model4.py created on Wed Feb 13 20:23:59 2019

@author: Danielle Sinnett, student number 200827672

This is the fourth version of the agent based modelling portfolio.
It sets up ten agents, walks them one hundred steps in a 100 x 100 grid, eat
from their environment and then plots their final location in the environment.

To run it:
1. Download this file
2. Download the agent class (agentframework.py) and the input data (in.txt)
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
"""
# Import random, operator, plotting, timer and csv modules, and Agent Class
import operator
import matplotlib.pyplot
import time
import agentframework
import csv

# Start the clock
start = time.clock()

# Open the input data
f = open('in.txt')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Create an empty list
environment = []

# Read in inout data
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

# Define calculation for distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5

# Create a new empty list
agents = []

# Control how many agents
num_of_agents = 10

# Control number of iterations
num_of_iterations = 100

# Set up agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents, and make them eat
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# Calculate Euclidian distance between agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)

# Stop the clocl
end = time.clock()
print("time = " + str(end - start))

# Plot the agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)