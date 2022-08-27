import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc("font", family='OPPOSans')

x_plot = [1, 2, 3, 4, 5, 6]
y_plot = [5, np.nan, 3, 4, 1, 7]
for i in range(len(y_plot)):
    if np.isnan(i):
        continue
    print(y_plot[i])
newlist = [x for x in y_plot if np.isnan(x) == False]
print(newlist, max([x for x in y_plot if np.isnan(x) == False]), min([x for x in y_plot if np.isnan(x) == False]))

print(max(y_plot), min(y_plot))

# 生成图像
plt.figure(figsize=(10, 6), dpi=200)
plt.plot(x_plot, y_plot, color='blue', linewidth=2.0, linestyle='--', marker='o', markerfacecolor='red', markersize=8)

# 设置坐标字体大小
plt.ylabel('排名变化', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# # # 设置数据标签
# for a, b in zip(x_plot, y_plot):
#     if b == np.nan: continue
#     plt.text(a, b - 1, '%.0f' % b, va='top', ha='center', fontsize=10,
#              bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', edgecolor='k', lw=1, alpha=0.5))

plt.title("name", fontsize=22)
plt.savefig('/Users/Elton/Downloads/data/' + "wss" + '.png')
plt.close()
