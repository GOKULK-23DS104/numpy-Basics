# 1. empty array with dimension:
import numpy as np
print("\n1.empty array with dimension:")
# Creates a 2D array with shape (1,2) using specified dimension ndmin=2.
# The elements are [2, 2], not uninitialized. 'ndmin=2' ensures it's at least 2D.
arr = np.array([2, 2], dtype=int, ndmin=2, order='C', like=None)
print(arr)

# 2. array with zero value:
import numpy as np
# Creates a 2x2 array filled with zeros.
# dtype=int ensures integer data type; order='F' is column-major (Fortran-style) memory layout.
arr = np.zeros((2, 2), dtype=int, order='F', like=None)
print("\n2.array with zero value:")
print(arr)

# 3. creates 1 dimensional values using arange(start, stop, step, dtype, like)
import numpy as np
# Creates a 1D array with values from 10 to 18 (excluding 20) with a step of 2.
# Equivalent to Python's range but returns a NumPy array.
arr = np.arange(10, 20, 2, dtype=int, like=None)
print("\n3.creates 1 dimensional values arrange(start,stop,step,dtype,like):")
print(arr)

# 4. creates array from the obj passed [list/tuple/set] using array(obj, dtype, ndim, order, subok)
import numpy as np
# List of mixed values (int and str) passed to array (data type inferred as string/object).
arr = np.array([1, 2, "3", 4, 5])  # dtype will become <U11 because of the string
# Tuple with mixed types (str and int).
arr1 = np.array(("a", "b", 1))  # dtype inferred as object
# Set with duplicate values (1 is repeated) and mixed types.
arr2 = np.array({1, 2, "a", 1})  # dtype inferred as object (unordered and unique)
# 2D array using nested list, dtype is explicitly object to allow mixed types.
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=object, ndmin=2)
print("\n4.creates array from the obj passed [list/tuple/set] array(obj,dtype,ndim,order,sublok):")
print(arr)     # 2D list array
print(arr1)    # tuple array
print(arr2)    # set array
