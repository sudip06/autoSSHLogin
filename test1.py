import os
from IPy import IP

def is_valid_ipv4_address(address):
    try:
        IP(address)
    except ValueError:
        return False

    return True

def readIpAddress():
    try:
        with open('ipAddr.txt') as fileHandle:
            ipList=fileHandle.read().splitlines()
            return ipList
    except IOError:
        print "file ipAddr.txt does not exist"



ipList=readIpAddress()
for ipAddr in ipList:
    if not is_valid_ipv4_address(ipAddr)==True: print "%s:Invalid address" %(ipAddr) 
    str="ping -q -c 3 -W 3 "+ipAddr+" 1>/dev/null 2>&1"
    ret=os.system(str)
    print "%s:Alive" %(ipAddr) if ret == 0 else "%s:Not alive"%(ipAddr)
