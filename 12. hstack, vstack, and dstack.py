import numpy as np

in_arr1 = np.array([1, 2, 3])
in_arr2 = np.array([4, 5, 6])

out_arr1 = np.hstack((in_arr1, in_arr2))
out_arr2 = np.vstack((in_arr1, in_arr2))
out_arr3 = np.dstack((in_arr1, in_arr2))

print("Horizontally stacked:\n", out_arr1)
print("Vertically stacked:\n", out_arr2)
print("Depth-wise stacked:\n", out_arr3)
