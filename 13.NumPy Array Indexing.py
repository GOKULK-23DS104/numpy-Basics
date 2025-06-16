import numpy as np

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing: First 2 rows and alternate columns
temp = arr[:2, ::2]
print("First 2 rows, alternate columns:\n", temp)

# Integer indexing: Specific elements at given indices
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0,3), (1,2), (2,1), (3,0):\n", temp)

# Boolean indexing: Elements > 0
cond = arr > 0
temp = arr[cond]
print("\nElements greater than 0:\n", temp)
