from netmiko import Netmiko




def netmiko_connect(device_type):

    print(
        f"\n\nConnecting to {cisco_sandbox_devices[device_type]['hostname']}:{cisco_sandbox_devices[device_type]['port']}"
    )
    print("... this may take a little while.")

    connection = Netmiko(
        cisco_sandbox_devices[device_type]["hostname"],
        port=cisco_sandbox_devices[device_type]["port"],
        username=cisco_sandbox_devices[device_type]["username"],
        password=cisco_sandbox_devices[device_type]["password"],
        device_type=cisco_sandbox_devices[device_type]["device_type"],
    )

    return connection


def disconnect(connection):
    connection.disconnect()
