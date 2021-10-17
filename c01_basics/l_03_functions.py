from random import choice
import string
from pprint import pprint
from tabulate import tabulate

# 创建函数的时候可以默认制定默认值
#
def create_devices(num_devices=1, num_subnets=1):

    # 创建一个设备list
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Too god dame devices and/or subnets.")
        return create_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            # CREATE EMPTY DICS
            device = dict()

            device["name"] = (
                    choice(["r1", "r2", "r5", "r4", "u0"])
                    + choice(["U", "S"])
                    + choice(string.ascii_lowercase)
            )

            # 供应商
            device["vendor"] = choice(["Bandwahost", "Dmit", "Vultr", "iOS"])

            # 设备系统
            if device["vendor"] == "Bandwahost":
                device["Operate System"] = choice(["CentOS 6", "CentOS 7", "CentOS 8"])
            elif device["vendor"] == "Dmit":
                device["Operate System"] = choice(["Ubuntu 18", "Ubuntu 19", "Ubuntu 20"])
            elif device["vendor"] == "Vultr":
                device["Operate System"] = choice(["Debian 8", "Debian 9"])
            elif device["vendor"] == "iOS":
                device["Operate System"] = choice(["14.1", "15.0"])

            # 设备IP地址
            device["ip"] = "192.168." + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)

    return created_devices



# ---------------------主程序------------------
# if __name__ == '__main__':
#     devices,s = create_devices(num_devices=4)
#     print()
#     print(tabulate(devices, headers="keys"))
#     print(s)
#
#
# pprint(type(create_devices(5)))