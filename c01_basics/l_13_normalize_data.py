from ipaddress import IPv4Address


print("\nNormalization tests\n")



ip_addr_1 = "10.0.1.1"
ip_addr_2 = "10.000.001.001"
ip_addr_3 = "010.00.01.001"

print(IPv4Address(ip_addr_1))
print(IPv4Address(ip_addr_2))
print(IPv4Address(ip_addr_3))


# if IPv4Address(ip_addr_1) == IPv4Address(ip_addr_2) == IPv4Address(ip_addr_3):
#     print("--IP address normalization works")
# else:
#     print("--IP address normalization failed")