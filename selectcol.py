import pandas as pd


df = pd.read_csv('sample.csv', sep =',', header =0)

def cleanup_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary

df['clean_salary'] = df.apply(cleanup_salary, axis=1)

# print(df['first_name'])
# print(df[['first_name', 'clean_salary']])

# print(df.loc[df['clean_salary'] > 50000]['first_name'])
print(df.loc[df['clean_salary'] > 50000][['first_name','City','clean_salary']])