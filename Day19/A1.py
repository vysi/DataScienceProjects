import pandas as pd
import matplotlib.pylab as plt
import numpy as np


df = pd.read_csv('../Tag18/data/names.csv', index_col='Id')
# Name Year Gender State Count

# 1
years = df['Year'].sample(2)
year1 = years.min()
year2 = years.max()

name = df['Name'].sample(1).iloc[0]

name_bool = df['Name'] == name
year_bool = (df['Year'] >= year1) & (df['Year'] <= year2)

df_prep = df[name_bool & year_bool]
final = df_prep.groupby('Year')['Count'].sum()

print('Name:', name, '\n', final)


# 2
# final_print = pd.Series(data=0,
#                         index=range(year1,
#                                     year2 + 1))
# final_print.update(final)


final_print = final.reindex(range(year1, year2 + 1),
                            fill_value=0)

plt.bar(final_print.index, final_print)
# plt.plot(final_print, color = 'r')
plt.title(f'Anzahl des Namen "{name.capitalize()}" in den Jahren von {year1} bis {year2}')
plt.ylabel('Häufigkeit')
plt.xlabel('Jahre')
plt.show()
