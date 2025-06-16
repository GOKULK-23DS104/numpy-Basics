import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
combined = np.concatenate((arr1, arr2), axis=0)
print("Row-wise append:\n", combined)

arr = np.array([1, 2, 3])
arr_float = np.array([4.0, 5.0])
combined = np.append(arr, arr_float)
print("Appended float array:\n", combined)
