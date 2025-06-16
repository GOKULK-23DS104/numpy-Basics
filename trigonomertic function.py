import numpy as np
arr1 = np.array([12,22,34])

# Trigonometric functions (convert degrees to radians by multiplying with π/180)
print("\nTrigonometric functions (convert degrees to radians by multiplying with π/180):")
print(f"1.sin(arr1) = {np.sin(arr1 * np.pi / 180)}")          # Sine of each angle
print(f"2.sin hyperbolic(arr1) = {np.sinh(arr1 * np.pi / 180)}")  # Hyperbolic sine
print(f"3.cos(arr1) = {np.cos(arr1 * np.pi / 180)}")          # Cosine of each angle
print(f"4.cos hyperbolic(arr1) = {np.cosh(arr1 * np.pi / 180)}")  # Hyperbolic cosine
print(f"5.tan(arr1) = {np.tan(arr1 * np.pi / 180)}")          # Tangent of each angle
print(f"6.tan hyperbolic(arr1) = {np.tanh(arr1 * np.pi / 180)}")  # Hyperbolic tangent

# Inverse trigonometric functions (input must be in range [-1,1] for arcsin/arccos)
print("\nInverse trigonometric functions (input must be in range [-1,1] for arcsin/arccos):")
print(f"7.arcsin(arr1) = {np.arcsin(arr1 * np.pi / 180)}")    # Inverse sine
print(f"8.arccos(arr1) = {np.arccos(arr1 * np.pi / 180)}")    # Inverse cosine
print(f"9.arctan(arr1) = {np.arctan(arr1 * np.pi / 180)}")    # Inverse tangent
print(f"10.arctan2(arr1) = {np.arctan2(arr1 * np.pi / 180, 1)}")  # Element-wise arctangent of y/x, quadrant-aware

# Angle conversion
print("\nAngle conversion:")
print(f"11.deg2rad(arr1) = {np.deg2rad(arr1)}")               # Convert degrees to radians
print(f"12.rad2deg(arr1) = {np.rad2deg(arr1)}")               # Convert radians to degrees
print(f"13.degrees(arr1) = {np.degrees(arr1)}")               # Same as rad2deg
print(f"14.radians(arr1) = {np.radians(arr1)}")               # Same as deg2rad

# Rounding operations
print("\nRounding operations:")
print(f"15.rint(arr1) = {np.rint(arr1)}")                     # Round to nearest integer
print(f"16.fix(arr1) = {np.fix(arr1)}")                       # Truncate toward zero
print(f"17.floor(arr1) = {np.floor(arr1)}")                   # Round down to nearest integer
print(f"18.ceil(arr1) = {np.ceil(arr1)}")                     # Round up to nearest integer
print(f"19.trunc(arr1) = {np.trunc(arr1)}")                   # Truncate decimals (same as fix for positive numbers)

# Exponential and logarithmic operations
print("\nExponential and logarithmic operations:")
print(f"20.exp(arr1) = {np.exp(arr1)}")                       # e^x for each element
print(f"21.exp2(arr1) = {np.exp2(arr1)}")                     # 2^x for each element
print(f"22.log(arr1) = {np.log(arr1)}")                       # Natural log (base e)
print(f"23.log2(arr1) = {np.log2(arr1)}")                     # Base-2 logarithm
print(f"24.log10(arr1) = {np.log10(arr1)}")                   # Base-10 logarithm
print(f"25.log1p(arr1) = {np.log1p(arr1)}")                   # log(1 + x), more accurate for small x

# Power and root functions
print("\nPower and root functions:")
print(f"26.sqrt(arr1) = {np.sqrt(arr1)}")                     # Square root of each element
print(f"27.cbrt(arr1) = {np.cbrt(arr1)}")                     # Cube root
print(f"28.square(arr1) = {np.square(arr1)}")                 # x^2 for each element
print(f"29.reciprocal(arr1) = {np.reciprocal(arr1)}")         # 1/x for each element

# Sign-related and decomposition functions
print("\nSign-related and decomposition functions:")
print(f"30.sign(arr1) = {np.sign(arr1)}")                     # Sign function: -1 for negative, 0 for 0, 1 for positive
print(f"31.modf(arr1) = {np.modf(arr1)}")                     # Returns (fractional part, integer part) of each element
print(f"32.frexp(arr1) = {np.frexp(arr1)}")                   # Decomposes into mantissa and exponent: arr1 = mant * 2^exp
print(f"33.ldexp(arr1) = {np.ldexp(arr1,2)}")                 # Computes arr1 * (2^2) = arr1 * 4
