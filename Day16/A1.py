# Given is the following list of colors:
#
# Use Numpy to:
#
# Output only the green ones.
# Count how many green and how many red elements are present.
#
# Do NOT! loop.

import numpy as np

l = ['grün', 'rot','grün','grün','rot', 'grün','rot']

arr = np.array(l)

print(arr[arr == 'grün'])
print(len(arr[arr == 'grün']))
print(len(arr[~(arr == 'grün')]))
