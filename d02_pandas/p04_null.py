import numpy as np
import pandas as pd
from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])
print(data)

print(data.dropna())
# Series and DataFrame
# 1 dimension: Series
# 2 demension: DataFrame


data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
cleaned = data.dropna()
# will delete all the rows with NA
print(cleaned)

print(data.dropna(how='all'))
# onle delete the rows with all NA

data[4] = NA
print(data)
# print(data.dropna(axis=1))
print(data.dropna(axis=1, how='all'))
# delete the columns with all NA


df = pd.DataFrame(np.random.randn(7, 3))
print(df)
df.iloc[:4, 1] = NA  # set the second column (only the top four) to NA
df.iloc[:2, 2] = NA  # set the third column (only the top two) to NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))

print(df.fillna(999))

print(df.fillna({1: 0.9, 2: 99}))
# fill the NA with the mean of the column
