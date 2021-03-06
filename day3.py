import numpy as np
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

#start with 1 and most common bits
arr = x
bit = 0
idx = np.arange(1000)
#while bit < 5:
while len(arr) > 1:
    idx_0 = []
    idx_1 = []
    for i in range(len(arr)):
        if arr[i][bit] == '0':
            idx_0.append(i)
        else:
            idx_1.append(i)
    if len(idx_0) > len(idx_1):
        idx = idx_0
    elif len(idx_0) < len(idx_1):
        idx = idx_1
    else:
        idx = idx_1
    print(len(idx))
    arr = arr[idx]
    bit += 1

o2 = int(arr[0], base=2)

arr = x
bit = 0
idx = np.arange(1000)
#while bit < 5:
while len(arr) > 1:
    idx_0 = []
    idx_1 = []
    for i in range(len(arr)):
        if arr[i][bit] == '0':
            idx_0.append(i)
        else:
            idx_1.append(i)
    if len(idx_0) > len(idx_1):
        idx = idx_1
    elif len(idx_0) < len(idx_1):
        idx = idx_0
    else:
        idx = idx_0
    print(len(idx))
    arr = arr[idx]
    bit += 1

co2 = int(arr[0], base=2)

print(o2 * co2)