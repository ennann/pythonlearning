import string
from random import choice
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint


devices = list()

for index in range(1, 8):

    device = dict()

    # 设备名称
    device["name"] = (
        choice(["r1", "r2", "r5", "r4", "u0"])
        + choice(["U", "S"])
        + choice(string.ascii_lowercase)
    )

    # 设备厂商
    device["vendor"] = choice(["Bandwahost", "Dmit", "Vultr", "iOS"])

    # 设备系统
    if device["vendor"] == "Bandwahost":
        device["Operate System"] = choice(["CentOS 6", "CentOS 7", "CentOS 8"])
    elif device["vendor"] == "Dmit":
        device["Operate System"] = choice(["Ubuntu 18","Ubuntu 19", "Ubuntu 20"])
    elif device["vendor"] == "Vultr":
        device["Operate System"] = choice(["Debian 8", "Debian 9"])
    elif device["vendor"] == "iOS":
        device["Operate System"] = choice(["14.1", "15.0"])

    # 设备IP地址
    device["ip"] = "192.168.1." + str(index)

    devices.append(device)

# for key, value in device.items():
#     print(f"{key:>20s} : {value}")

# print("-------------------------------pprint------------------------------")
pprint(devices)

# print("-------------------------------输出表格------------------------------")
# print(tabulate(sorted(devices, key=itemgetter("vendor", "Operate System", "ip")), headers="keys"))


print("-------------------------------输出表格------------------------------")
sorted_decives = sorted(devices, key=itemgetter("ip", "Operate System"))
print(tabulate(sorted_decives, headers="keys"))