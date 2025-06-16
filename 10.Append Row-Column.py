import numpy as np

arr = np.arange(1, 13).reshape(2, 6)
col = np.arange(5, 11).reshape(1, 6)
arr_col = np.append(arr, col, axis=0)

row = np.array([1, 2]).reshape(2, 1)
arr_row = np.append(arr, row, axis=1)

print("Column-wise append:\n", arr_col)
print("Row-wise append:\n", arr_row)
