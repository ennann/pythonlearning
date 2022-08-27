# 批量生成折线图

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc("font", family='OPPOSans')


# 读取 csv 函数
def read_csv(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(',') for line in lines]
        return lines


csv_data = read_csv('/Users/Elton/Downloads/data/data.csv')

x_plot = csv_data[0][1:]

for i in range(1, len(csv_data)):
    y_plot = [int(y) for y in csv_data[i][1:]]
    for i in range(len(y_plot)):
        if y_plot[i] == 0:
            y_plot[i] = np.nan

    y_max = max([x for x in y_plot if np.isnan(x) == False])
    y_min = min([x for x in y_plot if np.isnan(x) == False])
    print(y_plot, y_max, y_min)
    # continue

    # 生成图像
    plt.figure(figsize=(10, 6), dpi=200)
    plt.plot(x_plot, y_plot, color='blue', linewidth=2.0, linestyle='--', marker='o', markerfacecolor='red',
             markersize=8)
    plt.ylabel('排名变化', fontsize=15)
    # 设置坐标字体大小
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # 设置坐标轴范围
    plt.ylim(y_max + y_max * 0.1, y_min - y_min * 0.1)

    # 设置数据标签
    # for a, b in zip(x_plot, y_plot):
    #     if b == np.nan:
    #         continue
    #     plt.text(a, b - min(y_plot)*0.06, '%.0f' % b, va='top', ha='center',  fontsize=10, bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', edgecolor='k',lw=1 ,alpha=0.5))

    plt.title(csv_data[i][0], fontsize=22)
    plt.savefig('/Users/Elton/Downloads/data/' + str(i) + ' ' + csv_data[i][0] + '.png')
    plt.close()
