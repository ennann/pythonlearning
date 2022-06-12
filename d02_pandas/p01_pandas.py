import numpy as np
import pandas as pd

obj = pd.Series([4, 7.0, -5, 3])
print(obj)

print(obj.values)

obj2 = pd.Series([4, 7.0, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj.index, obj2.index, sep='\n')

# You can use the index to access the values, and the index can be a range.
print(obj2['a'])
print(obj2['d'])
print()
print(obj2['d':'a'])

# You can use a condition to select a subset of the data.
print(obj2[obj2 > 0])
print()
print(obj2[obj2 % 2 == 0])

# You can transform the data using a Series function from a dict to series.
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
print(sdata)
obj3 = pd.Series(sdata)
print(obj3)
# You can even use a dict to create a series.

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print()
# You can use the index to access the values, and the index can be a range.

print(pd.isnull(obj4))
print(pd.notnull(obj4))
print()
print(obj3 + obj4)
print()

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
print()

# DataFrames

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = pd.DataFrame(data)
print(frame)
## Automatically generate the index


print(frame.head(3))
## Only show the first 3 rows.

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
## Specify the columns and index.

print(pd.DataFrame(frame2, columns=['year', 'state', 'pop']).head(3))
## You can define the columns.

print(
    pd.DataFrame(frame2, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five']).head(
        3))
## You can define the columns and the index at the same time.

print(frame2.columns)
##

print()
print(frame2['state'])
print(frame2['year'])
print(frame2.year)
## You can access the columns by name.

print()
print(frame2.loc['three'])

frame2['debt'] = 16.5
print(frame2)
## You can add a new column.

print()
frame2['debt'] = np.arange(5.00)
print(frame2)

print()
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

del frame2['eastern']
print(frame2)
print()
## You can delete a column.


pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
       }
frame3 = pd.DataFrame(pop)
print(frame3)

print(frame3.T)
print()
## You can transpose the data.


pdate = {'Ohio': frame3['Ohio'][0:-1],
         'Nevada': frame3['Nevada'][0:2]}

print(pdate)
print()
print(pd.DataFrame(pdate))

frame3.index.name = 'YEAR ↓'
frame3.columns.name = 'STATE →'
print()
print(frame3)
## You can define the name of index.


print(frame3.values)
## You can get the values of the dataframe.


print(frame3.columns)
## You can get the columns of the dataframe.


"""
Basic functions
"""

obj = pd.Series([4, 7.0, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
print()
## You can reindex the data.

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))

print()
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
print(frame3)
## You can reindex the data.

print('This is a test.')
frame4 = frame.loc[['a', 'b', 'c', 'd'], states]
print(frame4)
