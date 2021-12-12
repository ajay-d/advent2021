import numpy as np
import pandas as pd

x = np.loadtxt('day9.txt', dtype=(np.dtype(str)))
x.size
len(x[0])

v = x.size
h = len(x[0])

m = np.empty((v,h), dtype=np.int64)
for i in range(v):
    for j in range(h):
        m[i,j] = np.int64(x[i][j])

m.shape

arr = []
for i in range(v):
    for j in range(h):
        cur = m[i, j]
        if i==0 and j==0:
            if cur < min(m[i+1, j], m[i, j+1]):
                arr.append(cur)
        elif i==0 and j==99:
            if cur < min(m[i+1, j], m[i, j-1]):
                arr.append(cur)
        elif i==99 and j==0:
            if cur < min(m[i-1, j], m[i, j+1]):
                arr.append(cur)
        elif i==99 and j==99:
            if cur < min(m[i-1, j], m[i, j-1]):
                arr.append(cur)
        elif i==0:
            if cur < min(m[i+1, j], m[i, j-1], m[i, j+1]):
                arr.append(cur)
        elif i==99:
            if cur < min(m[i-1, j], m[i, j-1], m[i, j+1]):
                arr.append(cur)
        elif j==0:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j+1]):
                arr.append(cur)
        elif j==99:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j-1]):
                arr.append(cur)
        else:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j-1], m[i, j+1]):
                arr.append(cur)
sum(arr)
len(arr)
sum(arr) + len(arr)

####Part two
#collect all the low points, and start from there
arr = []
for i in range(v):
    for j in range(h):
        cur = m[i, j]
        if i==0 and j==0:
            if cur < min(m[i+1, j], m[i, j+1]):
                arr.append((i,j))
        elif i==0 and j==99:
            if cur < min(m[i+1, j], m[i, j-1]):
                arr.append((i,j))
        elif i==99 and j==0:
            if cur < min(m[i-1, j], m[i, j+1]):
                arr.append((i,j))
        elif i==99 and j==99:
            if cur < min(m[i-1, j], m[i, j-1]):
                arr.append((i,j))
        elif i==0:
            if cur < min(m[i+1, j], m[i, j-1], m[i, j+1]):
                arr.append((i,j))
        elif i==99:
            if cur < min(m[i-1, j], m[i, j-1], m[i, j+1]):
                arr.append((i,j))
        elif j==0:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j+1]):
                arr.append((i,j))
        elif j==99:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j-1]):
                arr.append((i,j))
        else:
            if cur < min(m[i+1, j], m[i-1, j], m[i, j-1], m[i, j+1]):
                arr.append((i,j))
len(arr)

#For each min, collect all non-9 adjacent points
arr = arr[100:105]
for pt in arr:
    print(pt)

#function to find all of a points neighbors
def find_neighbors(pt):
    i,j = pt
    n = []
    if i==0 and j==0:
        n.append((i+1,j))
        n.append((i,j+1))
        return n
    elif i==0 and j==99:
        n.append((i+1,j))
        n.append((i,j-1))
        return n
    elif i==99 and j==0:
        n.append((i-1,j))
        n.append((i,j+1))
        return n
    elif i==99 and j==99:
        n.append((i-1,j))
        n.append((i,j-1))
        return n
    elif i==0:
        n.append((i+1,j))
        n.append((i,j-1))
        n.append((i,j+1))
        return n
    elif i==99:
        n.append((i-1,j))
        n.append((i,j-1))
        n.append((i,j+1))
        return n
    elif j==0:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j+1))
        return n
    elif j==99:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j-1))
        return n
    else:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j+1))
        n.append((i,j-1))
        return n

find_neighbors(arr[0])

for pt in arr:
    print(pt)
    n = find_neighbors(pt)
    i = 0
    while len(n) > 1:
        cur = n[i]
        if m[cur] < 9 and 