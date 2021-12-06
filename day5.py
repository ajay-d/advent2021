import numpy as np
import pandas as pd

df = pd.read_csv('day5.txt', header=None, names=['x1', 'mid', 'y2'])
df[['y1', 'to', 'x2']] = df['mid'].str.split(' ', expand=True)
df = df[['x1', 'y1', 'x2', 'y2']]

df.max()
df.min()
df.shape
df[df['y1']==df['y2']]

df.dtypes
df.astype(np.float)
df = df.astype(np.int64)

df = df[(df['x1']==df['x2']) | (df['y1']==df['y2'])]
df.reset_index(inplace=True)
df.min()
df.max()

mat = np.zeros((1000, 1000))
mat[2, 1:4]
df.shape
for i in range(df.shape[0]):
    if df['x1'][i] == df['x2'][i]:
        row = df['x1'][i]
        y1 = min(df['y1'][i], df['y2'][i])
        y2 = max(df['y1'][i], df['y2'][i]) + 1
        mat[row, y1:y2] += 1
    if df['y1'][i] == df['y2'][i]:
        col = df['y1'][i]
        x1 = min(df['x1'][i], df['x2'][i])
        x2 = max(df['x1'][i], df['x2'][i]) + 1
        mat[x1:x2, col] += 1

points = np.where(mat > 1)
print(len(points[0]))

#####Part2
df = pd.read_csv('day5.txt', header=None, names=['x1', 'mid', 'y2'])
df[['y1', 'to', 'x2']] = df['mid'].str.split(' ', expand=True)
df = df[['x1', 'y1', 'x2', 'y2']]
df = df.astype(np.int64)

mat = np.zeros((1000, 1000))
for i in range(df.shape[0]):
    print(i)
    if df['x1'][i] == df['x2'][i]:
        row = df['x1'][i]
        y1 = min(df['y1'][i], df['y2'][i])
        y2 = max(df['y1'][i], df['y2'][i]) + 1
        mat[row, y1:y2] += 1
    elif df['y1'][i] == df['y2'][i]:
        col = df['y1'][i]
        x1 = min(df['x1'][i], df['x2'][i])
        x2 = max(df['x1'][i], df['x2'][i]) + 1
        mat[x1:x2, col] += 1
    else:
        x_min = min(df['x1'][i], df['x2'][i])
        x_max = max(df['x1'][i], df['x2'][i])
        y_min = min(df['y1'][i], df['y2'][i])
        y_max = max(df['y1'][i], df['y2'][i])
        x1, x2 = df['x1'][i], df['x2'][i]
        y1, y2 = df['y1'][i], df['y2'][i]
        for j in range(y_max-y_min+1):
            if (x1 < x2) & (y1 < y2):
                mat[x1+j, y1+j] += 1
            if (x1 < x2) & (y1 > y2):
                mat[x1+j, y1-j] += 1
            if (x1 > x2) & (y1 < y2):
                mat[x1-j, y1+j] += 1
            if (x1 > x2) & (y1 > y2):
                mat[x2+j, y2+j] += 1
np.sum(mat)
points = np.where(mat > 1)
print(len(points[0]))

for j in range(20-10+1):
    print(10+j)
