import pandas as pd


df = pd.read_csv('sample.csv', sep =',', header =0)
#print(df)

def cleanup_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary

df['clean_salary'] = df.apply(cleanup_salary, axis=1)

# print("Average Salary Per Gender")
# print(df.groupby('gender')['clean_salary'].mean())

def female_salary(row):
    if row['gender'] =='Female':
        return row['clean_salary']

df['female_average_salary'] = df.apply(female_salary, axis=1)

def male_salary(row):
    if row['gender'] =='Male':
        return row['clean_salary']

df['male_average_salary'] = df.apply(female_salary, axis=1)

# print("Average Salary Per Jobtitle")
# print(df.groupby('Job Title')['clean_salary','female_average_salary','male_average_salary'].mean())

#print all columns
pd.set_option('display.max_columns', None)

print("Average Salary Per Jobtitle Per City")
# print(df.groupby(['Job Title','City'])['clean_salary','female_average_salary','male_average_salary'].mean())
# print(df.groupby(['Job Title','City'])['clean_salary','female_average_salary','male_average_salary'].median())
# print(df.groupby(['Job Title','City'])['clean_salary','female_average_salary','male_average_salary'].max())
# print(df.groupby(['Job Title','City'])['clean_salary','female_average_salary','male_average_salary'].min())


#df.to_csv('output.csv')
#df.to_json('output.json')

#reset_index : column heading --> use column for the next statement
df2 = df.groupby(['Job Title'])['clean_salary'].min()
df3 =df.groupby(['Job Title'])['clean_salary'].min().reset_index()

#error
#print(df2.sort_values('clean_salary',ascending = False))
print(df3.sort_values('clean_salary',ascending = False))

