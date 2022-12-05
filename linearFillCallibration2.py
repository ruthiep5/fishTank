import numpy as np
import time
from ezGraph import *
from rStats import *

length = 50
depth = 28
width = 25

v = (length*width)*depth

dt = 1
nsteps = 20

x_measured = [1,2,3,4,5,6,7]
y_measured = [97.14, 187.82, 278, 382.88, 466.56, 560.2, 659.41]
y_modeled = []


graph = ezGraphMM(xmax = 100,
    ymin=0, ymax=100,
    x_measured = x_measured,
    y_measured = y_measured,
    xLabel="Time (s)",
    yLabel="Height (cm)")
graph.addModeled(0,h)