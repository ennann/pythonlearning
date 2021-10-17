device_str = "    Bandwahost, Dmit  ,Oracle JP,  iOS   "


print("---------去头尾空格-----------")
device1 = device_str.strip()
print(device1)

print("---------拆分-----------")
device2 = device_str.split(",")
print(device2)

print("---------去头尾空格-----------")
device3 = device_str.strip().split(",")
print(device3)

print("--------------------")
device4 = device_str.replace(" ","").split(",")
print(device4)

device5 = list()
for item in device_str.split(","):
    device5.append(item.strip())
print(device5)

device6 =[item.strip() for item in device_str.split(",")]
print(device6)



vendor_info = device_str.split(",")
for p, vendor_info_part in enumerate(vendor_info):
    print(f"vendor part {p}: {vendor_info_part.strip()}")
print()