import numpy as np
print "#2 question"
a = np.arange(25).reshape(5,5)
b = np.array([1., 5, 10, 15, 20])
c = a/b.reshape(5,1)
print c


