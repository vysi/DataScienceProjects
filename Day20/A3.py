import pandas as pd
import matplotlib.pylab as plt
import numpy as np


df = pd.read_csv('..data/names.csv', index_col='Id')
# Name Year Gender State Count

# 1
year = 2000
df_year = df[df['Year'] == year]
names = df_year.groupby('Name')['Count'].sum()

final = names[names > names.mean()]

print(f'Im Jahr {year} ist der Mittelwert gleich {names.mean()}.')
print('Die folgenden Namen wurden häufiger vergeben.')
for name in final.index:
    print(f'{name.capitalize()} wurde {final[name]} vergeben.')
