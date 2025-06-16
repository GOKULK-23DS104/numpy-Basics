# Arithmetic functions - One Dimensional Array
import numpy as np
arr1 = np.array([12, 22, 34])
arr2 = np.array([10, 20, 30])

print(f"1. Addition: {np.add(arr1, arr2)}")              # Element-wise addition
print(f"2. Subtraction: {np.subtract(arr1, arr2)}")      # Element-wise subtraction
print(f"3. Multiplication: {np.multiply(arr1, arr2)}")   # Element-wise multiplication
print(f"4. Division: {np.divide(arr1, arr2)}")           # Element-wise division
print(f"5. Modulus: {np.mod(arr1, arr2)}")               # Remainder of division (arr1 % arr2)
print(f"6. Reciprocal: {np.reciprocal(arr1)}")           # 1 / arr1 (only for non-zero elements)
print(f"7. Sort: {np.sort(arr1)}")                       # Sorts the array
print(f"8. Power: {np.power(arr1, arr2)}")               # arr1 raised to power of arr2 element-wise
print(f"9. Floor division: {np.floor_divide(arr1, arr2)}") # Element-wise floor division

# Mathematical and statistical functions
print(f"10. Absolute value: {np.absolute(arr1)}")        # Absolute values of elements
print(f"11. Maximum value: {np.maximum(arr1, arr2)}")    # Element-wise maximum
print(f"12. Minimum value: {np.minimum(arr1, arr2)}")    # Element-wise minimum
print(f"13. Rounding: {np.round(arr1)}")                 # Round elements to nearest integer
print(f"14. Exponential: {np.exp(arr1)}")                # e^arr1 for each element
print(f"15. Logarithm: {np.log(arr1)}")                  # Natural log (ln) of elements
print(f"16. Square root: {np.sqrt(arr1)}")               # Square root of each element
print(f"17. Conjugate: {np.conj(arr1)}")                 # Complex conjugate (same for real numbers)

# Aggregation functions
print(f"18. Sum: {np.sum(arr1)}")                        # Sum of all elements
print(f"19. Mean: {np.mean(arr1)}")                      # Average of elements
print(f"20. Median: {np.median(arr1)}")                  # Median value
print(f"21. Standard deviation: {np.std(arr1)}")         # Standard deviation
print(f"22. Variance: {np.var(arr1)}")                   # Variance

# Logical operations
print(f"23. All true: {np.all(arr1)}")                   # Checks if all elements are non-zero
print(f"24. Any true: {np.any(arr1)}")                   # Checks if any element is non-zero

# Cumulative functions
print(f"25. Cumsum: {np.cumsum(arr1)}")                  # Cumulative sum
print(f"26. Cumprod: {np.cumprod(arr1)}")                # Cumulative product
print(f"27. Diff: {np.diff(arr1)}")                      # Difference between consecutive elements
print(f"28. Ediff1d: {np.ediff1d(arr1)}")                # Similar to diff but flattens and simplifies

# Set membership and sorting helpers
print(f"29. In1d: {np.isin(arr1, [12, 22])}")            # Checks if elements are in given list
print(f"30. Partition: {np.partition(arr1, 2)}")         # Rearranges so that the 2nd smallest is at position 2
print(f"40. Argpartition: {np.argpartition(arr1, 2)}")   # Indices that would partition array

# Sorting and index-related
print(f"50. Sort: {np.sort(arr1)}")                      # Sorted version of arr1
print(f"51. Argsort: {np.argsort(arr1)}")                # Indices that would sort the array
print(f"52. Searchsorted: {np.searchsorted(arr1, 22)}")  # Index to insert 22 to keep order

# Repeating and tiling
print(f"53. Repeat: {np.repeat(arr1, 2)}")               # Repeat each element twice
print(f"54. Tile: {np.tile(arr1, 2)}")                   # Repeat entire array twice

# Clipping and comparisons
print(f"55. Clip: {np.clip(arr1, 10, 20)}")              # Clip values outside [10, 20] to 10 or 20
print(f"56. Max: {np.max(arr1)}")                        # Maximum of the array
print(f"57. Min: {np.min(arr1)}")                        # Minimum of the array
print(f"58. Round: {np.round(arr1)}")                    # Same as earlier: round to nearest integer

# Comparisons
print(f"59. Allclose: {np.allclose(arr1, arr2)}")        # Check if all elements are approximately equal
print(f"60. Equal: {np.equal(arr1, arr2)}")              # Element-wise comparison for equality
print(f"61. Not equal: {np.not_equal(arr1, arr2)}")      # Element-wise comparison for inequality

# Sorting indices
print(f"62. Argsort: {np.argsort(arr1)}")                # Repeated: returns indices that would sort the array
