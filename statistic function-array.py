import numpy as np
arr = np.array(([23, 36, 33], [23, 21, 45], [4, 22, 78]))

# 1. Mean: Average of all elements
print(f"1. Mean: {np.mean(arr)}")

# 2. Median: Middle value in the sorted array
print(f"2. Median: {np.median(arr)}")

# 3. Standard Deviation: Measure of data spread from mean
print(f"3. Standard Deviation: {np.std(arr)}")

# 4. Percentile: Value below which a given percentage of observations fall
print(f"4. Percentile (0th): {np.percentile(arr, 0)}")  # Minimum value

# 5. Variance: Average of the squared deviations from mean
print(f"5. Variance: {np.var(arr)}")

# 6. Minimum: Smallest value in the array
print(f"6. Minimum: {np.min(arr)}")

# 7. Maximum: Largest value in the array
print(f"7. Maximum: {np.max(arr)}")

# 8. Sum: Total of all array elements
print(f"8. Sum: {np.sum(arr)}")

# 9. Product: Multiplication of all array elements
print(f"9. Product: {np.prod(arr)}")

# 10. Cumulative Sum: Running total of the elements
print(f"10. Cumulative sum: {np.cumsum(arr)}")

# 11. Cumulative Product: Running product of the elements
print(f"11. Cumulative product: {np.cumprod(arr)}")

# 12. Difference: First-order differences between consecutive elements in row-wise manner
print(f"12. Difference: {np.diff(arr)}")

# 13. Ediff1d: Flattened 1D difference of adjacent elements
print(f"13. Ediff1d: {np.ediff1d(arr)}")

# 14. In1d: Checks which elements are in the second list (element-wise)
print(f"14. In1d: {np.isin(arr, [23, 21])}")

# 15. Partition: Rearranges elements so the kth element is in its sorted position
print(f"15. Partition: {np.partition(arr, 2)}")

# 16. Argpartition: Indices that would partition the array
print(f"16. Argpartition: {np.argpartition(arr, 2)}")

# 17. Sort: Returns a sorted copy of array (row-wise for 2D)
print(f"17. Sort: {np.sort(arr)}")

# 18. Argsort: Returns indices that would sort the array
print(f"18. Argsort: {np.argsort(arr)}")

# 19. Searchsorted: Finds indices where elements should be inserted to maintain order
# For 2D array, this may raise an error; needs 1D input ideally
print(f"19. Searchsorted (on flattened): {np.searchsorted(arr.flatten(), 23)}")

# 20. Repeat: Repeats each element specified number of times
print(f"20. Repeat: {np.repeat(arr, 2)}")

# 21. Tile: Repeats the entire array specified number of times
print(f"21. Tile: {np.tile(arr, 2)}")

# 22. Clip: Limits the values in an array (min=20, max=30)
print(f"22. Clip: {np.clip(arr, 20, 30)}")
