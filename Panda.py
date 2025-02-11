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

