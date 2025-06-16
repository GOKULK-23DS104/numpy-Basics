import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

print("Max element:", arr.max())
print("Row-wise max:", arr.max(axis=1))
print("Column-wise min:", arr.min(axis=0))
print("Sum of all elements:", arr.sum())
print("Cumulative sum along rows:\n", arr.cumsum(axis=1))
