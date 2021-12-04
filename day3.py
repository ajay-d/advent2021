import numpy as np
from numpy.core.fromnumeric import compress
import pandas as pd

x = np.loadtxt('day3.txt', dtype=(np.dtype(str)))
np.size(x) 
len(x[0])

b1 = []
for i in range(np.size(x)):
    b1.append(x[i][0])
np.array(b1).astype(int).sum()

bits = np.zeros(12)

for j in range(len(x[0])):
    arr = []
    for i in range(np.size(x)):
        arr.append(x[i][j])
    print(np.array(arr).astype(int).sum())
    bits[j] = np.array(arr).astype(int).sum()

[1 if i > 500 else 0 for i in bits ]
g = [1 if i > 500 else 0 for i in bits ]
e = np.logical_not(g).astype(int)

gamma = ''
for i in g:
    gamma += str(i)
epsilon = ''
for i in e:
    epsilon += str(i)

int(gamma, base=2)
int(epsilon, base=2)
print(int(gamma, base=2) * int(epsilon, base=2))

#####
