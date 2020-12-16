# Create a matrix with 10 rows and 10 columns with
# random entries between 0 - 100.
#
# Output all entries from column 3 that are greater than 50.

import numpy as np

mat = np.random.randint(0, 101, (10, 10))

print(mat)
print()

print(mat[:, 2])

b_spalte = mat[:, 2] > 50
print(b_spalte)
print()
print(mat[:, 2][b_spalte])
