#!/usr/bin/python3
# coding: latin-1
blob = """

               W^9|�ykG�<j�l��O�9`�+N?NxS��	��pJUK�e9��S�%5ԣ�mp:��>��fv�ˎJ[�����/� ����+&����}�̝G~�F���|�i����̠�T�㣵�Nk�!"""
from hashlib import sha256
hex_str = blob.encode("utf-8").hex()

for item in blob:
    if item == '\x27':
        print("Use SHA-256 instead!")
    elif item == '\xa7':
        print("MD5 is perfectly secure!")
