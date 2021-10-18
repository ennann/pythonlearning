from random import choice, randint
import string
from pprint import pprint


def create_device(device_index=1, subnet_index=1, random_ip=False):
    device = dict()

    # RANDOM DEVICE NAME
    device["name"] = (
            choice(["r1", "r2", "r5", "r4", "u0"])
            + choice(["U", "S"])
            + choice(string.ascii_lowercase)
    )

    # 供应商
    device["vendor"] = choice(["Bandwahost", "Dmit", "Vultr", "iOS"])

    # 设备系统
    if device["vendor"] == "Bandwahost":
        device["OperateSystem"] = choice(["CentOS 6", "CentOS 7", "CentOS 8"])
    elif device["vendor"] == "Dmit":
        device["OperateSystem"] = choice(["Ubuntu 18", "Ubuntu 19", "Ubuntu 20"])
    elif device["vendor"] == "Vultr":
        device["OperateSystem"] = choice(["Debian 8", "Debian 9"])
    elif device["vendor"] == "iOS":
        device["OperateSystem"] = choice(["14.1", "15.0"])

    # 设备IP地址
    # device["ip"] = "192.168." + str(subnet_index) + "." + str(device_index)
    if random_ip:
        device["ip"] = "192.168." + str(subnet_index) + "." + str(device_index)
    else:
        device["ip"] = "192.168." + str(subnet_index) + "." + str(device_index)
    return device



def create_devices(num_devices=1, num_subnets=1):

    # 创建一个设备list
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Too god dame devices and/or subnets.")
        return create_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            device = create_device(device_index, subnet_index)
            # # CREATE EMPTY DICS
            # device = dict()
            #
            # # device = create_device()
            #
            # device["name"] = (
            #         choice(["r1", "r2", "r5", "r4", "u0"])
            #         + choice(["U", "S"])
            #         + choice(string.ascii_lowercase)
            # )
            #
            # # 供应商
            # device["vendor"] = choice(["Bandwahost", "Dmit", "Vultr", "iOS"])
            #
            # # 设备系统
            # if device["vendor"] == "Bandwahost":
            #     device["OperateSystem"] = choice(["CentOS 6", "CentOS 7", "CentOS 8"])
            # elif device["vendor"] == "Dmit":
            #     device["OperateSystem"] = choice(["Ubuntu 18", "Ubuntu 19", "Ubuntu 20"])
            # elif device["vendor"] == "Vultr":
            #     device["OperateSystem"] = choice(["Debian 8", "Debian 9"])
            # elif device["vendor"] == "iOS":
            #     device["OperateSystem"] = choice(["14.1", "15.0"])
            #
            # # 设备IP地址
            # device["ip"] = "192.168." + str(subnet_index) + "." + str(device_index)
            created_devices.append(device)

    return created_devices



def create_network(num_devices=1, unm_subnets=1):

    devices = create_devices(num_devices, unm_subnets)


    network = dict()
    network["subnets"] = dict()

    for device in devices:
        subnet_address_bytes = device["ip"].split(".")
        subnet_address_bytes[3] = "0"   # 检查最后一个IP地址
        subnet_address = ".".join(subnet_address_bytes)  # 聚合IP地址

        if subnet_address not in network["subnets"]:

            network["subnets"][subnet_address] = dict()
            network["subnets"][subnet_address]["devices"] = list()

        network["subnets"][subnet_address]["devices"].append(device)
    interfaces = list()
    for index in range(0, choice([2, 4, 6])):
        interface = {
            "name": "g/0/0/"+str(index),
            "speed": choice(["100", "200", "500", "1000"])
        }
        interfaces.append(interface)
    device["interfaces"] = interfaces

    return network


def create_devices_gen(num_devices=1, num_subnets=1):

    # 判断输入数字是否超过子网限制
    if num_devices > 254 or num_subnets > 254:
        print("Too god dame devices and/or subnets.")
        return create_devices

    print("Start decide generating... ...")
    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):
            device = create_devices(num_devices, num_subnets)
            yield device
