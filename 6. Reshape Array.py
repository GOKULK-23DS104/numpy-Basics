import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print("Original array:\n", arr)
print("Reshaped array:\n", newarr)
