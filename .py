import pandas as pd 
import numpy as np
ser = pd.Series() 
print("Pandas Series: ", ser) 
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data, index = [10, 11, 12, 13, 14])
ser = pd.Series(data) 
print("Pandas Series:\n", ser)
df = pd.DataFrame(); print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
df = pd.DataFrame(); print(df)
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df1 - df2, df1 > df2)
df1 = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
df2 = pd.DataFrame({'A': [1, None, 3], 'B': [None, 5, 6]})
print(df1 + df2)
s1 = pd.Series([True, False, True])
s2 = pd.Series([False, False, True])
print(s1 & s2)
list = ['g', 'e', 'e', 'k', 's']
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(pd.Series(list))
series = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon'])
print(series)
series.index = ['City 1', 'City 1', 'City 3', 'City 3'] 
print(series)
dic = {'Geeks': 10, 'for': 20, 'geeks': 30}
print(pd.Series(dict))
print(pd.Series(10, index = [0, 1, 2, 3, 4, 5]))
print(pd.Series(np.linspace(3, 33, 3))
print(pd.Series(np.linspace(1, 100, 10)))
print(pd.Series(range(10)))
print(pd.Series(range(1,20,3), index = [x for x in 'abcdefg']))
ser = np.arange(10,15)
obj = pd.Series(data = ser*5,index = ser)
print(serobj)
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
print(ser[0], ser[:5], ser[-10:])
ser = pd.Series(data, index = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
print(ser[16])
print(ser[[10, 11, 12, 13, 14]])
ser = pd.Series(np.arange(3, 9), index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(ser[['a', 'd']])
s1 = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])
print(s1 + s2, s1 == s2)
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

df = pd.read_csv("nba.csv")
ser = pd.Series(df['Name'])
print(ser.head(10))
# get first five names
ser[:5]
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
import pandas as pd
import json
data = {
    "One": { "0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60
    },
    "Two": { "0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102
    }
}
print(pd.read_json(json.dumps(data), orient = 'index'))
json_data = json.dumps(data)
normalize = pd.json_normalize(json.loads(json_data))
print(normalize)
data = {'col1': [1, 2], 'col2': [3, 4]}  
df = pd.DataFrame(data)
df = pd.DataFrame([
    ['a', 'b'], ['c', 'd']], 
    index = ['row 1', 'row 2'], 
    columns = ['col 1', 'col 2'])  
print("\nJSON (Split format):\n", df.to_json(orient = 'split'))  
print("\nJSON (Index format):\n", df.to_json(orient = 'index'))
d = {
    "programs": [{
            "id": 1,
            "orchestra": "New York Philharmonic",
            "programID": "001",
            "season": "2022",
            "works":[
                {"title": "Symphony No. 5", "composer": "Beethoven"},
                {"title": "Piano Concerto No. 2", "composer": "Rachmaninoff"}
            ]
        }
    ]
}
works_data = pd.json_normalize(data=d['programs'], record_path='works',  
   meta=['id', 'orchestra', 'programID', 'season']) 
print("\nWorks Data (First 3 rows):\n", works_data.head(3))
soloist_data = pd.json_normalize(data=d['programs'],record_path=['works', 'soloists'], 
    meta=['id'], errors='ignore')  
print("\nSoloist Data (First 3 rows):\n", soloist_data.head(3))
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Spending Score (1-100)': [50, 80, 45, 90, 30],
    'Age': [25, 40, 35, 50, 45]}
frame = pd.DataFrame(data)
def fun(value):
    return "Yes" if value > 70 else "No"
frame['Customer Satisfaction'] = frame['Spending Score (1-100)'].apply(fun)
const = frame['Age'].max()
if const > 0: 
    frame['Age'] = frame['Age'].apply(lambda x: x / const)
print(frame.head())
frame.plot(x='CustomerID', y='Spending Score (1-100)', kind='scatter')
plt.title("CustomerID vs Spending Score")
plt.show()
frame['Spending Score (1-100)'].plot.hist(bins=5, alpha=0.7)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score (1-100)")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame([
    [180000, 110, 18.9, 1400],
    [360000, 905, 23.4, 1800],
    [230000, 230, 14.0, 1300],
    [60000, 450, 13.5, 1500]
], columns=['Col A', 'Col B', 'Col C', 'Col D'])
print(df.head())
df.plot(kind = 'bar', title = "Original Data")
plt.show()
df_max_scaled = df / df.abs().max()
print(df_max_scaled.head())
df_max_scaled.plot(kind = 'bar', title = "Max Normalized Data")
plt.show()
df_min_max_scaled = (df - df.min()) / (df.max() - df.min())
print(df_min_max_scaled.head())
df_min_max_scaled.plot(kind = 'bar', title = "Min-Max Normalized Data")
plt.show()
df_z_scaled = (df - df.mean()) / df.std()
print(df_z_scaled.head())
df_z_scaled.plot(kind='bar', title="Z-Score Normalized Data")
plt.show()
import numpy as np
import pandas as pd
dataset = pd.read_csv("diamonds.csv")
print(dataset.head(5))
cut_sum = dataset.groupby('cut').sum()
print(cut_sum)
cut_color_min = dataset.groupby(['cut', 'color']).agg('min')
print(cut_color_min)
agg_functions = {
    'price': ['sum', 'mean', 'median', 'min', 'max', 'prod']
}
color_agg = dataset.groupby(['color']).agg(agg_functions)
print(color_agg)
cut_sum.to_csv("cut_sum.csv")
cut_color_min.to_csv("cut_color_min.csv")
color_agg.to_csv("color_agg.csv")
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Title': ['The Crown', 'Stranger Things', 'Breaking Bad', 'The Mandalorian', 'Avatar: The Last Airbender', 'The Office', 'Game of Thrones', 'Cosmos: A Spacetime Odyssey', 'The Good Place', 'Black Mirror', 'The Chosen', 'The Bible'],
    'Genre': ['Drama', 'Sci-Fi', 'Drama', 'Sci-Fi', 'Animation', 'Comedy', 'Fantasy', 'Documentary', 'Comedy', 'Sci-Fi', 'Drama', 'Drama'],
    'Release_Year': [2016, 2016, 2008, 2019, 2005, 2005, 2011, 2014, 2016, 2011, 2019, 2013],
    'Director': ['Peter Morgan', 'The Duffer Brothers', 'Vince Gilligan', 'Jon Favreau', 'Michael Dante DiMartino, Bryan Konietzko', 'Greg Daniels', 'David Benioff, D. B. Weiss', 'Brannon Braga', 'Michael Schur', 'Charlie Brooker', 'Dallas Jenkins', 'Various'],
    'Seasons': [4, 4, 5, 2, 3, 9, 8, 1, 4, 5, 2, 1],
    'Duration_Minutes': [60, 50, 47, 40, 23, 22, 57, 60, 22, 60, 45, 43]
}
tv_serials_df = pd.DataFrame(data)
print(tv_serials_df.head())
genre_seasons = tv_serials_df.groupby('Genre')['Seasons'].mean()
plt.figure(figsize = (10, 6))
genre_seasons.plot(kind = 'bar', color = 'coral')
plt.title('Bar Plot of Average Seasons by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Seasons')
plt.xticks(rotation=45)
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.show()
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
# Filter DataFrame based on multiple conditions
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago'] })
filt = df[(df['Age'] > 30) & (df['City'] == 'New York')]; print(filt)
print(df[df['Age'] > 30])
cities = ['New York', 'Chicago']
print(df[df['City'].isin(cities)])
print(df.query('Age' > 30 and 'City' == 'New York'))

data1 =
    {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
data2 = 
    {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
    'Age': [17, 14, 12, 52],
    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
    'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1, index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
frames = [df, df1]
print(pd.concat(frames))
print(df.append(df1))
print(pd.concat(frames, keys=['x', 'y']))
data1 = 
    {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
    'Mobile No': [97, 91, 58, 76]}
data2 = 
    {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
    'Age': [22, 32, 12, 52],
    'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
    'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
    'Salary': [1000, 2000, 3000, 4000]}
df = pd.DataFrame(data1, index = [0, 1, 2, 3])
df1 = pd.DataFrame(data2, index = [2, 3, 6, 7])
print(df, df1)
print(pd.concat([df, df1], axis = 1, join='inner'))
print(pd.concat([df, df1], axis = 1, sort = False))
print(pd.concat([df, df1], axis = 1, join_axes = [df.index]))
print(pd.concat([df, df1], ignore_index = True))

data1 = 
    {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
    'Age':[27, 24, 22, 32], 
    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
    'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data1,index = [0, 1, 2, 3])
s = pd.Series([1000, 2000, 3000, 4000], name='Salary')
print(df,s) 
print(pd.concat([df, s], axis = 1))

data1 = 
    {'key': ['K0', 'K1', 'K2', 'K3'],
    'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
    'Age':[27, 24, 22, 32],} 
data2 = 
    {'key': ['K0', 'K1', 'K2', 'K3'],
    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)
print(pd.merge(df, df1, on = 'key'))

data1 = {
    'key': ['K0', 'K1', 'K2', 'K3'],
    'key1': ['K0', 'K1', 'K0', 'K1'],
    'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
    'Age':[27, 24, 22, 32],}
data2 = {
    'key': ['K0', 'K1', 'K2', 'K3'],
    'key1': ['K0', 'K0', 'K0', 'K0'],
    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2) 
print(pd.merge(df, df1, on = ['key', 'key1']))
print(pd.merge(df, df1, how = 'left', on = ['key', 'key1']))
print(pd.merge(df, df1, how = 'right', on = ['key', 'key1']))
print(pd.merge(df, df1, how = 'outer', on = ['key', 'key1']))
print(pd.merge(df, df1, how = 'inner', on = ['key', 'key1']))

data1 = 
    {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
    'Age':[27, 24, 22, 32]}
data2 = 
    {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
    'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
df = pd.DataFrame(data1,index = ['K0', 'K1', 'K2', 'K3'])
df1 = pd.DataFrame(data2, index = ['K0', 'K2', 'K3', 'K4'])
print(df.join(df1))
print(df.join(df1, how = 'outer'))
df = pd.DataFrame(data1, index = pd.Index(['K0', 'K1', 'K2'], name='key'))

index = pd.MultiIndex.from_tuples([
    ('K0', 'Y0'), ('K1', 'Y1'),
    ('K2', 'Y2'), ('K2', 'Y3')],
    names=['key', 'Y'])
df1 = pd.DataFrame(data2, index = index)
print(df.join(df1, how='inner'))

data1 = 
    {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
    'Age':[27, 24, 22, 32],
    'Key':['K0', 'K1', 'K2', 'K3']} 
data2 = 
    {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
    'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
print(df.join(df1, on = 'Key'))

data =
    {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)
print(df.sort_values(by = 'Age'))
print(df.sort_values(by = 'Age',ascending = False))
print(df.sort_values(by = ['Age', 'Score']))
print(df.sort_values(by = 'Age', kind = 'mergesort'))
print(df.sort_values(by = 'Name', key = lambda col: col.str.lower()))

data =
    {"Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [28, 22, None, 22] }
df = pd.DataFrame(data)
print(df.sort_values(by = "Age", na_position = "first"))

df = pd.DataFrame(
    {'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana', 'Beans', 'Orange', 'Broccoli', 'Banana'],
    'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
    'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
    'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})
print(df.pivot_table(index = ['Product'], values = ['Amount'], aggfunc = 'sum'))
print(df.pivot_table(index=['Category'], values = ['Amount'], aggfunc = 'sum'))
print(df.pivot_table(index = ['Product', 'Category'], values = ['Amount'], aggfunc = 'sum')
print(df.pivot_table(index = ['Category'], values = ['Amount'], aggfunc = {'median', 'mean', 'min'}))
print(df.pivot_table(index = ['Product'], values = ['Amount'], aggfunc = {'median', 'mean', 'min'}))
date = ['1/1/2018', '2/1/2018', '3/1/2018', '4/1/2018']
Index = ['Day 1', 'Day 2', 'Day 3', 'Day 4']
sr = pd.Series(data = Date, index = Index)
print(sr, sr.index)
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s.index) 
s = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
s.index = ['a', 'b', 'c']
print(s)
s = pd.Series([10, 20, 30], index = pd.Index(['apples', 'oranges', 'bananas'], name = 'fruits'))
print(s.index.name)
data = np.array(['a', 'b', 'c', 'd', 'e'])
print(pd.Series(data))
print(pd.Series(data, index = [1000, 1001, 1002, 1003, 1004]))
data = {
    'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(data)
print(df.isnull(), df.notnull())
print(df.fillna(0))
print(df.fillna(method = 'pad'))
print(df.fillna(method = 'bfill')) 
import pandas as pd  

df = pd.DataFrame({
    "A": [12, 4, 5, None, 1], 
    "B": [None, 2, 54, 3, None], 
    "C": [20, 16, None, 3, 8], 
    "D": [14, 3, None, None, 6]
})  
print("\nOriginal DataFrame:\n", df)
print(df.interpolate(method = 'linear', limit_direction = 'forward'))
dic = {'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, np.nan, 45, 56],
    'Third Score': [52, 40, 80, 98],
    'Fourth Score': [np.nan, np.nan, np.nan, 65]}

df = pd.DataFrame(dic)
print(df.dropna())
print(df.dropna(how = 'all'))
print(df.dropna(axis = 1))
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 40],
    'City': ['NY', 'LA', 'SF', 'Chicago']
})
print(df.drop_duplicates())
print(df.drop_duplicates(subset = ['Name']))
print(df.drop_duplicates(keep = 'last')
print(df.drop_duplicates(keep = False))
print(df.drop_duplicates(inplace = True))
print(df.drop_duplicates(subset = ['A']))
print(df.duplicated().any())
df1 = pd.DataFrame({ 'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({ 'A': [4, 2, 3], 'B': ['d', 'b', 'c']})
print(pd.merge(df1, df2, how = 'outer').drop_duplicates())

data = 
    {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
    'Age': [25, 30, 22, 35, 28], 
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
    'Salary': [50000, 55000, 40000, 70000, 48000]}
df = pd.DataFrame(data)
df['Age'] = df['Age'].astype(float)
print(df.dtypes)
df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes)
df = df.astype({'Age': 'float64', 'Salary': 'str'})
print(df.dtypes)
frame = pd.DataFrame(
    {'FirstName': ['Vipul', 'Ashish', 'Milan'], 
    "Gender": ["", "", ""], 
    "Age": [0, 0, 0]}) 
frame['Department'] = np.nan 
print(frame) 
frame.dropna(how = 'all', axis = 1, inplace = True) 
print(frame)
nan_value = float("NaN") 
#frame.replace("", nan_value, inplace = True) 
frame.replace(0, nan_value, inplace=True) 
frame.dropna(how = 'all', axis = 1, inplace = True) 
print(frame)

df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek', 'Anand', np.nan, 'Pratap'])
print(df.astype('string'))
df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek', 'Anand', np.nan, 'Pratap'], dtype = 'string')
print(df)

df = pd.Series(['night_fury1', 'Is  ', 'Geeks, forgeeks', '100', np.nan, '  Contributor '])
print(df)
print(df.str.upper())
print(df.str.lower())
print(df.str.strip())
print(df.str.split(','))
print(df.str.split(',').str[0])
print(df.str.split(',').str.get(1))
print(len(df))
print(df.str.len())
print("\nafter using cat:")
print(df.str.cat(sep = '_'))
print(df.str.cat(sep='_', na_rep='#'))
print(df.str.get_dummies())
print(df.str.startswith('G'))
print(df.str.endswith('1'))
print(df.str.replace('Geeks', 'Gulshan'))
print(df.str.repeat(2))
print(df.str.count('n'))
print(df.str.find('n'))
print(df.str.findall('n'))
print(df.str.islower())
print(df.str.isupper()) 
print(df.str.isnumeric())
print(df.str.swapcase())

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

frame = pd.DataFrame( [['tom', 10], ['nick', '15'], ['juli', 14.8]], columns=['Name', 'Age'])
# frame[column] = frame[column].astype(int)
for column in frame.columns:
    print(column,':',pd.api.types.infer_dtype(frame[column]))
frame[column] = frame[column].apply(lambda x: pd.to_numeric(x, errors = 'ignore'))
for column in data_frame.columns:
    print(pd.api.types.infer_dtype(frame[column]))
print(frame.head())
print(frame.tail())
print(list(frame.columns))
print(frame.info())
print(frame.describe())
print(frame.isnull())
print(frame.isnull().sum())
frame = frame.dropna()
frame = frame.fillna(value)
frame[col] = frame[col].fillna(value)
frame.drop(4).head()
frame.rename({0:"First",1:"Second"})
frame['NewColumn'] = 1
print(frame.head())
frame.sort_values(by = 'Age', ascending = False).head()
frame.sort_values(by = ['Age','Annual Income (k$)']).head(10)
print(frame)
df1 = pd.DataFrame({
    'Name':['Jeevan', 'Raavan', 'Geeta', 'Bheem'],
    'Age':[25, 24, 52, 40], 
    'Qualification':['Msc', 'MA', 'MCA', 'Phd']})
df2 = pd.DataFrame({
    'Name':['Jeevan', 'Raavan', 'Geeta', 'Bheem'],
    'Salary':[100000, 50000, 20000, 40000]})
print(pd.merge(df1, df2))
register = pd.DataFrame()
register['Name'] = ['Abhijit','Smriti', 'Akash', 'Roshni']
register['Age'] = [20, 19, 20, 14]
register['Student'] = [False, True, True, False]
print(register)
person = pd.Series(['Mansi', 19, True], 
    index = ['Name', 'Age', 'Student'])
register.append(person, ignore_index = True)
print(register)
print(register.shape)
print(register.info())
print(register.corr())
print(register.describe())
students = register.drop('Age', axis = 1)
print(students.head())
students = students.drop(2, axis = 0)
print(students.head())

import pandas as pd 
df = pd.DataFrame([[9, 4, 8, 9], 
    [8, 10, 7, 6], [7, 6, 8, 5]], 
    columns=['Maths','English',   'Science', 'History']) 
print(df) 
print(df.sum())
print(df.describe())
df.agg(['sum', 'min', 'max'])
df.groupby(by = ['Maths'])
a = df.groupby('Maths') 
print(a.first())
b = df.groupby(['Maths', 'Science']) 
print(b.first())

import pandas as pd
a, b = pd.DataFrame()
dic = {'id' : [1, 2, 10, 12], 
    'val1': ['a', 'b', 'c', 'd']}
dec = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
x = pd.DataFrame(dic)
y = pd.DataFrame(dec)
print(x, y)
df = pd.merge(x, y, on = 'id', how = 'outer'); print(df)
df = pd.merge(x, y, left_index = True, right_index = True); print(df)
df ={
    "arr": [30, 70, 100],
    "ray": [65.1, 49.50, 30.7] }
data = pd.DataFrame(df)
print(data.corr())
df = pd.DataFrame({
    'A' : [1, 2, 3, 4, 5],
    'B' : [5, 6, 7, 8, 9],
    'C' : [9, 8, 7, 6, 5] })
print(df.corr())
