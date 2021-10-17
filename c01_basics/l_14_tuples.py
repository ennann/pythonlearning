# tuples 学习
# tuples 是不可以像 list 一样添加信息的，是一个inmutable
# tuple 也是一个内置函数，将其他list转换为tuple
# index 是从 0 开始的，like t[1] 其实是第二个value
# id函数，返回值
from util import functions
from pprint import pprint
from collections import namedtuple


if __name__ == "__main__":

    device = tuple(functions.create_device(4,1))
    pprint(device)

    print("\n--------------Tuple of device:-----------")
    device = ("r2Ub", "Bandwahost", "Ubuntu 20", "20.12")

    print("          name:", device[0])
    print("        vendor:", device[1])
    print("Operate System:", device[2])
    print("            ip:", device[3])


    print("\n--------------device ad named tuple-----------")
    Device = namedtuple('Device', ['name', 'vendor', 'OperateSystem', 'ip'])
    device = Device("r2Ub", "Bandwahost", "Ubuntu 20", "20.12")

    print("          name:", device.name)
    print("        vendor:", device.vendor)
    print("OperateSystem:", device.OperateSystem)
    print("            ip:", device.ip)

    print("\n--------------device as named tuple-----------")
    device_as_tuples = list()
    devices = functions.create_devices(1,4)
    for device in devices:
        Device = namedtuple("Device", device.keys())
        device_as_tuples.append(Device(**device))

    pprint(device_as_tuples)
# print(type(device.keys()))