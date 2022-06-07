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
