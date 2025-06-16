import numpy as np

arr1 = np.array([12.0945, 22.3456, 34.5678])

# --- Round Functions ---
# np.around(): Rounds to specified decimal places
print(f"Round off to 2 decimal places: {np.around(arr1, 2)}")  # Rounds to 2 decimal places
print(f"Round off to 1 decimal places: {np.around(arr1, 1)}")  # Rounds to 1 decimal place
print(f"Round off to 0 decimal places: {np.around(arr1, 0)}")  # Rounds to nearest whole number

# np.ceil(): Rounds up to the nearest integer (toward +∞)
print(f"ceil L to next value: {np.ceil(arr1)}")

# np.floor(): Rounds down to the nearest integer (toward -∞)
print(f"floor L to next value: {np.floor(arr1)}")

# np.rint(): Rounds to the nearest integer (even rounding for .5 values)
print(f"rint L to nearest integer: {np.rint(arr1)}")

# np.fix(): Rounds toward zero (truncates decimal part)
print(f"fix L to nearest integer: {np.fix(arr1)}")

# np.trunc(): Also truncates the decimal part (like fix)
print(f"trunc L to nearest integer: {np.trunc(arr1)}")

# --- Exponential and Logarithmic Functions ---
arr2 = np.array([1, 2, 3])

# np.exp(): Calculates e^x for each element
print(f"exp L to next value: {np.exp(arr2)}")

# np.exp2(): Calculates 2^x for each element
print(f"exp2 L to next value: {np.exp2(arr2)}")

# np.log(): Natural logarithm (base e)
print(f"log L to next value: {np.log(arr2)}")

# np.log2(): Base-2 logarithm
print(f"log2 L to next value: {np.log2(arr2)}")

# np.log10(): Base-10 logarithm
print(f"log10 L to next value: {np.log10(arr2)}")

# np.log1p(): Computes log(1 + x) accurately for small x
print(f"log1p L to next value: {np.log1p(arr2)}")

# --- Power and Root Functions ---

# np.power(): Raises each element to the power (here, squared)
print(f"power L to next value: {np.power(arr2, 2)}")

# np.sqrt(): Calculates square root of each element
print(f"sqrt L to next value: {np.sqrt(arr2)}")

# np.cbrt(): Calculates cube root of each element
print(f"cbrt L to next value: {np.cbrt(arr2)}")

# np.square(): Squares each element (same as power with 2)
print(f"square L to next value: {np.square(arr2)}")

# np.reciprocal(): Returns 1 / x for each element
print(f"reciprocal L to next value: {np.reciprocal(arr2)}")

# np.abs(): Returns absolute value of each element
print(f"abs L to next value: {np.abs(arr2)}")
