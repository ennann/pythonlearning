from util import functions
from pprint import pprint

device = functions.create_device()

print(device)

devices = functions.create_devices(1,4)
# pprint(devices)


print(device.keys())
print(device.values())
print(type(device.keys()))
print(type(device.values()))

pprint(devices)