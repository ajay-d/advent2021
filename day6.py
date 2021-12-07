import numpy as np
import pandas as pd

x = np.array([4,1,1,4,1,2,1,4,1,3,4,4,1,5,5,1,3,1,1,1,4,4,3,1,5,3,1,2,5,1,1,5,1,1,4,1,1,1,1,2,1,5,3,4,4,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,4,1,2,3,5,1,2,2,4,1,4,4,4,1,2,5,1,2,1,1,1,1,1,1,4,1,1,4,3,4,2,1,3,1,1,1,3,5,5,4,3,4,1,5,1,1,1,2,2,1,3,1,2,4,1,1,3,3,1,3,3,1,1,3,1,5,1,1,3,1,1,1,5,4,1,1,1,1,4,1,1,3,5,4,3,1,1,5,4,1,1,2,5,4,2,1,4,1,1,1,1,3,1,1,1,1,4,1,1,1,1,2,4,1,1,1,1,3,1,1,5,1,1,1,1,1,1,4,2,1,3,1,1,1,2,4,2,3,1,4,1,2,1,4,2,1,4,4,1,5,1,1,4,4,1,2,2,1,1,1,1,1,1,1,1,1,1,1,4,5,4,1,3,1,3,1,1,1,5,3,5,5,2,2,1,4,1,4,2,1,4,1,2,1,1,2,1,1,5,4,2,1,1,1,2,4,1,1,1,1,2,1,1,5,1,1,2,2,5,1,1,1,1,1,2,4,2,3,1,2,1,5,4,5,1,4])
x = np.array([3,4,3,1,2])
np.unique(x, return_counts=True)
np.shape(np.unique(x, return_counts=True))

for i in range(80):
    toadd = len(np.where(x == 0)[0])
    idx_day = np.where(x >= 1)
    idx_zero = np.where(x == 0)
    x[idx_day] = x[idx_day]-1
    x[idx_zero] = 6
    x = np.append(x, np.zeros(toadd) + 8)
    print(len(x))

####Part 2
#x = np.array([3,4,3,1,2])
col1 = np.arange(9, dtype=np.int64).reshape((9,1))
col2 = np.zeros((9,1), dtype=np.int64)
df = pd.DataFrame(np.concatenate((col1, col2), axis=1), columns = ['age','count'])

#fill up initial values
for i in range(len(np.unique(x, return_counts=True)[0])):
    df.loc[df['age']== i+1, 'count'] = np.unique(x, return_counts=True)[1][i]

for i in range(256):
    toadd = df.loc[df['age'] == 0, 'count'].astype(np.int64).to_numpy()
    arr = df.loc[df['age'] > 0, 'count'].to_numpy()
    #arr = np.where(arr < 0, 0, arr) #0 through 7
    arr = np.append(arr, toadd)
    df['count'] = arr
    df.loc[df['age'] == 6, 'count'] = df.loc[df['age'] == 6, 'count'] + toadd

np.sum(df['count'])