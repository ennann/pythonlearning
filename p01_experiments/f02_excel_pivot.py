import pandas as pd
from pandas import ExcelWriter


# Read file and print to double check.
print('-'*10+'Check the original table content'+'-'*10)
df = pd.read_excel(r"/Users/Elton/Downloads/服务台回收设备擦除记录11.11.xlsx", sheet_name="详情")
print(df)

# Export pivot table.
print('-'*10+'Export pivot content.'+'-'*10)
pivot_1 = pd.pivot_table(df, index=["工单类型", "工区"], values=["是否两小时", "是否擦除", "是否需要统计"], aggfunc="sum", margins=True).reset_index()

# Export group.
data_group = df.groupby(["备注",]).count()
print(data_group)


# Write to Results file.
with ExcelWriter('/Users/Elton/Downloads/Results.xlsx') as writer:
    pivot_1.to_excel(writer, sheet_name="Sheet1")
    data_group.to_excel(writer, sheet_name="Sheet2")


print('-'*10+'保存完成'+'-'*10)

# Notes
#
#
# data_group.to_excel('/Users/Elton/Downloads/Results.xlsx',sheet_name="Sheet2")
# pivot_2.to_excel('/Users/Elton/Downloads/Results.xlsx',sheet_name="Sheet2")