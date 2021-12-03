import numpy as np
import pandas as pd
x = np.loadtxt('day2.txt', usecols=(0, 1), dtype=(np.dtype(str), np.dtype(float)))

np.dtype(float)
np.dtype(str)

df = pd.read_csv('day2.txt', sep=' ', header=None, names=['dir', 'len'])
arr = np.array(df)
df.dir.unique()

f = df[df['dir'] == 'forward']
np.sum(f.len)

d = df[df['dir'] == 'down']
np.sum(d.len)
u = df[df['dir'] == 'up']
np.sum(-u.len)

depth = np.sum(d.len) + np.sum(-u.len)
depth * np.sum(f.len)

####
aim = 0
depth = 0
horizon = 0
for i in range(df.shape[0]):
    if(df.dir[i] == 'down'):
        aim = aim + df.len[i]
    if(df.dir[i] == 'up'):
        aim = aim - df.len[i]
    if(df.dir[i] == 'forward'):
        horizon = horizon + df.len[i]
        depth = depth + aim * df.len[i]
print(aim, depth, horizon)
print(horizon * depth)