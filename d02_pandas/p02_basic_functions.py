import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
# print(frame)

states = ['Texas', 'Utah', 'California']
# print(frame.reindex(columns=states))

# print(frame.loc[['a', 'b', 'c', 'd'], states])
# KeyError: "['b'] not in index"


obj = pd.DataFrame(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)

new_obj = obj.drop(['c'])
# print(new_obj)
# print()

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
# print(data)


# print(data.drop(['Ohio', 'Utah']))
# print(data.drop(['two'], axis=1))
# print(data.drop(['two', 'four'], axis='columns'))
print(data)
# print(obj.drop('c', inplace=True))

# print(data.loc['Colorado'], ['one', 'two'])
print(data.loc['Colorado', ['one', 'two']])
print(data.iloc[2, [3, 0, 1]])
## You can use loc and iloc to get the data.


s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4.5], index=['a', 'c', 'e', 'f'])
print(s1 + s2)
## You can use + to add two series, and when some data are missing, it will use NaN. Just like outer join.


df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1 + df2)
## You can use + to add two dataframes, and when some data are missing, it will use NaN. Just like outer join.
## When some columns have data in one dataframe, but not in the other, it will use NaN.


df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1, df2, sep='\n')
df2.loc[1, 'b'] = np.nan  # modify some data to NaN.

print(df2)
print(df1 + df2)
## When you add two dataframe, if they don't have the same columns, it will use NaN.
## But sometimes you want to replace the NaN with specific value.

print()
print(df1.add(df2, fill_value=0))
## It means that you replace the NaN with 0 in the df2.


arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr - arr[0])
## When a dataframe substract a series, it will use the value of the series.
## 广播机制，这是对行进行广播。

print()
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)
print(frame - series)

series2 = frame['d']
print(frame.sub(series2, axis='index'))

frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 0, 4]})
# print(frame)
# print(frame.rank(axis='columns'))


df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])

# print(df.sum())
# print(df.sum(axis='index'))
# print(df.sum(axis=0))
# print(df.sum(axis='columns'))
# print(df.sum(axis=1))
# print(df.sum(axis=1, skipna=False))
# print()
# print(df)
# print(df.cumsum())
# print(df.describe())


import pandas_datareader.data as web

all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
print("Test the yahoo")
print(price)
print(volume.head())

returns = price.pct_change()
print(returns.tail())

print(returns.MSFT.corr(returns.IBM))
print(returns.corr())
