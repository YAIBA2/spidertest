#!/usr/bin/env python
import logging
import sys
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv)!=2:
    print "出错了"
    sys.exit()

interface=str(sys.argv[1])#1代表读取参数
ip=subprocess.check_output("ifconfig"+interface+"|grep 'inet addr'|cut -d ':' -f 2|cut -d '' -f 1",shell=True).strip()
prefix=ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+ip.split('.')[2]+'.'

for addr in range(0,254):
    answer=sr1(ARP(pdst=prefix+str(addr)),timeout=0.1,verbose=0)
    if answer==None:
        pass
    else:
        print prefix+str(addr)
