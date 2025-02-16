import pandas as pd 
import numpy as np
ser = pd.Series() 
print("Pandas Series: ", ser) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data) 
print("Pandas Series:\n", ser)
df = pd.DataFrame(); print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
df = pd.DataFrame(); print(df)

data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data); print(df)
dic = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
    'degree': ["MBA", "BCA", "M.Tech", "MBA"],
    'score':[90, 40, 80, 98]}
df = pd.DataFrame(dic);print(df)
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 55000, 40000, 70000, 48000]}
df = pd.DataFrame(data); print(df.index)  
df_reset = df.reset_index(); print(df_reset)
row = df[df['Name'] == 'Alice']  
print(row)
print(df.set_index('Age'))
age_column = df['Age']; print(age_column)
second_row = df.iloc[1]; print(second_row)
subset = df.loc[0 : 2, ['Name', 'Age']]
print(subset)
filt = df[df['Age'] > 25]; print(filt)
salaryIdx2 = df.at[2, 'Salary']; print(salaryIdx2)
"""
data = pd.read_csv("nba.csv", index_col="Name")
print("Dataset:")
print(data.head(5)) 
first = data["Age"]
print("\nSingle Column selected from Dataset:")
print(first.head(5)) 
first = data[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset:")
print(first.head(5)) 

data = pd.read_csv("nba.csv", index_col="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n", second)
first = data.loc[["Avery Bradley", "R.J. Hunter"]]
print("\nMultiple rows selection:\n")
print(first)
first = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print("\nSelecting specific rows and columns:\n")
print(first)
first = data.loc[:, ["Team", "Number", "Position"]]
print("\nSelecting all rows for specific columns:\n")
print(first)

data = pd.read_csv("nba.csv", index_col="Name")
row2 = data.iloc[3]
print("\nSingle row selection by position:\n")
print(row2)
row2 = data.iloc[[3, 5, 7]]
print("\nMultiple rows selection by position:\n")
print(row2)  
row2 = data.iloc[[3, 4], [1, 2]]
print("\nSelecting specific rows and columns by position:\n")
print(row2)
row2 = data.iloc[:, [1, 2]]
print("\nSelecting all rows for specific columns by position:\n")
print(row2)
"""
lst = [
    ['M.S.Dhoni', 36, 75, 5428000], ['A.B.D Villers', 38, 74, 3428000],
    ['V.Kohli', 31, 70, 8428000], ['S.Smith', 34, 80, 4428000],
    ['C.Gayle', 40, 100, 4528000], ['J.Root', 33, 72, 7028000],
    ['K.Peterson', 42, 85, 2528000]]
df = pd.DataFrame(lst, columns=['Name', 'Age', 'Weight', 'Salary']); print(df)
df1 = df.iloc[0:4]; print(df1)
df1 = df.iloc[:, 0:2]; print(df1)
cell = df.iloc[2, 3]  
print("Specific Cell Value:", cell)
filt = df[df['Age'] > 35].iloc[:, :]  
print("\nFiltered Data based on Age > 35:\n", filt)
df_custom = df.set_index('Name'); print(df_custom)
sliced = df_custom.loc['A.B.D Villers':'S.Smith']; print(sliced)
cell= df_custom.loc['V.Kohli', 'Salary']
print("\nValue of the Specific Cell (V.Kohli, Salary):", cell)

import pandas as pd
import numpy as np  #l
dataFrame = pd.DataFrame({
    'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ', '  ROSS    ', 'CHANDLER', ' JOEY    '],
    'Age': [30, 35, 37, 33, 34, 30],
    'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
    'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY', 'IT', 'ARTIST']
})

print(dataFrame)
filtered_data = dataFrame.loc[
    (dataFrame['Salary'] >= 100000) & 
    (dataFrame['Age'] < 40) & 
    (dataFrame['JOB'].str.startswith('D')), 
    ['Name', 'JOB']
]
print( filtered_data)
filtered_indices = np.where(
    (dataFrame['Salary'] >= 100000) & 
    (dataFrame['Age'] < 40) & 
    (dataFrame['JOB'].str.startswith('D'))
)[0]  
print( filtered_indices)

print( dataFrame.iloc[filtered_indices])  
filtered_query = dataFrame[dataFrame['JOB'].str.startswith("C") & (dataFrame['Salary'] <= 100000) & (dataFrame['Age'] < 40)]
print("\nFiltered DataFrame using query() (for 'C' jobs):\n", filtered_query)
filtered_p = dataFrame[(dataFrame['Salary'] >= 100000) & (dataFrame['Age'] < 40) & dataFrame['JOB'].str.startswith('P')]
print("\nFiltered DataFrame for 'P' jobs:\n", filtered_p[['Name', 'Age', 'Salary']])
dataFrame['job_starts_with_A'] = dataFrame['JOB'].str.startswith('A')  
filtered_eval = dataFrame[dataFrame.eval("Salary <= 100000 & (Age < 40) & job_starts_with_A")]
print("\nFiltered DataFrame using eval():\n", filtered_eval)

dataFrame = pd.DataFrame({
    'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ', '  ROSS    ', 'CHANDLER', ' JOEY    '],
    'Age': [30, 35, 37, 33, 34, 30],
    'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
    'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY', 'IT', 'ARTIST']})
print(dataFrame)
filtered_data = dataFrame.loc[
    (dataFrame['Salary'] >= 100000) & 
    (dataFrame['Age'] < 40) & 
    (dataFrame['JOB'].str.startswith('D')), 
    ['Name', 'JOB']
]
print(filtered_data)
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
print(dataFrame.loc[filtered_values])
print(dataFrame[(dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & dataFrame['JOB'].str.startswith('P')][['Name','Age','Salary']])

print(dataFrame[dataFrame.eval("Salary"<=100000 & (Age <40) & JOB.str.startswith('A').values)])

