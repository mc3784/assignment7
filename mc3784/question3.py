import numpy as np
randMatrix = np.random.rand(10,3)
print "#3 question"
print "1-D array containing 10 values, each value is the number closest to 0.5 from the corresponding row of the original array"
mask=np.argsort(abs(randMatrix-0.5))==0
print randMatrix[mask]
