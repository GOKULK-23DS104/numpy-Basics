import numpy as np

arr = np.arange(25).reshape(5, 5)
print("Original shape:", arr.shape)

arr_5D = arr[np.newaxis, ..., np.newaxis, np.newaxis]
print("New shape (using newaxis):", arr_5D.shape)

x = np.zeros((3, 4))
y = np.expand_dims(x, axis=1)
print("Shape using expand_dims:", y.shape)

arr = np.arange(25).reshape(5, 5)
arr_5D = np.expand_dims(arr, axis=(0, 3, -1))
print("Shape using expand_dims with multiple axes:", arr_5D.shape)
