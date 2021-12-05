import pandas as pd
from pandas import ExcelWriter


# Read file and print to double check.
print('*'*20+'Print original table.'+'*'*20)
df = pd.read_excel(r"/Users/Elton/Downloads/服务台回收设备擦除记录11.26.xlsx", sheet_name="详情")

# Export pivot table.
print('*'*20+'Export pivot content.'+'*'*20)
pivot_1 = pd.pivot_table(df, index=[ "工区"], values=["是否两小时", "是否擦除", "是否需要统计"],
                         aggfunc="sum", margins=True).reset_index()

# Export group.
print('*'*20+'Export group content.'+'*'*20)
data_group = df.groupby(["备注"]).count()

# Write to Results file.
with ExcelWriter('/Users/Elton/Downloads/Results.xlsx') as writer:
    pivot_1.to_excel(writer, sheet_name="Sheet1")
    data_group.to_excel(writer, sheet_name="Sheet2")


print('*'*20+'File saved.'+'*'*20)

"""
Notes:



# data_group.to_excel('/Users/Elton/Downloads/Results.xlsx',sheet_name="Sheet2")
# pivot_2.to_excel('/Users/Elton/Downloads/Results.xlsx',sheet_name="Sheet2")
"""