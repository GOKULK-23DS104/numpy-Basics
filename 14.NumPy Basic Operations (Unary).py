import numpy as np
a = np.array([1, 2, 5, 3])
print("Add 1 to each element:\n", a + 1)
print("Subtract 3:\n", a - 3)
print("Multiply by 10:\n", a * 10)
print("Square of elements:\n", a ** 2)

a *= 2
print("Doubled original array:\n", a)

# Transpose
a = np.array([[1, 2, 3],
              [3, 4, 5],
              [9, 6, 0]])
print("Original array:\n", a)
print("Transpose:\n", a.T)
