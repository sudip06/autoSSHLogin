import os
from IPy import IP
import csv
import paramiko

"""
Check if the ip adress is valid and reachable through ping command 
"""
def is_valid_ipv4_address(address):
    try:
        IP(address)
    except ValueError:
        return False

    str="ping -q -c 3 -W 3 "+address+" 1>/dev/null 2>&1"
    ret=os.system(str)
    print "%s:Alive" %(address) if ret == 0 else "%s:Not alive"%(address)
    return True if ret == 0 else False

"""
Read the configuration file to get the ssh server address,
credentials and list of commands to be executed
"""
def readIpAddress():
    try:
        with open('ipAddr.txt','rb') as csvFile:
            ipList=csv.reader(csvFile, delimiter=':')
            data=[]
            for row in ipList:
                data.append(row)
            return data
    except IOError:
        print "file ipAddr.txt does not exist"

ipList=readIpAddress()

for index,ipData in enumerate(ipList):
    ipAddress = ipData[0]
    username  = ipData[1]
    password  = ipData[2]
    session   = paramiko.SSHClient()
    commandsToExecute = ipData[3]
    
    if is_valid_ipv4_address(ipAddress)==True:
        try:
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #Connect to the device using username and password 
            session.connect(ipAddress, username = username, password = password)
            commandsList=commandsToExecute.split(",")
            
            outFileName="output"+str(index+1)+".txt"
            with open(outFileName,'wb') as writeFile:
                print >> writeFile, "IP Address:"+ipAddress+"\n=====================\n" 
                for commands in commandsList:
                    print >> writeFile, commands 
                    print >> writeFile, "================" 
                    stdin, stdout, stderr = session.exec_command(commands)
                    print >> writeFile, stdout.read()
        except (paramiko.AuthenticationException,paramiko.SSHException,paramiko.ssh_exception.NoValidConnectionsError):
            print "Error: SSH connection to " +ipAddress +" failed"
        finally:
            session.close()
