#!/usr/bin/python3

import requests
import sys
success_msg_mac = 'Decrypted message must contain a correct MAC'
success_msg_valid = 'The ciphertext is valid'
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: %s ORACLE_URL CIPHERTEXT_HEX" % (sys.argv[0]), file=sys.stderr)
        sys.exit(-1)
    oracle_url = sys.argv[1]
    ciphertext = sys.argv[2]
    
    final_decrypt_msg=bytearray()
    chunks=[]
    for i in range(0,len(ciphertext),32):
        chunks.append(ciphertext[i:i+32])
    #print(chunks)
    pad_flag=0
    
    for i in range(1,len(chunks)):
    
        decrypt_cipher = bytearray.fromhex(chunks[-i])
        #attack_cipher = bytearray.fromhex('b39a4600e2938055eb992a6a92ddcc01')
    
        attack_cipher = bytearray.fromhex(chunks[-(i+1)])
        #decoded_bytes = bytearray.fromhex('0cc1d09f672794e6588d9eef')
        
        decoded_bytes = bytearray()

        pre_attack_cipher = ''.join(chunks[0:-(i+1)])

        post_attack_cipher = chunks[-i]

        for curr_pad in range(1,len(decrypt_cipher)+1):
            
            xor_byte = attack_cipher[-curr_pad]
            #print('start',curr_pad)
            #print('attack',attack_cipher.hex(),decrypt_cipher.hex())
            for i in range(256):
                attack_cipher[-1*curr_pad] = i
                #print(i,attack_cipher.hex())
                #pre_cipher = ''.join(chunks[0:-2])
                #final_attack_cipher = pre_attack_cipher + attack_cipher.hex() + post_attack_cipher
                final_attack_cipher = attack_cipher.hex() + decrypt_cipher.hex()
                #print(final_attack_cipher)
        
                # Example check of ciphertext at the oracle URL:
                r = requests.get("%s?message=%s" % (oracle_url, final_attack_cipher))
                #r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(ciphertext).hex()))
                r.raise_for_status()
                obj = r.json()
                #print(obj)
                if (obj['message'] == success_msg_mac or (obj['message'] == success_msg_valid and len(final_decrypt_msg)>1)):
                    #print(obj)
                    #print(attack_cipher.hex())
                    dcode_byte = curr_pad ^ attack_cipher[-curr_pad]
                    final_byte = dcode_byte ^ xor_byte
                    if pad_flag == 0:
                        if final_byte == 1:
                            continue
                        else:
                            pad_flag = final_byte
                    decoded_bytes.append(curr_pad ^ attack_cipher[-curr_pad])
                    #print('decoded byte',decoded_bytes.hex())
                    final_decrypt_msg.append(decoded_bytes[curr_pad-1] ^ xor_byte)
                    #print('final msg',final_decrypt_msg.hex())
                    for i in range(curr_pad):
                        attack_cipher[-(i+1)] = decoded_bytes[i] ^ (curr_pad + 1)
                    break
                if i==255:
                   sys.exit(-1)
    
    #print('Padding',pad_flag)
    
    #pad_flag=0xd
    message = bytes.fromhex(final_decrypt_msg[pad_flag + 32:].hex())
    print(message.decode('ascii')[::-1])
