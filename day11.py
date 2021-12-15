import numpy as np
import pandas as pd

x = np.loadtxt('day11.txt', dtype=(np.dtype(str)))

def find_neighbors(pt):
    i,j = pt
    n = []
    if i==0 and j==0:
        n.append((i+1,j))
        n.append((i,j+1))
        n.append((i+1,j+1))
        return n
    elif i==0 and j==9:
        n.append((i+1,j))
        n.append((i,j-1))
        n.append((i+1,j-1))
        return n
    elif i==9 and j==0:
        n.append((i-1,j))
        n.append((i,j+1))
        n.append((i-1,j+1))
        return n
    elif i==9 and j==9:
        n.append((i-1,j))
        n.append((i,j-1))
        n.append((i-1,j-1))
        return n
    elif i==0:
        n.append((i+1,j))
        n.append((i+1,j-1))
        n.append((i+1,j+1))
        n.append((i,j-1))
        n.append((i,j+1))
        return n
    elif i==9:
        n.append((i-1,j))
        n.append((i-1,j-1))
        n.append((i-1,j+1))
        n.append((i,j-1))
        n.append((i,j+1))
        return n
    elif j==0:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j+1))
        n.append((i-1,j+1))
        n.append((i+1,j+1))
        return n
    elif j==9:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j-1))
        n.append((i-1,j-1))
        n.append((i+1,j-1))
        return n
    else:
        n.append((i+1,j))
        n.append((i-1,j))
        n.append((i,j+1))
        n.append((i,j-1))

        n.append((i+1,j+1))
        n.append((i+1,j-1))
        n.append((i-1,j+1))
        n.append((i-1,j-1))

        return n

m = np.empty((10,10), dtype=np.int64)
for i in range(10):
    for j in range(10):
        m[i,j] = np.int64(x[i][j])

test=[]
for i in range(10):
    for j in range(10):
        test.append(len(find_neighbors((i,j))))
np.unique(test, return_counts=True)

len(m[np.where(m==9)])
i,j = zip(np.where(m==9))

for i,j in zip(*np.where(m==9)):
    print(i,j)

m[7,3]
len(find_neighbors((7,3)))
find_neighbors((7,2))
find_neighbors((7,4))

m = np.empty((10,10), dtype=np.int64)
for i in range(10):
    for j in range(10):
        m[i,j] = np.int64(x[i][j])
flash = 0
for step in range(100):
    m += 1
    print("STEP: ", step)
    increase_array = []
    already_flashed = []
    for i,j in zip(*np.where(m==10)):
        n = find_neighbors((i,j))
        for pt in n:
            increase_array.append(pt)
            if pt == (7,3):
                print("Here")
        m[i,j] = 0
        flash += 1
        already_flashed.append((i,j))
        #increase_array = list(set(increase_array).difference(set(already_flashed)))
    for pt in increase_array:
        if pt in already_flashed:
            idx = increase_array.index(pt)
            increase_array.pop(idx)
    while len(increase_array) > 0:
        cur_pt = increase_array.pop()
        #print(cur_pt)
        #print(m)
        if m[cur_pt] < 10 and m[cur_pt] > 0:
            m[cur_pt] += 1
        if m[cur_pt] > 9:
            n = find_neighbors(cur_pt)
            m[cur_pt] = 0
            flash += 1
            already_flashed.append(cur_pt)
            for pt in n:
                increase_array.append(pt)
            for pt in increase_array:
                if pt in already_flashed:
                    idx = increase_array.index(pt)
                    increase_array.pop(idx)

####Part 2
m = np.empty((10,10), dtype=np.int64)
for i in range(10):
    for j in range(10):
        m[i,j] = np.int64(x[i][j])
flash = 0
for step in range(300):
    m += 1
    print("STEP: ", step)
    increase_array = []
    already_flashed = []
    for i,j in zip(*np.where(m==10)):
        n = find_neighbors((i,j))
        for pt in n:
            increase_array.append(pt)
        m[i,j] = 0
        flash += 1
        already_flashed.append((i,j))
        #increase_array = list(set(increase_array).difference(set(already_flashed)))
    for pt in increase_array:
        if pt in already_flashed:
            idx = increase_array.index(pt)
            discard = increase_array.pop(idx)
    while len(increase_array) > 0:
        cur_pt = increase_array.pop()
        if m[cur_pt] < 10 and m[cur_pt] > 0:
            m[cur_pt] += 1
        if m[cur_pt] > 9:
            n = find_neighbors(cur_pt)
            m[cur_pt] = 0
            flash += 1
            already_flashed.append(cur_pt)
            print(len(already_flashed))
            for pt in n:
                increase_array.append(pt)
            for pt in increase_array:
                if pt in already_flashed:
                    idx = increase_array.index(pt)
                    discard = increase_array.pop(idx)