# Reverse Engineering Whoop 4.0

The **Whoop 4.0** is a fitness band that requires a subscription to use.  
This project is just my documentation of reverse engineering it and working on an actual mobile app.

---

## Packet Analysis

### Whoop Timer Data
```
Header       Packet Count   Device #   Unix Timestamp (Hex LE)   4 blank bytes   Checksum
aa10005723   1c             4201       004a2f68                  00000000        edfb6182   # 12:00 PM
aa10005723   1b             4201       a0f52e68                  00000000        0ee5761c   #  6:00 AM
aa10005723   1a             4201       349d2f68                  00000000        e2513705   #  5:55 PM
aa10005723   19             4201       74f42e68                  00000000        9d2f3a60   #  5:55 AM
aa10005723   18             4201       88c12f68                  00000000        08a87738   #  8:30 PM
aa10005723   17             4201       c8182f68                  00000000        b5d849bc   #  8:30 AM
aa10005723   16             4201       70ac2f68                  00000000        d4a1eeac   #  7:00 PM
aa10005723   15             4201       b0032f68                  00000000        652349fe   #  7:00 AM
aa10005723   14             4201       e02d2f68                  00000000        a24d63f5   # 10:00 AM
```
I am unsure what the 4 blank bytes are for. I think that they are a placeholder for the checksum when sent however I will need to do more testing to check my hypothesis. 


### Misc Packets
```
turning off?
aa0800a823   13   45013349aa77 
aa10005723   12   17011c1b01000000000   vb04a0378b5
aa10005723   11   17011a1b01000000000   0cc6cf5ea
```

---

## Checksum Analysis

The device appears to use a **32-bit checksum (CRC)**.

```
aa100057231c4201004a2f6800000000  edfb6182
aa100057231b4201a0f52e6800000000  0ee5761c
aa100057231a4201349d2f6800000000  e2513705
aa1000572319420174f42e6800000000  9d2f3a60
aa1000572318420188c12f6800000000  08a87738
aa10005723174201c8182f6800000000  b5d849bc
aa1000572316420170ac2f6800000000  d4a1eeac
aa10005723154201b0032f6800000000  652349fe
aa10005723144201e02d2f6800000000  a24d63f5
```

### Notes
- Likely **CRC-32** or a variant.  
- Tools for reverse-engineering CRC:
  - [CRC Beagle](https://reveng.sourceforge.io)
  - [CRC RevEng](https://reveng.sourceforge.io) (CLI, Rust implementation also available)

---

## Python Example (Alarm Testing)

```python
import struct
from crccheck.crc import Crc32Base  # pip install crccheck

class WhoopCRC(Crc32Base):      
    _polynom = 0x04C11DB7       # Standard CRC-32 polynomial
    _initvalue = 0x00000000
    _reflect_input = True
    _reflect_output = True
    _xor_output = 0xF43F44AC    # Discovered via reverse-engineering

def get_crc(stuff):
    x = WhoopCRC.calc(stuff)
    y = struct.pack("<I", x)    # Little endian
    return y

data = bytes.fromhex("aa10005723144201e02d2f6800000000")
PacketCRC = get_crc(data)
print("crc is:", PacketCRC.hex())
```

---

## Flutter Integration

Potential approaches for app development:

- **Bluetooth Libraries**
  - [`flutter_reactive_ble`](https://pub.dev/packages/flutter_reactive_ble) → scan, connect, read/write to Whoop
  - [`flutter_blue_plus`](https://pub.dev/packages/flutter_blue_plus)

- **Info.plist (iOS)**
```xml
<key>NSBluetoothAlwaysUsageDescription</key>
<string>This app uses Bluetooth to connect to heart monitors.</string>
<key>NSBluetoothPeripheralUsageDescription</key>
<string>Used to read heart rate data from your device.</string>
```

- **Backend & Testing**
  - Firebase → data storage
  - TestFlight → iOS testing (can run in a VM)

---

## Next Steps

- Confirm CRC parameters using **RevEng** or **CRC Beagle**.  
- Implement Flutter prototype for BLE scanning & data collection.  
- Store parsed data in Firebase.  
- Experiment with Whoop’s hidden packet structures (alarms, heart rate, sleep, etc.).  
