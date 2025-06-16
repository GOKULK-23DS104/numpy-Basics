# 1. Reshape - Changes the shape of the array to (2 rows, 3 columns)
import numpy as np
print("\n1. Reshape:")
arr = np.array([31, 44, 55, 16, 4, 23])
sArray = arr.reshape(2, 3)
print(sArray)

# 2. Transpose - Swaps rows with columns
print("\n2. Transpose:")
arr = np.array([[31, 44, 55], [16, 4, 23]])
tArray = arr.transpose()
print(tArray)

# 3. Flatten - Converts 2D array into 1D array
print("\n3. Flatten:")
arr = np.array([[31, 44, 55], [16, 4, 23]])
fArray = arr.flatten()
print(fArray)

# 4. Sort - Sorts the array in ascending order
print("\n4. Sort:")
arr = np.array([31, 44, 55, 16, 4, 23])
SortArray = np.sort(arr)
print(SortArray)

# 5. argsort - Returns the indices that would sort the array
print("\n5. argsort:")
arr = np.array([31, 44, 55, 16, 4, 23])
argsortArray = np.argsort(arr)
print(argsortArray)

# 6. join (concatenate) - Joins two arrays into one
print("\n6. join:")
arr1 = np.array([31, 44, 55])
arr2 = np.array([4, 2, 6, 9])
joinArray = np.concatenate((arr1, arr2))
print(joinArray)

# 7. repeat - Repeats each element specified number of times
print("\n7. repeat:")
arr = np.array([31, 44, 55])
repeatArray = np.repeat(arr, 2)
print(repeatArray)

# 8. tile - Repeats the whole array specified number of times
print("\n8. tile:")
arr = np.array([31, 44, 55])
tileArray = np.tile(arr, 2)
print(tileArray)

# 9. clip - Limits values to a specified range [10, 20]
print("\n9. clip:")
arr = np.array([31, 44, 55, 16, 4, 23])
clipArray = np.clip(arr, 10, 20)
print(clipArray)

# 10. where - Replaces values > 20 with 20, otherwise keeps original
print("\n10. where:")
arr = np.array([31, 44, 55, 16, 4, 23])
whereArray = np.where(arr > 20, 20, arr)
print(whereArray)

# 11. searchsorted - Returns index where 20 should be inserted to maintain order
print("\n11. searchsorted:")
arr = np.array([31, 44, 55, 16, 4, 23])
searchsortedArray = np.searchsorted(arr, 20)
print(searchsortedArray)

# 12. unique - Removes duplicate elements and returns sorted unique values
print("\n12. unique:")
arr = np.array([31, 44, 55, 16, 4, 23, 31, 44, 55])
uniqueArray = np.unique(arr)
print(uniqueArray)

# 13. split - Splits array into 2 equal parts
print("\n13. split:")
arr = np.array([31, 44, 55, 16, 4, 23])
splitArray = np.split(arr, 2)
print(splitArray)

# 14. isin - Checks which elements of arr are in the list [31, 44]
print("\n14. isin:")
arr = np.array([31, 44, 55, 16, 4, 23])
isinArray = np.isin(arr, [31, 44])
print(isinArray)

# 15. partition - Rearranges elements so that the 3rd smallest element is in its sorted position
print("\n15. partition:")
arr = np.array([31, 44, 55, 16, 4, 23])
partitionArray = np.partition(arr, 3)
print(partitionArray)

# 16. argpartition - Returns indices that would partition the array around the 3rd smallest element
print("\n16. argpartition:")
arr = np.array([31, 44, 55, 16, 4, 23])
argpartitionArray = np.argpartition(arr, 3)
print(argpartitionArray)

# 17. argsort - Repeats argsort (already explained above)
print("\n17. argsort:")
arr = np.array([31, 44, 55, 16, 4, 23])
argsortArray = np.argsort(arr)
print(argsortArray)

# 18. cumsum - Cumulative sum of elements
print("\n18. cumsum:")
arr = np.array([31, 44, 55, 16, 4, 23])
cumsumArray = np.cumsum(arr)
print(cumsumArray)

# 19. cumprod - Cumulative product of elements
print("\n19. cumprod:")
arr = np.array([31, 44, 55, 16, 4, 23])
cumprodArray = np.cumprod(arr)
print(cumprodArray)

# 20. diff - Difference between consecutive elements
print("\n20. diff:")
arr = np.array([31, 44, 55, 16, 4, 23])
diffArray = np.diff(arr)
print(diffArray)

# 21. ediff1d - Efficient version of diff for 1D arrays
print("\n21. ediff1d:")
arr = np.array([31, 44, 55, 16, 4, 23])
ediff1dArray = np.ediff1d(arr)
print(ediff1dArray)
