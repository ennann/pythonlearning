import numpy as np
import pandas as pd

#  Seriers
print("-"*20+"Begin Pandas"+"-"*20)
S1 = pd.Series(["a","b","c",'d','e','f','g'])
print(S1)

print("-"*10+"Pandas' Series with index"+"-"*10)

# Series with index
S2 = pd.Series(["a","b","c",'d','e','f','g'], index=[1,2,3,4,5,6,7])
print(S2)

# Create a random two dimension table.
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

# read data from xlsx file
p_data = pd.read_excel(r"/Users/Elton/Downloads/记录11.04.xlsx")
print(p_data)