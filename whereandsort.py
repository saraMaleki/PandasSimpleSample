import pandas as pd


df = pd.read_csv('sample.csv', sep =',', header =0)

def cleanup_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary

df['clean_salary'] = df.apply(cleanup_salary, axis=1)

#print(df.loc[df['clean_salary'] > 50000])

#print(df.loc[(df['clean_salary'] > 50000) & (df['clean_salary'] < 60000)])

#print(df.loc[(df['clean_salary'] > 50000) & (df['clean_salary'] < 60000)].sort_values('clean_salary'))

print(df.loc[(df['clean_salary'] > 50000) & (df['clean_salary'] < 60000)].sort_values('clean_salary', ascending=False))

