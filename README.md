# Reverse-Engineering-Whoop-4.0
Whoop is a fitness band that you must have a subscription to use. I want to change that so that you can still utalize it without the subscription.

Whoop timer data------
Header       packet count   device #     Unix time stamp in hex little endian (ALL EST)   checksum ☹
aa10005723   1c             4201         004a2f68                                         00000000edfb6182      #  12:00 PM
aa10005723   1b             4201         a0f52e68                                         000000000ee5761c     #  6:00 AM
aa10005723   1a             4201         349d2f68                                         00000000e2513705     #  5:55 PM
aa10005723   19             4201         74f42e68                                         000000009d2f3a60     #  5:55 AM
aa10005723   18             4201         88c12f68                                         0000000008a87738     #  8:30 PM
aa10005723   17             4201         c8182f68                                         00000000b5d849bc     #  8:30 AM
aa10005723   16             4201         70ac2f68                                         00000000d4a1eeac     #  7:00PM
aa10005723   15             4201         b0032f68                                         00000000652349fe     #   7:00AM
aa10005723   14             4201         e02d2f68                                         00000000a24d63f5     #  10:00AM
turning off?
aa0800a823   13   45013349aa77 
aa10005723   12   17011c1b01000000000   vb04a0378b5
aa10005723   11   17011a1b01000000000   0cc6cf5ea



Check sum solving
aa100057231c4201004a2f6800000000  edfb6182
aa100057231b4201a0f52e6800000000  0ee5761c
aa100057231a4201349d2f6800000000  e2513705
aa1000572319420174f42e6800000000  9d2f3a60
aa1000572318420188c12f6800000000  08a87738
aa10005723174201c8182f6800000000  b5d849bc
aa1000572316420170ac2f6800000000  d4a1eeac
aa10005723154201b0032f6800000000  652349fe
aa10005723144201e02d2f6800000000  a24d63f5
#seems that they are using a 32 bit checksum/ 4 bytes 
#CRC Beagle, python for reverse engineering checksum- use 5/28
#CRC RevEng, crc CLI tool that allows for rev eng crcs- RUST
#FIRST TRY SEARCHING FOR CRC



#this is the code for setting an alarm (testing only)
import struct
from crccheck.crc import Crc32Base  # crc check python module (pip install crccheck) 

class WhoopCRC(Crc32Base):      
    _polynom = 0x04C11DB7  #basic crc-32 poly
    _initvalue = 0x00000000
    _reflect_input = True
    _reflect_output = True
    _xor_output = 0xF43F44AC    #calculated crc value from reverse engineering

def get_crc(stuff):
    x = WhoopCRC.calc(stuff)
    y = struct.pack("<I", x)
    return y

data = bytes.fromhex("aa10005723144201e02d2f6800000000")  #crc only does calculations in byte data so must convert from hex
PacketCRC= get_crc(data)
print("crc is:", PacketCRC.hex())    










Flutter Ideas


Flutter_reactive_ble to send, scan, connec and write/read to the whoop
Possibly flutter_blue_plus

Into Info.plist:
<key>NSBluetoothAlwaysUsageDescription</key>
<string>This app uses Bluetooth to connect to heart monitors.</string>
<key>NSBluetoothPeripheralUsageDescription</key>
<string>Used to read heart rate data from your device.</string>

USE FIREBASE FOR STORING DATA

USE TESTFLIGHT TO TEST APPLICATION THROUGH VIRTUAL MACHINE


