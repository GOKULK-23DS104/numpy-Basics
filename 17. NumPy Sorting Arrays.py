import numpy as np

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

print("Sorted array (flattened):\n", np.sort(a, axis=None))
print("Row-wise sort:\n", np.sort(a, axis=1))
print("Column-wise merge sort:\n", np.sort(a, axis=0, kind='mergesort'))

# Structured sort
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

arr = np.array(values, dtype=dtypes)

print("Sorted by name:\n", np.sort(arr, order='name'))
print("Sorted by graduation year and CGPA:\n", np.sort(arr, order=['grad_year', 'cgpa']))
