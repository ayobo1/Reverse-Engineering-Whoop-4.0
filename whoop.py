import struct
from datetime import datetime, timezone
import crcCalc

def set_time(year, month, day, hour, minute):
    theTime = datetime(year, month, day, hour, minute, tzinfo=timezone.utc)
    unixTime = int(theTime.timestamp())
    timestamp = struct.pack("<I", unixTime)  # little-endian uint32

    header = bytes.fromhex("aa10005723")
    packetCount = bytes.fromhex("00")
    deviceNum = bytes.fromhex("4201")
    blank4 = bytes.fromhex("00000000")

    payload = header + packetCount + deviceNum + timestamp + blank4 
    crc = crcCalc.get_crc(payload)
    return payload + crc


data1 = bytes.fromhex("aa10005723704201696d657400000000")   #test for 
data2 = set_time(2025, 1, 1, 12, 0)
data1c = crcCalc.get_crc(data1)

print(data1c.hex())
print(data2.hex())


theTime = datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc)
unixTime = int(theTime.timestamp())
timestamp = struct.pack("<I", unixTime)
print(timestamp.hex())




# print("data 1 is: ", data1)
# print("data 2 is: ", data2)
# PacketCRC1 = crcCalc.get_crc(data1)
# PacketCRC2 = crcCalc.get_crc(data2)
# print("crc is:", PacketCRC1.hex())
# print("crc2 is:", PacketCRC2.hex())

# async def main(address):
#     header = bytes.from