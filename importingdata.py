import pandas as pd

#table
#excel , csv
#sql
#json

#other python structures
d ={
    "name": "sara",
    "age": 35
}
next_df = pd.DataFrame(d, index=[1])
print(next_df)



sample_data = pd.read_csv('sample.csv')
#read 5 first row of data
print(sample_data.head(5))
#read 5 last row of data
print(sample_data.tail(5))
#read dimension of data
print(sample_data.shape)
#some summary statistics of int, float 
print(sample_data.describe())
#field types
print(sample_data.info())