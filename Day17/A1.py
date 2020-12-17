import matplotlib.pyplot as plt


x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31, 32,
     33, 34, 35, 36, 37, 18, 49, 50, 100]

# num_bins = 5
num_bins = [0, 10, 50, 75, 101]

anzProBin, bins, patches = plt.hist(x, num_bins, edgecolor='k')
print(anzProBin)
print(bins)
plt.show()

help(plt.hist)
