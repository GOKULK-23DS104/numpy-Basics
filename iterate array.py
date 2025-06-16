# 1. Iterate array using index
import numpy as np
print("\n1.iterate array:")
arr = np.array([3,4,5,6])
for i in range(arr.size):       # arr.size gives total number of elements
    print(arr[i])               # Access each element by index

# 2. Iterate array using 'in' operator
import numpy as np
print("\n2.iterate array using 'in' operator:")
arr = np.array([3,4,5,6])
for i in arr:                   # Directly loop through each element
    print(i)

# 3. Slice more than one element using different slicing patterns
import numpy as np
print("\n3.slice more than one element:")
arr = np.array([31, 44, 55, 16, 4, 23])

arr1 = arr[1:4]                 # Elements from index 1 to 3 → [44, 55, 16]
arr2 = arr[2:5]                 # Elements from index 2 to 4 → [55, 16, 4]
arr3 = arr[:-2]                 # All elements except last two → [31, 44, 55, 16]
arr4 = arr[2:]                  # Elements from index 2 to end → [55, 16, 4, 23]
arr5 = arr[::2]                 # Every 2nd element (step=2) → [31, 55, 4]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
