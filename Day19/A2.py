# Read the file 'Popular_Baby_Names.xlsx' and enter the
# top 3 most popular female names in 2013 for all # ethnicities.
# Ethnicities.
# # Columns: 'Year of Birth', 'Gender', 'Ethnicity',
# 'Child's First Name', 'Count', 'Rank'.
import pandas as pd


df = pd.read_excel('data/Popular_Baby_Names.xlsx')

b_female = df['Gender'] == 'FEMALE'
b_year = df['Year of Birth'] == 2013

dff = df[b_female & b_year]

etns = dff['Ethnicity'].unique()
# all_etns = df['Ethnicity'].unique()

# print(etns)
# print(all_etns)

for etn in etns:
    dffe = dff[dff['Ethnicity'] == etn]
    print(dffe.sort_values('Rank'))



# print(df[df['Ethnicity'] == 'WHITE NON HISP']['Year of Birth'].unique())
# # ersetze alle Einträge 'WHITE NON HISP' mit 'WHITE NON HISPANIC'
# df[df['Ethnicity'] == 'WHITE NON HISP'] = 'WHITE NON HISPANIC'
# print(df['Ethnicity'].unique())
