import numpy as np
import time
from ezGraph import *
from rStats import *


#Parameters
dt = 1
nsteps = 1320

h = 0
l = 25
w = 50 
Qin = 13.5      
k = 13.5    

#Experimental Data
x_measured = [97, 188, 278, 383, 467, 560, 659]
y_measured = [1,2,3,4,5,6,7]
y_modeled = []


#Graph
graph = ezGraphMM(xmax = 100,
    ymin=0, ymax=100,
    x_measured = x_measured,
    y_measured = y_measured,
    xLabel="Time (s)",
    yLabel="Height (cm)")

graph.addModeled(0,h)
filling = True
#TIME LOOP
for t in range(nsteps):
    modelTime = t * dt

    #Filling
    if filling:
        dh = Qin * dt / (w * l)
        h = h + dh
    #Draining
    else: 
        dh = Qin * dt / (w * l)
        h = h - dh
 

    if h > 5:
        filling = False
    if h < 4:
        filling = True
    

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

# r = res(y_measured, y_modeled)
# print(f'residual = {r}')

d = dsq(y_measured)
print(f'difference = {d}')

# r2 = rSquared(y_measured, y_modeled)
# print(f'r squared = {r2}')


#draw graph
graph.keepOpen()

