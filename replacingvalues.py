import pandas as pd

sample_data = pd.read_csv('sample.csv', sep=',', header=0)

df = sample_data.replace(['Male','Female'],['M','F'])

print(df[['first_name','last_name','gender']])