import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.rc("font", family='OPPOSans')


# 读取 csv 函数
def read_csv(filename):
    """
    :param filename:
    :return: a list of lists that contains each line in the csv file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(',') for line in lines]
        return lines


csv_data = read_csv('/Users/Elton/Downloads/data/data.csv')

x_plot = csv_data[0][1:]

for i in range(1, len(csv_data)):
    name = csv_data[i][0]
    header = csv_data[0][1:]
    data = csv_data[i][1:]
    data = [float(d) for d in data]
    df = pd.DataFrame({'时间': header, '成绩': data})
    df.loc[df['成绩'] == 0, '成绩'] = np.nan  # 替换 0 值 为 NaN

    plt.figure(figsize=(10, 6), dpi=200)
    plt.plot(df['时间'], df['成绩'], color=(0.41, 0.74, 0.97), linewidth=2.0, linestyle='--', marker='o',
             markerfacecolor=(0.49, 0.89, 0.60), markersize=8)

    plt.ylabel('排名变化', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    y_max = max([ele for ele in df['成绩'] if np.isnan(ele) == False])
    y_min = min([ele for ele in df['成绩'] if np.isnan(ele) == False])

    # 设置坐标轴范围
    plt.ylim(y_max + 15, y_min - 20)

    # 设置数据标签
    for a, b in zip(df['时间'], df['成绩']):
        if b == np.nan: continue  # 跳过 NaN 值
        plt.text(a, b - (y_max - y_min) * 0.1, '%.0f' % b, va='bottom', ha='center', fontsize=10,
                 bbox=dict(boxstyle='round,pad=0.5', facecolor=(0.98, 0.83, 0.52), edgecolor='k', lw=1, alpha=0.5))

    plt.title(csv_data[i][0], fontsize=22)
    plt.savefig('/Users/Elton/Downloads/data/' + str(i) + ' ' + csv_data[i][0] + '.png')
    plt.close()
