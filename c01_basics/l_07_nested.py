from pprint import pprint
from random import choice
from copy import deepcopy

from l_03_functions import create_devices

devices = create_devices(1,1)


device = {
    'name': 'r2Uj',
    'Operate System': 'Debian 9',
    'vendor': 'Vultr',
    'ip': '192.168.1.1',
    "interface": [

    ]
}

print("---------device without interface---------")
for key, value in device.items():
    print(f'{key:>16} : {value}')


interfaces = list()
for index in range(8):
    interface = {
        "name": "g/0/0/"+str(index),
        "speed": choice(["100", "200", "500", "1000"])
    }
    interfaces.append(interface)

device["interface"] = interfaces

print("---------device with interface---------")
for key, value in device.items():
    if key != "interface":
        print(f'{key:>16} : {value}')
    else:
        print(f'{key:>16} :')
        for interface in interfaces:
            print(f'\t\t\t\t\t{interface}')


print("---------device print interface with pprint---------")
pprint(device)


