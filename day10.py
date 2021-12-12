import numpy as np
import pandas as pd

x = np.loadtxt('day10.txt', dtype=(np.dtype(str)))
x.size
max(x[0])

l = lambda t: len(t)
vfunc = np.vectorize(l)
larr = vfunc(x)
len(larr)

left = ["[", "<", "(", "{"]
right = ["]", ">", ")", "}"]

corrupt=[]
for i in range(x.size):
    row = x[i]
    left_row = []
    for chr in row:
        if chr in left:
            left_row.append(chr)
        elif chr in right:
            idx = right.index(chr)
            if left_row[len(left_row)-1] == left[idx]:
                discard = left_row.pop()
            else:
                corrupt.append(i)
                break
    else:
        print(row)
        print(i, "incomplete")

for i in corrupt:
    print(x[i])

incomplete = set(range(x.size)).difference(corrupt)
pts = dict.fromkeys(right)
for k,v in pts.items():
    pts[k] = 0

for i in corrupt:
    row = x[i]
    left_row = []
    for chr in row:
        if chr in left:
            left_row.append(chr)
        else:
            idx = right.index(chr)
            if left_row[len(left_row)-1] == left[idx]:
                discard = left_row.pop()
            else:
                pts[chr] += 1
                break
pts[')'] * 3
pts[']'] * 57
pts['}'] * 1197
pts['>'] * 25137

pts[')'] * 3 + pts[']'] * 57 + pts['}'] * 1197 + pts['>'] * 25137

#####Part 2
m = []
for i in incomplete:
    row = x[i]
    left_row = []
    for chr in row:
        if chr in left:
            left_row.append(chr)
        else:
            idx = right.index(chr)
            if left_row[len(left_row)-1] == left[idx]:
                discard = left_row.pop()
    m.append(left_row)

complete = []
for i in range(len(m)):
    row = m[i]
    row.reverse()
    complete_row = []
    for chr in row:
        idx = left.index(chr)
        complete_row.append(right[idx])
    complete.append(complete_row)

score = []
pts = dict.fromkeys(right)
pts[")"], pts["]"], pts["}"], pts[">"] = 1,2,3,4

for i in range(len(complete)):
    cur_score = 0
    for chr in complete[i]:
        cur_score = cur_score * 5 + pts[chr]
    score.append(cur_score)

print(score)
score.sort()
score[22]