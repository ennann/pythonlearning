from l_03_functions import create_devices
from pprint import pprint
from random import randint
from random import uniform
from datetime import datetime
from copy import copy
from copy import deepcopy
# copy 用来完全拷贝一个字典



devices = create_devices(12,5)

print(devices)
print("\n   Name        Vendor : OS             IP Addr ")
print("  ------  -----------   ---------     -------------- ")
for device in devices:
    print(
        f'{device["name"]:>8}   {device["vendor"]:>10}   {device["Operate System"]:<9}    {device["ip"]:>12}'
    )


# 检查相同用户名的机器
print("----------START CHECK SAME NAME----------")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(f'Found Name Matched! {device_b["name"]} FOR both {device_a["ip"]} and {device_b["ip"]}')
print("-----------------------------------------")


device2 = copy(devices)
device2[0]["name"] = "This is a dumb device name."
if device2 == devices:
    print("Shallow copy: devices2 STILL equals to devices.")
else:
    print("     ?Huh!")

device3 = deepcopy(devices)
device3[0]["name"] = "This is a dumb device name."
if device3 != devices:
    print("Deep copy: devices3 not equals to devices.")
else:
    print("     ?Huh!")

print("-----------------------START TEST------------------")
SLA_AVIBILITY = 90
SLA_RESPONSE_TIME = 1.0

for device in  devices:

    device["avilibility"] = randint(80,100)
    device["response_time"] = uniform(0.5, 1.1)

    if device["avilibility"] > SLA_AVIBILITY:
        print(f'{datetime.utcnow()}: {device["name"]:6}  - Avilibility {device["avilibility"]} > {SLA_AVIBILITY}')
    if device["response_time"] > SLA_RESPONSE_TIME:
        print(f'{datetime.utcnow()}: {device["name"]:6}  - Response_time {device["response_time"]} > {SLA_RESPONSE_TIME}')

    