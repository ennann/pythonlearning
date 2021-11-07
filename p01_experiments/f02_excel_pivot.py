import numpy as np
import pandas as pd
import csv

# read file and test.
print('-'*10+'打印原始表格'+'-'*10)
df = pd.read_excel(r"/Users/Elton/Downloads/Book1.xlsx")
print(df)
# print(df.shape)

# 查看维修与分类的数量多少
# print(df.groupby('工单类型').count())
# data_group = df.groupby(["工单类型", "工区"]).count()
# groupby 函数还挺好用的，直接把两种类型的表格做到了计数


# f = open("groupby.csv", mode="a")
# csvwriter = csv.writer(f)
# csvwriter.writerow(data_group)


# 第一次数据透视
print('-'*10+'打印透视图表格'+'-'*10)
pivot_1 = pd.pivot_table(df, index=["工单类型", "工区"], values=[u"是否需要统计", u"是否两小时"], aggfunc="count", margins=True).reset_index()
pivot_1.to_csv("groupby.csv")
