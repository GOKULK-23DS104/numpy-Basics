import numpy as np

arr = np.array([2, 4, 6, 8, 10])
c = arr.copy()
v = arr.view()
ass = arr

print(f"arr: {arr}")
print(f"IDs -> view: {id(v)}, assign: {id(ass)}, original: {id(arr)}")
print(f"Base of copy: {c.base}")
print(f"Base of view: {v.base}")
