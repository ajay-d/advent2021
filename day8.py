from os import curdir
from typing_extensions import _AnnotatedAlias
import numpy as np
import pandas as pd

x = pd.read_csv('day8.txt', sep=' ', header=None)
#x = pd.read_csv('day8-small.txt', sep=' ', header=None)

arr = x.iloc[:, 11:15].to_numpy()
arr.shape

l = lambda t: len(t)
vfunc = np.vectorize(l)
larr = vfunc(arr)
vfunc = np.vectorize(len)
larr = vfunc(arr)

#1, 4, 7, 8
small = lambda x: 1 if x in [2,4,3,7] else 0
vfunc = np.vectorize(small)
smallarr = vfunc(larr)
np.sum(smallarr)

####Part 2
arr = x.iloc[:, 0:10].to_numpy()
arr.shape
vfunc = np.vectorize(len)
larr = vfunc(arr)
larr.min(axis=1)
larr.max(axis=1)

arr_out = x.iloc[:, 11:15].to_numpy()
answer_arr = []
#define digits in numbered segments.
d = {'123567' : '0', '36' : '1', '13457' : '2', '13467' : '3', '2346' : '4',
     '12467' : '5', '124567' : '6', '136' : '7', '1234567' : '8', '123467' : '9'}

for row in range(arr.shape[0]):
    cur_row = arr[row]
    cur_out = arr_out[row]
    #cur_row = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    vfunc = np.vectorize(len)
    lengths = vfunc(cur_row)
    x_1 = np.array(cur_row)[np.where(lengths == 2)]
    x_4 = np.array(cur_row)[np.where(lengths == 4)]
    x_7 = np.array(cur_row)[np.where(lengths == 3)]
    x_8 = np.array(cur_row)[np.where(lengths == 7)]

    #dict to store letter to bit mapping
    d_curr = {}

    #set(x_7[0])
    #set(x_1[0])
    let_cur = set(x_7[0]).difference(set(x_1[0]))
    #top
    d_curr[let_cur.pop()] = 1

    #2,3,5
    x_235 = np.array(cur_row)[np.where(lengths == 5)]
    #0,6,9
    x_069 = np.array(cur_row)[np.where(lengths == 6)]

    #the third one is bottom left - 5
    if len(set(x_235[0]).difference(set(x_4[0]))) == 3:
        s3 = set(x_235[0]).difference(set(x_4[0]))
    if len(set(x_235[1]).difference(set(x_4[0]))) == 3:
        s3 = set(x_235[1]).difference(set(x_4[0]))
    if len(set(x_235[2]).difference(set(x_4[0]))) == 3:
        s3 = set(x_235[2]).difference(set(x_4[0]))

    if len(set(x_235[0]).difference(set(x_4[0]))) == 2:
        s2 = set(x_235[0]).difference(set(x_4[0]))
    if len(set(x_235[1]).difference(set(x_4[0]))) == 2:
        s2 = set(x_235[1]).difference(set(x_4[0]))
    if len(set(x_235[2]).difference(set(x_4[0]))) == 2:
        s2 = set(x_235[2]).difference(set(x_4[0]))
    #the third one is bottom left - 5
    let_cur = s3.difference(s2)
    d_curr[let_cur.pop()] = 5
    #bottom
    let_cur = s2.difference(x_7[0])
    d_curr[let_cur.pop()] = 7

    #if intersect is 3, the digit is 3
    if len(set(x_235[0]).intersection(set(x_7[0]))) == 3:
        n3 = set(x_235[0]).difference(set(x_7[0]))
    if len(set(x_235[1]).intersection(set(x_7[0]))) == 3:
        n3 = set(x_235[1]).difference(set(x_7[0]))
    if len(set(x_235[2]).intersection(set(x_7[0]))) == 3:
        n3 = set(x_235[2]).difference(set(x_7[0]))

    for k,v in d_curr.items():
        if v == 7:
            bottom = k
    middle = n3.difference(bottom)
    d_curr[middle.pop()] = 4
    for k,v in d_curr.items():
        if v == 4:
            middle = k
        if v == 5:
            bottom_left = k
    #the digit 0
    if len(set(x_069[0]).intersection(middle)) == 0:
        zero = x_069[0]
        diff1 = set(x_069[0]).difference(set(x_7[0]))
        diff1 = diff1.difference(bottom)
        top_left = diff1.difference(bottom_left)
    if len(set(x_069[1]).intersection(middle)) == 0:
        zero = x_069[1]
        diff1 = set(x_069[1]).difference(set(x_7[0]))
        diff1 = diff1.difference(bottom)
        top_left = diff1.difference(bottom_left)
    if len(set(x_069[2]).intersection(middle)) == 0:
        zero = x_069[2]
        diff1 = set(x_069[2]).difference(set(x_7[0]))
        diff1 = diff1.difference(bottom)
        top_left = diff1.difference(bottom_left)
    d_curr[top_left.pop()] = 2
    #sorted(d_curr.items())
    #sorted(d_curr.values())

    x_69 = x_069[np.where(x_069 != zero)]

    #int = 1 is number 6, other is 9
    if len(set(x_69[0]).intersection(set(x_1[0]))) == 1:
        bottom_right = set(x_69[0]).intersection(set(x_1[0]))
        top_right = set(x_1[0]).difference(bottom_right)
    if len(set(x_69[1]).intersection(set(x_1[0]))) == 1:
        bottom_right = set(x_69[1]).intersection(set(x_1[0]))
        top_right = set(x_1[0]).difference(bottom_right)
    d_curr[top_right.pop()] = 3
    d_curr[bottom_right.pop()] = 6

    x=''
    y=''
    for k,v in d_curr.items():
        x += k
        y += str(v)

    ans = ""
    for j in range(len(cur_out)):
        mytable = cur_out[j].maketrans(x, y)
        t = cur_out[j].translate(mytable)
        t_sort = "".join(sorted(t))
        ans += d[t_sort]
    print(ans)
    answer_arr.append(int(ans))

sum(answer_arr)