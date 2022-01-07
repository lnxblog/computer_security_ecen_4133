#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

demo_text= 'ethicslawanduniversitypoliciestodefendasystemyouneedtobeabletothink\
likeanattackerandthatincludesunderstandingtechniquesthatcanbeusedto\
compromisesecurityhoweverusingthosetechniquesintherealworldmayviola\
tethelawandtheuniversityscomputingpracticesormaybeunethicalyoumustr\
especttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfai\
lthecourseundersomecircumstancesevenprobingforweaknessesmayresultin\
severepenaltiesuptoandincludingcivilfinesexpulsionandjailtimecarefu\
llyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycri\
minalizescomputerintrusionsthisisjustoneofseverallawsthatgovernhack\
ingunderstandwhatthelawprohibitsyoudontwanttoenduplikethisguyifindo\
ubticanreferyoutoanattorneypleasereviewcaenspolicydocumentonrightsa\
ndresponsibilitiesforguidelinesconcerninguseoftechnologyresourcesat\
umaswellastheengineeringhonorcodeasmembersoftheuniversityyouarerequ\
iredtoadheretothesepolicies'

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    #for key,value in freqs.items():
     #   print('key',key,'relative freq',float(value)/len(s))
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

def relative_freq(s):
    rel_freq_list = {}
    alphbt_list = list(alphabet)
    for i in alphbt_list:
        rel_freq_list[i] = 0

    freqs = Counter(s) 
    for key,value in freqs.items():
        rel_freq_list[key] = float(value)/len(s)
    return rel_freq_list

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    #print(cipher)
    mean_val = sum(letter_freqs.values())/len(alphabet)

    sum_freq_sqr = 0
    for freq_val in letter_freqs.values():
        sum_freq_sqr = sum_freq_sqr + (freq_val - mean_val)**2
        
    alphbt_pop_var = sum_freq_sqr/len(alphabet)

    #print('reference',alphbt_pop_var)
    #print('pop var of demo text',pop_var(demo_text))
    #print('pop variance reference',pop_var(alphabet))
    #################################################################
   # Your code to determine the key and decrypt the ciphertext here

    # Find population variance for all characters in a given key index
    min_pop_var=[0,999]
    for key_size in range(2,14):

        key_list = ['']*key_size
        i=0
        for char in cipher:
            key_list[i%key_size] = key_list[i%key_size] + char
            i = i+1
        #print(key_list)
        cipher_var = [0]*key_size
        for i in range(key_size):
            cipher_var[i] = pop_var(key_list[i])
           
        #print(key_size,cipher_var)
        var_mean = sum(cipher_var)/len(cipher_var)
        #print('var mean',var_mean)
        diff = abs(var_mean - alphbt_pop_var)
        #print(diff)
        if diff < min_pop_var[1]:
            min_pop_var[1] = diff
            min_pop_var[0] = key_size

    #print(min_pop_var)
       
    p_key_size = min_pop_var[0]
    str_list = ['']*p_key_size
    i=0
    for char in cipher:
        str_list[i%p_key_size] = str_list[i%p_key_size] + char
        i = i + 1

    alphbt_list = list(alphabet)
    true_freq_list = []
    for i in alphbt_list:
        true_freq_list.append(letter_freqs[i])
    #print(true_freq_list)
    predict_key=''
    for i in range(p_key_size):
        rel_dict = relative_freq(str_list[i])
        #print(rel_dict)
        test_freq_list = []
        for i in alphbt_list:
            test_freq_list.append(rel_dict[i])
        #print(test_freq_list)

        min_diff = 99
        
        for j in range(26):
            temp = j
            diff = 0
            for k in range(26):
                diff = diff + abs(true_freq_list[k] - test_freq_list[temp%26])
                temp = temp + 1
            if diff < min_diff:
                min_diff = diff
                shift = j
            #print('diff',diff,'for shift',j)
        #print(min_diff,shift)
        predict_key += alphabet[shift]
    print(predict_key)

