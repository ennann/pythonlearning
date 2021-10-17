from util import functions
from tabulate import tabulate
import time


# dicts is more efficienty that lists.


# -------------Main program-------------
if __name__ =="__main__":

    devices = functions.create_devices(num_devices=254, num_subnets=254)

    devices_dict = dict()
    for device in devices:
        devices_dict[device["ip"]] = device

    print("calculating tabular output devices...")
    print("\n", tabulate(devices, headers="keys"))

    while True:

        ip_to_find = input("\nInput the IP you want find: ")
        if not ip_to_find:
            break

        start = time.time()
        for device in devices:
            if device["ip"] == ip_to_find:
                print(f"--- --->found it (list): {device}")
                list_search_time = (time.time() - start) * 1000
                print(f"--- --->in {list_search_time} msec")
                print(f"--- --->id of device", id(device))
                break
        else:
            print("---! IP not found, please try again.")
            continue


        start = time.time()
        if ip_to_find in devices_dict:
            print(f"--- --->found it (dict): {device}")
            dict_search_time = (time.time() - start) * 1000
            print(f"--- --->in {dict_search_time} msec")
            print(f"--- --->id of device", id(devices_dict[ip_to_find]))




        print(f"dict search is {int(list_search_time/dict_search_time)} time faster than list.")