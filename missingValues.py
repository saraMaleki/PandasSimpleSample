import pandas as pd

sample_data = pd.read_csv('sample.csv')

sample_data['City'].fillna('London', inplace=True)
# print(sample_data.head(5))

median = sample_data['Latitude'].median()
sample_data['Latitude'].fillna(median, inplace=True)
# print(sample_data.head(5))

df = sample_data.dropna()
# print(df.head(5))

#duplicates
df_dup = sample_data.drop_duplicates()
print(df_dup.shape)

df_dupname = sample_data.drop_duplicates(['first_name'], keep='last')
print(df_dupname.shape)