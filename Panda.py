import pandas as pd 
import numpy as np
ser = pd.Series() 
print("Pandas Series: ", ser) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data) 
print("Pandas Series:\n", ser)

import pandas as pd 
  
# Calling DataFrame constructor 
df = pd.DataFrame() 
print(df)

# list of strings 
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df)

import pandas as pd
import pandas as pd
 
# Calling DataFrame constructor
df = pd.DataFrame()
 
print(df)

import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

import pandas as pd
 
# initialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)
import pandas as pd
 
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
df = pd.DataFrame(dict)
 
print(df)

import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
print(df.index)  # Accessing the index

# Reset the index back to the default integer index
df_reset = df.reset_index()
print(df_reset)
# Reset the index back to the default integer index
df_reset = df.reset_index()
print(df_reset)
row = df.loc['Alice']
print(row)
# Set 'Age' as the new index
df_with_new_index = df.set_index('Age')
print(df_with_new_index)

#Data Frame
import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)
# Access the 'Age' column
age_column = df['Age']
print(age_column)
# Access the row at index 1 (second row)
second_row = df.iloc[1]
print(second_row)
# Access the first three rows and the 'Name' and 'Age' columns
subset = df.loc[0:2, ['Name', 'Age']]
print(subset)
# Access rows where 'Age' is greater than 25
filtered_data = df[df['Age'] > 25]
print(filtered_data)
# Access the 'Salary' of the row with label 2
salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)
#select
import pandas as pd

# Load the data
data = pd.read_csv("nba.csv", index_col="Name")
print("Dataset")
display(data.head(5))

# Select a single column
first = data["Age"]
print("\nSingle Column selected from Dataset")
display(first.head(5))
first = data[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset")
display(first.head(5))  
# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]


print(first, "\n\n\n", second)
# Select multiple rows
first = data.loc[["Avery Bradley", "R.J. Hunter"]]
display(first)
# Select two rows and three columns
first = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print(first)
# Select all rows and specific columns
first = data.loc[:, ["Team", "Number", "Position"]]
print(first)
import pandas as pd
data = pd.read_csv("nba.csv", index_col="Name")

# Select a single row by position
row2 = data.iloc[3]
print(row2)
# Select multiple rows by position
row2 = data.iloc[[3, 5, 7]]
display(row2)
# Select two rows and two columns by position
row2 = data.iloc[[3, 4], [1, 2]]
print(row2)
# Select all rows and specific columns
row2 = data.iloc[:, [1, 2]]
print(row2)
#slicing
import pandas as pd

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
df # data frame before slicing
# Slicing rows in data frame
df1 = df.iloc[0:4]

# data frame after slicing
df1
# Slicing columnss in data frame
df1 = df.iloc[:, 0:2]

# data frame after slicing
df1
specific_cell_value = df.iloc[2, 3]  # Row 2, Column 3 (Salary)
print("Specific Cell Value:", specific_cell_value)
filtered_data = df[df['Age'] > 35].iloc[:, :]  # Select rows where Age is greater than 35
print("\nFiltered Data based on Age > 35:\n", filtered_data)
df_custom = df.set_index('Name')
df_custom
sliced_rows_custom = df_custom.loc['A.B.D Villers':'S.Smith']
sliced_rows_custom
specific_cell_value = df_custom.loc['V.Kohli', 'Salary']
print("\nValue of the Specific Cell (V.Kohli, Salary):", specific_cell_value)

# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# display dataframe
display(dataFrame)
# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
# filter dataframe
display(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])
# import module
import pandas as pd
import numpy as np

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# filter dataframe                                   
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
display(dataFrame.loc[filtered_values])
# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# filter dataframe 
display(dataFrame.query('Salary  <= 100000 & Age < 40 & JOB.str.startswith("C").values'))
# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# filter dataframe 
display(dataFrame[(dataFrame['Salary']>=100000) & (dataFrame['Age']<40) & dataFrame['JOB'].str.startswith('P')][['Name','Age','Salary']])
# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

# filter dataframe 
display(dataFrame[dataFrame.eval("Salary <=100000 & (Age <40) & JOB.str.startswith('A').values")])
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
})

# Filter DataFrame based on multiple conditions
filtered_df = df[(df['Age'] > 30) & (df['City'] == 'New York')]
print(filtered_df)
# Filter where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
# List of cities
cities = ['New York', 'Chicago']

# Filter DataFrame by list of cities
filtered_df = df[df['City'].isin(cities)]
print(filtered_df)
# List of cities
cities = ['New York', 'Chicago']

# Filter DataFrame by list of cities
filtered_df = df[df['City'].isin(cities)]
print(filtered_df)
# List of cities
cities = ['New York', 'Chicago']

# Filter DataFrame by list of cities
filtered_df = df[df['City'].isin(cities)]
print(filtered_df)
# Using query to filter DataFrame
filtered_df = df.query('Age > 30 and City == "New York"')
print(filtered_df)
# concatenate
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])

print(df, "\n\n", df1)
# using a .concat() method
frames = [df, df1]

res1 = pd.concat(frames)
res1
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

# Define a dictionary containing employee data
data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

print(df, "\n\n", df1)
# applying concat with axes
# join = 'inner'
res2 = pd.concat([df, df1], axis=1, join='inner')

res2
# using a .concat for
# union of dataframe
res2 = pd.concat([df, df1], axis=1, sort=False)

res2
# using join_axes
res3 = pd.concat([df, df1], axis=1, join_axes=[df.index])
 
res3
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])

print(df, "\n\n", df1)
# using append function

res = df.append(df1)
res
# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
    
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
  
  
print(df, "\n\n", df1) 
# using ignore_index
res = pd.concat([df, df1], ignore_index=True)
 
res
# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1)  
# using keys 
frames = [df, df1 ]
 
res = pd.concat(frames, keys=['x', 'y'])
res
# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# creating a series
s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')
 
print(df, "\n\n", s1) 
# combining series and dataframe
res = pd.concat([df, s1], axis=1)
 
res
# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1) 
# using .merge() function
res = pd.merge(df, df1, on='key')
 
res
# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1) 
# merging dataframe using multiple keys
res1 = pd.merge(df, df1, on=['key', 'key1'])
 
res1
# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1) 
# using keys from left frame
res = pd.merge(df, df1, how='left', on=['key', 'key1'])
 
res
# using keys from right frame
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])
 
res1
# getting union  of keys
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
 
res2
# getting intersection of keys
res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])
 
res3
# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32]} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
 
 
print(df, "\n\n", df1)  
# joining dataframe
res = df.join(df1)
 
res
# getting union
res1 = df.join(df1, how='outer')
 
res1
# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],
        'Key':['K0', 'K1', 'K2', 'K3']} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
 
 
print(df, "\n\n", df1) 
# using on argument in join
res2 = df.join(df1, on='Key')
 
res2
# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav'], 
        'Age':[27, 24, 22]} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))
 
index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                   names=['key', 'Y'])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index= index)
 
 
print(df, "\n\n", df1)
# joining singly indexed with
# multi indexed
result = df.join(df1, how='inner')
 
result
#sorting
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

# Sorting by 'Age' in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df)
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

# Sorting by 'Age' in descending order
sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

# Sorting by 'Score' in ascending order
sorted_df = df.sort_values(by=['Age', 'Score'])
print(sorted_df)
import pandas as pd
data_with_nan = {"Name": ["Alice", "Bob", "Charlie", "David"],"Age": [28, 22, None, 22]}
df_nan = pd.DataFrame(data_with_nan)

# Sort by 'Age', placing missing values first
sorted_df = df_nan.sort_values(by="Age", na_position="first")
print(sorted_df)
import pandas as pd

# Create a DataFrame with duplicate 'Age' values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)

# Sort the DataFrame by 'Age' using the 'mergesort' algorithm
sorted_df = df.sort_values(by='Age', kind='mergesort')
print(sorted_df)
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Name', key=lambda col: col.str.lower())
print(sorted_df)
#pivot
import pandas as pd
 
# creating dataframe
df = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana',
                               'Beans', 'Orange', 'Broccoli', 'Banana'],
                   'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit',
                                'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})
df
pivot = df.pivot_table(index=['Product'],
                       values=['Amount'],
                       aggfunc='sum')
print(pivot)
# creating pivot table of total
# sales category-wise aggfunc = 'sum'
pivot = df.pivot_table(index=['Category'],
                       values=['Amount'],
                       aggfunc='sum')
print(pivot)
pivot = df.pivot_table(index=['Product', 'Category'],
                       values=['Amount'], aggfunc='sum')
print(pivot)
# 'mean', 'min'} will get median, mean and
# minimum of sales respectively
pivot = df.pivot_table(index=['Category'], values=['Amount'],
                       aggfunc={'median', 'mean', 'min'})
print(pivot)
pivot = df.pivot_table(index=['Product'], values=['Amount'],
                       aggfunc={'median', 'mean', 'min'})
print(pivot)
#series
import pandas as pd
 
# Creating empty series
ser = pd.Series()
 
print(ser)
# import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
 
ser = pd.Series(data)
print(ser)
# import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
 
ser = pd.Series(data)
print(ser)
# import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
 
# providing an index
ser = pd.Series(data, index=[10, 11, 12, 13, 14])
print(ser)
import pandas as pd
 
# a simple list
list = ['g', 'e', 'e', 'k', 's']
 
# create series form a list
ser = pd.Series(list)
print(ser)
import pandas as pd
 
# a simple dictionary
dict = {'Geeks': 10,
        'for': 20,
        'geeks': 30}
 
# create series from dictionary
ser = pd.Series(dict)
 
print(ser)
import pandas as pd
 
import numpy as np
 
# giving a scalar value with index
ser = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
 
print(ser)
# import pandas and numpy
import pandas as pd
import numpy as np
 
# series with numpy linspace()
ser1 = pd.Series(np.linspace(3, 33, 3))
print(ser1)
 
# series with numpy linspace()
ser2 = pd.Series(np.linspace(1, 100, 10))
print(& quot
       \n"       , ser2)
# code
import pandas as pd
ser=pd.Series(range(10))
print(ser)
import pandas as pd
ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print(ser)
import pandas as pd
import numpy as np
ser=np.arange(10,15)
serobj=pd.Series(data=ser*5,index=ser)
print(serobj)

# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
# retrieve the first element
print(ser[0])
# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
# retrieve the first element
print(ser[:5])
# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)

# retrieve the first element
print(ser[-10:])
# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

ser = pd.Series(df['Name'])
ser.head(10)
# get first five names
ser[:5]
# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data, index=[10, 11, 12, 13, 14,
                             15, 16, 17, 18, 19, 20, 21, 22])

# accessing a element using index element
print(ser[16])
# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data, index=[10, 11, 12, 13, 14,
                             15, 16, 17, 18, 19, 20, 21, 22])

# accessing a multiple element using
# index element
print(ser[[10, 11, 12, 13, 14]])
# importing pandas and numpy
import pandas as pd
import numpy as np

ser = pd.Series(np.arange(3, 9), index=['a', 'b', 'c', 'd', 'e', 'f'])

print(ser[['a', 'd']])
# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

ser = pd.Series(df['Name'])
ser.head(10)

import pandas as pd
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Adding the two Series
result = s1 + s2
print(result)

import pandas as pd
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([10, 25, 30])

# Comparing the two Series
result = s1 == s2
print(result)

import pandas as pd
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Subtracting the DataFrames
result = df1 - df2
print(result)

import pandas as pd
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [5, 15, 35], 'B': [30, 60, 55]})

# Checking if elements of df1 are greater than df2
result = df1 > df2
print(result)

import pandas as pd
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [5, 15, 35], 'B': [30, 60, 55]})

# Checking if elements of df1 are greater than df2
result = df1 > df2
print(result)

import pandas as pd
s1 = pd.Series([True, False, True])
s2 = pd.Series([False, False, True])

# Applying logical AND
result = s1 & s2
print(result)

import pandas as pd 
df1 = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
df2 = pd.DataFrame({'A': [1, None, 3], 'B': [None, 5, 6]})

# Adding the DataFrames
result = df1 + df2
print(result)

# importing pandas as pd
import pandas as pd

# Creating the Series
series = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon'])

# Print the series
print(series)

# Creating the row axis labels
series.index = ['City 1', 'City 2', 'City 3', 'City 4'] 

# Print the series
print(series)

# Creating the row axis labels
series.index = ['City 1', 'City 1', 'City 3', 'City 3'] 

# Print the series
print(series)

# importing pandas as pd
import pandas as pd

Date = ['1/1/2018', '2/1/2018', '3/1/2018', '4/1/2018']
Index_name = ['Day 1', 'Day 2', 'Day 3', 'Day 4']

# Creating the Series
sr = pd.Series(data = Date,        # Series Data
              index = Index_name   # Index
              )             

# Print the series
print(sr)
# print the index labels
print(sr.index)
import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s.index)  # Output: Index(['a', 'b', 'c'], dtype='object')
# Setting index at creation
s = pd.Series([1, 2, 3], index=['x', 'y', 'z'])

# Modifying index of an existing Series
s.index = ['a', 'b', 'c']
print(s)
# Create a Series with an index
s = pd.Series([10, 20, 30], index=pd.Index(['apples', 'oranges', 'bananas'], name='fruits'))

# Access the index name
print(s.index.name)  # Output: 'fruits'
# importing Pandas & numpy 
import pandas as pd 
import numpy as np 
  
# numpy array 
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
# creating series 
s = pd.Series(data) 
print(s) 

# importing Pandas & numpy 
import pandas as pd 
import numpy as np 
  
# numpy array 
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
# creating series 
s = pd.Series(data, index =[1000, 1001, 1002, 1003, 1004]) 
print(s) 
import pandas as pd
import json
data = {
    "One": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Two": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    }
}
# Corrected the attribute name to dumps
df_read_json = pd.read_json(json.dumps(data), orient='index')
print("DataFrame using pd.read_json() method:")
print(df_read_json)
import pandas as pd
import json
 
# Using JSON module and pd.json_normalize() method
json_data = json.dumps(data)
df_json_normalize = pd.json_normalize(json.loads(json_data))
print("\nDataFrame using JSON module and pd.json_normalize() method:")
print(df_json_normalize)
import pandas as pd
 
df = pd.DataFrame(data)
 
print(df)
import pandas as pd 
# Creating Dataframe  
df = pd.DataFrame([['a', 'b'], ['c', 'd']], 
                  index =['row 1', 'row 2'], 
                  columns =['col 1', 'col 2']) 
  
# Indication of expected JSON string format 
print(df.to_json(orient ='split')) 
  
print(df.to_json(orient ='index'))
works_data = json_normalize(data = d['programs'], 
                            record_path ='works',  
                            meta =['id', 'orchestra', 'programID', 'season']) 
works_data.head(3)
soloist_data = json_normalize(data = d['programs'], 
                              record_path =['works', 'soloists'], 
                              meta =['id']) 
  
soloist_data.head(3) 
#Data manuplate
# Importing pandas and numpy
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(data)

# Checking for missing values using isnull()
missing_values = df.isnull()

print(missing_values)
# Importing pandas and numpy
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(data)

# Checking for non-missing values using notnull()
non_missing_values = df.notnull()

print(non_missing_values)
# Importing pandas
import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)

# Filling missing values with 0
df.fillna(0)
df.fillna(method='pad')  # Forward fill
df.fillna(method='bfill')  # Backward fill
# importing pandas as pd 
import pandas as pd
  
# Creating the dataframe  
df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]}) 
  
# Print the dataframe 
print(df)
# to interpolate the missing values 
df.interpolate(method ='linear', limit_direction ='forward')
import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

df = pd.DataFrame(dict)

# Drop rows with at least one missing value
df.dropna()
dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

df = pd.DataFrame(dict)

# Drop rows where all values are missing
df.dropna(how='all')
dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [60, 67, 68, 65]}

df = pd.DataFrame(dict)

# Drop columns with at least one missing value
df.dropna(axis=1)
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}
df = pd.DataFrame(data)
display(df)

# Removing duplicates
unique_df = df.drop_duplicates()
display(unique_df)
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'SF', 'Chicago']
})

# Drop duplicates based on the 'Name' column
result = df.drop_duplicates(subset=['Name'])
print(result)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})

# Keep the last occurrence of duplicates
result = df.drop_duplicates(keep='last')
print(result)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})
# Drop all duplicates
result = df.drop_duplicates(keep=False)
print(result)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})
# Modify the DataFrame in place
df.drop_duplicates(inplace=True)
print(df)
# Remove duplicates considering only column 'A'
clean_df = df.drop_duplicates(subset=['A'])
print(clean_df)
has_duplicates = df.duplicated().any()
print(has_duplicates)  # True if duplicates exist  
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

df2 = pd.DataFrame({
    'A': [4, 2, 3],
    'B': ['d', 'b', 'c']
})

# Merge DataFrames and remove duplicates
merged_df = pd.merge(df1, df2, how='outer').drop_duplicates()
print(merged_df)
#change type
import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)

# Convert 'Age' column to float type
df['Age'] = df['Age'].astype(float)
print(df.dtypes)
# Example: Create a 'Join Date' column as a string
df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']

# Convert 'Join Date' to datetime type
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes)
# Convert 'Age' to float and 'Salary' to string
df = df.astype({'Age': 'float64', 'Salary': 'str'})
print(df.dtypes)

import numpy as np 
import pandas as pd 
  
# create a Dataframe 
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'], 
                            "Gender": ["", "", ""], 
                            "Age": [0, 0, 0]}) 
Mydataframe['Department'] = np.nan 
  
# show the dataframe 
print(Mydataframe) 
# import required libraries 
import numpy as np 
import pandas as pd 
  
# create a Dataframe 
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'], 
                            "Gender": ["", "", ""], 
                            "Age": [0, 0, 0]}) 
  
Mydataframe['Department'] = np.nan 
  
display(Mydataframe) 
  
Mydataframe.dropna(how='all', axis=1, inplace=True) 
  
# show the dataframe 
display(Mydataframe) 
# import required libraries 
import numpy as np 
import pandas as pd 
  
# create a Dataframe 
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'], 
                            "Gender": ["", "", ""], 
                            "Age": [0, 0, 0]}) 
  
Mydataframe['Department'] = np.nan 
display(Mydataframe) 
  
nan_value = float("NaN") 
Mydataframe.replace("", nan_value, inplace=True) 
  
Mydataframe.dropna(how='all', axis=1, inplace=True) 
  
# show the dataframe 
display(Mydataframe) 
# import required libraries 
import numpy as np 
import pandas as pd 
  
# create a Dataframe 
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'], 
                            "Gender": ["", "", ""], 
                            "Age": [0, 0, 0]}) 
  
Mydataframe['Department'] = np.nan 
display(Mydataframe) 
  
nan_value = float("NaN") 
Mydataframe.replace(0, nan_value, inplace=True) 
  
Mydataframe.dropna(how='all', axis=1, inplace=True) 
  
# show the dataframe 
display(Mydataframe) 
# import required libraries 
import numpy as np 
import pandas as pd 
  
# create a Dataframe 
Mydataframe = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'], 
                            "Gender": ["", "", ""], 
                            "Age": [0, 0, 0]}) 
  
Mydataframe['Department'] = np.nan 
display(Mydataframe) 
  
nan_value = float("NaN") 
Mydataframe.replace(0, nan_value, inplace=True) 
Mydataframe.replace("", nan_value, inplace=True) 
  
Mydataframe.dropna(how='all', axis=1, inplace=True) 
  
# show the dataframe 
display(Mydataframe) 
# Importing the necessary libraries
import pandas as pd
import numpy as np
 
# df stands for dataframe
df = pd.Series(['Gulshan', 'Shashank', 'Bablu',
                'Abhishek', 'Anand', np.nan, 'Pratap'])
 
print(df)
# we can change the dtype after
# creation of dataframe
print(df.astype('string'))
# now creating the dataframe as dtype = 'string'
import pandas as pd
import numpy as np
 
df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek',
                'Anand', np.nan, 'Pratap'], dtype='string')
 
print(df)
# now creating the dataframe as dtype = pd.StringDtype()
import pandas as pd
import numpy as np
 
df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek',
                'Anand', np.nan, 'Pratap'], dtype=pd.StringDtype())
 
print(df)
# python script for create a dataframe
# for string manipulations
import pandas as pd
import numpy as np
 
df = pd.Series(['night_fury1', 'Is  ', 'Geeks, forgeeks',
                '100', np.nan, '  Contributor '])
df
#upper()
print(df.str.upper())
# lower()
print(df.str.lower())
# strip()
print(df)
print('\nAfter using the strip:')
print(df.str.strip())
# split(pattern)
print(df)
print('\nAfter using the strip:')
print(df.str.split(','))
 
# now we can use [] or get() to fetch 
# the index values
print('\nusing []:')
print(df.str.split(',').str[0])
 
print('\nusing get():')
print(df.str.split(',').str.get(1))
# len()
print("length of the dataframe: ", len(df))
print("length of each value of dataframe:")
print(df.str.len())
# cat(sep=pattern)
print(df)
 
print("\nafter using cat:")
print(df.str.cat(sep='_'))
 
print("\nworking with NaN using cat:")
print(df.str.cat(sep='_', na_rep='#'))
# get_dummies()
print(df.str.get_dummies())
# startswith(pattern)
print(df.str.startswith('G'))
# endswith(pattern)
print(df.str.endswith('1'))
# replace(a,b)
print(df)
print("\nAfter using replace:")
print(df.str.replace('Geeks', 'Gulshan'))
# repeat(value)
print(df.str.repeat(2))
# count(pattern)
print(df.str.count('n'))
# find(pattern)
# in result '-1' indicates there is no
# value matching with given pattern in 
# particular row
print(df.str.find('n'))
# findall(pattern)
# in result [] indicates null list as 
# there is no value matching with given
# pattern in particular row
print(df.str.findall('n'))
# islower()
print(df.str.islower())
# isupper()
print(df.str.isupper()) 
# isnumeric()
print(df.str.isnumeric())
# swapcase()
print(df.str.swapcase())
import pandas as pd 
sports = pd.Series(['Virat', 'azam', 'fiNch', 'ShakiB', 'STOKES', 'KAne']) 
print(sports) 
print(s.str.upper())
print(s.str.lower()) 
print(s.str.isupper())
print(s.str.islower())
print(s.str.len())
print(s.str.startswith('a'))
print(s.str.split('a')) 
print(s.str.find('a')) 
print(s.str.strip()) 
print(s.str.replace('a', '')) 
# Python program to detect mixed data types in Pandas data frame

# Import the library Pandas
import pandas as pd
  
# Create the pandas DataFrame
data_frame = pd.DataFrame( [['tom', 10], ['nick', '15'], ['juli', 14.8]], columns=['Name', 'Age'])

# Traverse data frame to detect mixed data types
for column in data_frame.columns:
    print(column,':',pd.api.types.infer_dtype(data_frame[column]))
# Python program to fix mixed data types using astype() in Pandas data frame

# Import the library Pandas
import pandas as pd
  
# Create the pandas DataFrame
data_frame = pd.DataFrame( [['tom', 10], ['nick', '15'], ['juli', 14.8]], columns=['Name', 'Age'])

# Transforming mixed data types to single data type
data_frame[column] = data_frame[column].astype(int)

# Traverse data frame to detect data types after fix
for column in data_frame.columns:
    print(column,':',pd.api.types.infer_dtype(data_frame[column]))
# Python program to fix mixed data types using to_numeric() in Pandas data frame

# Import the library Pandas
import pandas as pd
  
# Create the pandas DataFrame
data_frame = pd.DataFrame( [['tom', 10], ['nick', '15'], ['juli', 14.8]], columns=['Name', 'Age'])

# Transforming mixed data types to single data type
data_frame[column] = data_frame[column].apply(lambda x: pd.to_numeric(x, errors = 'ignore'))

# Traverse data frame to detect data types after fix
for column in data_frame.columns:
  print(pd.api.types.infer_dtype(data_frame[column]))
