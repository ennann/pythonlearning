device_info_str = "name:r3-L-n7, vendor:cisco, model:catalyst 2960, os:ios, version:12.1(T)"

# LIST THEN DICT COMPREHENSION FROM STRING
device_info_pairs = [kv_pair.split(":") for kv_pair in device_info_str.split(",")]
device = {item[0].strip(): item[1].strip() for item in device_info_pairs}
print("\ndevice using list and dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

print("device nicely formatted:")
device2 = {item[0].strip(): item[1].strip() for item in device_info_pairs for kv_pair in device_info_str.split(",")}
for key, value in device2.items():
    print(f"{key:>16s} : {value}")