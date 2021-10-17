from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from enum import Enum


# Constant:

# Class 的初见，算是更方便了吧，可以让代码更加可视化。
class Vendor:
    BANDWAHOST = "Bandwahost"
    DMIT = "Dmit"
    VULTR = "Vultr"
    IOS = "iOS"


# Class 的Enum穷举，可以让变量从固定值中进行选择，这样的话可以避免很多不必要的麻烦。
class Vendor(Enum):
    BANDWAHOST = "Bandwahost"
    DMIT = "Dmit"
    VULTR = "Vultr"
    IOS = "iOS"
    TEST = 1.0

devices = list()

for index in range(10):

    device = dict()

    device["name"] = (
            choice(["r1", "r2", "r5", "r4", "u0"])
            + choice(["U", "S"])
            + choice(string.ascii_lowercase)
    )

    # device["vendor"] = choice(["Bandwahost", "Dmit", "Vultr", "iOS"])

    device["vendor"] = choice([Vendor.BANDWAHOST, Vendor.DMIT, Vendor.VULTR, Vendor.IOS])

    if device["vendor"] == Vendor.BANDWAHOST:
        device["os"] = choice(["CentOS 6", "CentOS 7", "CentOS 8"])
        device["ip"] = ""
    elif device["vendor"] == Vendor.DMIT:
        device["os"] = choice(["Ubuntu 18", "Ubuntu 19", "Ubuntu 20"])
    elif device["vendor"] == Vendor.VULTR:
        device["os"] = choice(["Debian 8", "Debian 9"])
    elif device["vendor"] == Vendor.IOS:
        device["os"] = choice(["14.1", "15.0", "15.7"])


    devices.append(device)


# sorted_decives = sorted(devices, key=itemgetter("vendor"))
# print(tabulate(sorted_decives, headers="keys"))

print(type(Vendor.TEST.value))