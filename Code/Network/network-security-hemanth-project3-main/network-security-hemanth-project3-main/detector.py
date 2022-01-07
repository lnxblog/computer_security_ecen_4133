from scapy.all import *
import sys

# Complete this function!
ip2syn={}
attacker={}
def process_pcap(pcap_fname):
    for pkt in PcapReader(pcap_fname):
        # Your code here
        if pkt.haslayer(TCP) and pkt.haslayer(IP) and pkt.haslayer(Ether):
            if pkt[TCP].flags==0x002:
                if pkt[IP].src in ip2syn:
                    ip2syn[pkt[IP].src][0] += 1
                else:
                    ip2syn[pkt[IP].src]=[1,0]
 
                '''
                if pkt[IP].src not in attacker: 
                    if pkt[IP].src in ip2syn:
                        ip2syn[pkt[IP].src][0] += 1
                        if ip2syn[pkt[IP].src][1]>0:
                            if ip2syn[pkt[IP].src][0] > 3*ip2syn[pkt[IP].src][1]:
                                print(pkt[IP].src)
                                attacker[pkt[IP].src]=1
                    else:
                        ip2syn[pkt[IP].src]=[1,0]
                '''
            if pkt[TCP].flags==0x012:
            #    if pkt[IP].dst not in attacker:
                if pkt[IP].dst in ip2syn:
                    ip2syn[pkt[IP].dst][1] += 1
                else:
                    ip2syn[pkt[IP].dst]=[0,1]
                #print(ip2syn) 

        pass

if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])
    for key,value in ip2syn.items():
        if ip2syn[key][1]==0:
            if ip2syn[key][0] >= ip2syn[key][1]:
                print(key)
        else:
            if ip2syn[key][0] >= 3*ip2syn[key][1]:
                print(key)
