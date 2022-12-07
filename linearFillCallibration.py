import numpy as np
import time
from ezGraph import *
from rStats import *

# Difference Model

#Parameters
dt = 1
nsteps = 30

l = 25
w = 50 
Qin = 30       
k = 0.0      

#Experimental Data
x_measured = [1,7,12,17,22,26]
y_measured = [0,10,20,30,40,50]
y_modeled = []

#Graph
graph = ezGraphMM(xmax = 100,
    ymin=0, ymax=100,
    x_measured = x_measured,
    y_measured = y_measured,
    xLabel="Time (s)",
    yLabel="Height (cm)")

graph.addModeled(0,h)

#TIME LOOP
for t in range(nsteps):
    modelTime = t * dt

    #Filling
    dh = Qin * dt / (np.pi * r **2)
    h = h + dh

    #Draining
    dVdt = -k * h 
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    # save height (h) calculated by the model
    #  only if the model time corresponds to one
    #  of the times when a measurement was taken
    if (modelTime in x_measured):
        print(modelTime, h)
        y_modeled.append(h)

    graph.addModeled(modelTime, h)
    #graph.wait(.1)


print('time:', x_measured)   
print('h_measured:', y_measured)
print("h_modeled:", y_modeled)

print(f'xavg measured =  {avg(x_measured)}')
print(f'yavg measured =  {avg(y_measured)}')

r = res(y_measured, y_modeled)
print(f'residual = {r}')

d = dsq(y_measured)
print(f'difference = {d}')

r2 = rSquared(y_measured, y_modeled)
print(f'r squared = {r2}')


#draw graph
graph.keepOpen()

