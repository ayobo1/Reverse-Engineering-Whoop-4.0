import struct
from crccheck.crc import Crc32Base  # pip install crccheck

class WhoopCRC(Crc32Base):      
    _polynom = 0x04C11DB7       # Standard CRC-32 polynomial
    _initvalue = 0x00000000
    _reflect_input = True
    _reflect_output = True
    _xor_output = 0xF43F44AC    # Discovered via reverse-engineering

def get_crc(hexString):
    x = WhoopCRC.calc(hexString)
    y = struct.pack("<I", x)    # Little endian
    return y
