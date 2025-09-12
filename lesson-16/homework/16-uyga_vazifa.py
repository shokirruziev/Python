import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr1)
# 2. Create 3x3 Matrix (2–10)
matrix = np.arange(2, 11).reshape(3, 3)
print("\n3x3 matrix with values from 2 to 10:\n", matrix)
# 3. Null Vector (10) & Update Sixth Value
vec = np.zeros(10)
print("\nNull vector:", vec)
vec[5] = 11
print("Update sixth value to 11:", vec)
# 4. Array from 12 to 38
arr2 = np.arange(12, 38)
print("\nArray with values from 12 to 38:", arr2)
# 5. Convert Array to Float Type
arr3 = np.array([1, 2, 3, 4])
arr_float = arr3.astype(float)
print("\nOriginal array:", arr3)
print("Array converted to float:", arr_float)
# 6. Celsius to Fahrenheit Conversion
C = np.array([0, 12, 45.21, 34, 99.91])
F = C * 9/5 + 32
print("\nValues in Centigrade degrees:", C)
print("Values in Fahrenheit degrees:", F)
# 7. Append Values to Array
arr4 = np.array([10, 20, 30])
arr_appended = np.append(arr4, [40, 50, 60, 70, 80, 90])
print("\nOriginal array:", arr4)
print("After append:", arr_appended)
# 8. Array Statistical Functions
arr5 = np.random.rand(10)
print("\nRandom array:", arr5)
print("Mean:", np.mean(arr5))
print("Median:", np.median(arr5))
print("Standard Deviation:", np.std(arr5))
# 9. Min and Max in 10x10 Random Array
arr6 = np.random.rand(10, 10)
print("\n10x10 random array:\n", arr6)
print("Min:", arr6.min())
print("Max:", arr6.max())
# 10. 3x3x3 Random Array
arr7 = np.random.rand(3, 3, 3)
print("\n3x3x3 random array:\n", arr7)
