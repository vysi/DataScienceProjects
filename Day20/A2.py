import pandas as pd
import matplotlib.pylab as plt
import numpy as np


df = pd.read_csv('..data/names.csv', index_col='Id')
# Name Year Gender State Count

# 1
dff = df[df['Gender'] == 'F']
dfm = df[df['Gender'] == 'M']

f = dff['Name'].unique()
m = dfm['Name'].unique()

both = np.intersect1d(f, m)

print(both)

for name in both:
    print(name)
