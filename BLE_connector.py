# This uses bleak as a gatt server to connect to the Whoop device.
# the device number must be changed if you would like to use it.
# my whoop's address is DC:AC:08:7B:BC:4F for example. use the following to search for your whoop's address:.

# import asyncio
# from bleak import BleakScanner

# async def main():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)

# asyncio.run(main())

# $ python BLE_connector.py
# 57:3F:2A:A0:DE:B6: None
# DC:AC:08:7B:BC:4F: Ayoob Whoop
# 28:9E:8E:62:D9:DC: None
# 46:DF:51:B7:DB:52: None
# 61:DB:93:AC:E9:95: None
# C4:A2:50:31:D4:F7: None
# DC:2A:7D:ED:E0:15: None
#note that I named my whoop "Ayoob Whoop." if you did not name yours, look in the whoop app.
#so the whoop's address is as :  DC:AC:08:7B:BC:4F

# using bleak again, we can get all the UUID's for the services/everything you would need
# import asyncio
# from bleak import BleakClient

# ADDRESS = "DC:AC:08:7B:BC:4F"

# async def main():
#     async with BleakClient(ADDRESS) as client:
#         print("Connected:", client.is_connected) #should return true

#         for service in client.services:
#             print(f"Service UUID: {service.uuid}")
#             for char in service.characteristics:
#                 print(f"  Characteristic UUID: {char.uuid}")
#                 print(f"    Properties: {char.properties}")

# asyncio.run(main())

# output: 
# $ python BLE_connector.py
# Connected: True
# Service UUID: 00001800-0000-1000-8000-00805f9b34fb
#   Characteristic UUID: 00002a00-0000-1000-8000-00805f9b34fb
#     Properties: ['write', 'read']
#   Characteristic UUID: 00002a01-0000-1000-8000-00805f9b34fb
#     Properties: ['read']
#   Characteristic UUID: 00002a04-0000-1000-8000-00805f9b34fb
#     Properties: ['read']
#   Characteristic UUID: 00002aa6-0000-1000-8000-00805f9b34fb
#     Properties: ['read']
# Service UUID: 00001801-0000-1000-8000-00805f9b34fb
#   Characteristic UUID: 00002a05-0000-1000-8000-00805f9b34fb
#     Properties: ['indicate']
# Service UUID: 61080001-8d6d-82b8-614a-1c8cb0f8dcc6
#   Characteristic UUID: 61080002-8d6d-82b8-614a-1c8cb0f8dcc6       This is likely the write UUID for 
#     Properties: ['write', 'write-without-response']
#   Characteristic UUID: 61080003-8d6d-82b8-614a-1c8cb0f8dcc6
#     Properties: ['notify']
#   Characteristic UUID: 61080004-8d6d-82b8-614a-1c8cb0f8dcc6
#     Properties: ['notify']
#   Characteristic UUID: 61080005-8d6d-82b8-614a-1c8cb0f8dcc6
#     Properties: ['notify']
#   Characteristic UUID: 61080007-8d6d-82b8-614a-1c8cb0f8dcc6
#     Properties: ['notify']
# Service UUID: 0000180d-0000-1000-8000-00805f9b34fb
#   Characteristic UUID: 00002a37-0000-1000-8000-00805f9b34fb
#     Properties: ['notify']
# Service UUID: 0000180a-0000-1000-8000-00805f9b34fb
#   Characteristic UUID: 00002a29-0000-1000-8000-00805f9b34fb
#     Properties: ['read']
# Service UUID: 0000180f-0000-1000-8000-00805f9b34fb
#   Characteristic UUID: 00002a19-0000-1000-8000-00805f9b34fb
#     Properties: ['read', 'notify']

#the UUID for setting the alarm would most likely be the write pointed to above
# UUID: 61080002-8d6d-82b8-614a-1c8cb0f8dcc6
# ADDRESS: DC:AC:08:7B:BC:4F
