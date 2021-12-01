import requests 
response = requests.get('https://adventofcode.com/2021/day/1/input') 
print(response.text) 

import numpy as np
x = np.loadtxt('day1.txt', usecols=0)
np.size(x)

[x for x in range(100) if x % 2 == 0]
[n * n for n in range(100)]

ind = np.array(range(np.size(x)-1)) + 1 

ind_gt = [x[i] for i in ind if x[i] > x[i-1]]
np.size(ind_gt)

#part 2
ind = np.array(range(np.size(x)-2))
trips = [np.sum(x[i:(i+3)]) for i in ind]
np.size(trips)

ind = np.array(range(np.size(trips)-1)) + 1 
ind_gt = [trips[i] for i in ind if trips[i] > trips[i-1]]
np.size(ind_gt)
