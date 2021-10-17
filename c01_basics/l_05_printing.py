from l_03_functions import create_devices
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from time import sleep
from datetime import datetime
from random import choice
import nmap


devices = create_devices(12)

print("-----------------先看一下生成的设备---------------")
# pprint(devices)

print("-----------------Loop循环看看---------------")

# for device in devices:
#     sleep(0.1)
#     device["time"] = str(datetime.now())
#     print(device)



# 第一个写的端口检测程序
nm = nmap.PortScanner()

while True:
    # ip = input("\nInput ip:")
    ip = "dmit.650056.xyz"
    print(f"\n------begining scan of {ip}")
    output = nm.scan(ip,"443")
    print(f"-----command: {nm.command_line()}")

    print("--------nmap scan output------------")
    pprint(output)
