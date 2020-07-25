import pandas as pd


df = pd.read_csv('sample.csv', sep =',', header =0)

def cleanup_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary

df['clean_salary'] = df.apply(cleanup_salary, axis=1)

df['rank'] = df['clean_salary'].rank(ascending=False)
print(df.sort_values('rank'))