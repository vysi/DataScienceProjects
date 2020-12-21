import numpy as np


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr_zip = list(zip(arr1, arr2))
print(arr_zip)

arr3 = np.concatenate([arr1, arr2])
print(arr3)

print(arr3.reshape(2, 4))
print()
print(arr3.reshape(4, 2))
