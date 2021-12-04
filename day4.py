import numpy as np
import pandas as pd

x = np.array([74,79,46,2,19,27,31,90,21,83,94,77,0,29,38,72,42,23,6,62,45,95,41,55,93,69,39,17,12,1,20,53,49,71,61,13,88,25,87,26,50,58,28,51,89,64,3,80,36,65,57,92,52,86,98,78,9,33,44,63,16,34,97,60,40,66,75,4,7,84,22,43,11,85,91,32,48,14,18,76,8,47,24,81,35,30,82,67,37,70,15,5,73,59,54,68,56,96,99,10])

boards = []
results = []
for i in range(100):
    board = np.loadtxt('day4.txt', skiprows=i*6, max_rows=5)
    boards.append(board)
    results.append(np.zeros_like(board))

np.where(boards[0]==3)
idx = np.where(boards[0]==92)
list(zip(idx[0], idx[1]))

for i in x:
    for b_i in range(100):
        idx = np.where(boards[b_i]==i)
        results[b_i][idx] = 1
        col_sum = np.sum(results[b_i], axis=0)
        row_sum = np.sum(results[b_i], axis=1)
        if np.any(col_sum==5) or np.any(row_sum==5):
            print("Which board won:", b_i)
            print("Winning number:", i)
            break
    if np.any(col_sum==5) or np.any(row_sum==5):
        break

np.where(x==i)
boards[85]
results[85]

winner = np.copy(boards[85])
np.where(np.sum(results[b_i], axis=1)==5)
#zeros out just the wining row
winner[np.where(np.sum(results[b_i], axis=1)==5)]=0

winner = np.copy(boards[85])
winner @ results[b_i]
np.multiply(winner, results[b_i])
np.logical_not(results[b_i])
#inverse then elementwise multiply
np.multiply(winner, np.logical_not(results[b_i]))

print(np.sum(np.multiply(winner, np.logical_not(results[b_i]))))
print(i)
print(np.sum(np.multiply(winner, np.logical_not(results[b_i]))) * i)

######Part 2
boards = []
results = []
results_win = list(np.zeros(100))
for i in range(100):
    board = np.loadtxt('day4.txt', skiprows=i*6, max_rows=5)
    boards.append(board)
    results.append(np.zeros_like(board))

for i in x:
    for b_i in range(100):
        idx = np.where(boards[b_i]==i)
        results[b_i][idx] = 1
        col_sum = np.sum(results[b_i], axis=0)
        row_sum = np.sum(results[b_i], axis=1)
        if np.any(col_sum==5) or np.any(row_sum==5):
            results_win[b_i] = 1
        if sum(results_win) == 100:
            print("Which board last:", b_i)
            print("Winning number:", i)
            break
    if sum(results_win) == 100:
        break
#winning number index
np.where(x==i)
print(np.sum(np.multiply(boards[b_i], np.logical_not(results[b_i]))))
print(i)
print(np.sum(np.multiply(boards[b_i], np.logical_not(results[b_i]))) * i)