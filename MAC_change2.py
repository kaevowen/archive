from random import randrange
from time import sleep

import re
import socket
import winreg
import subprocess

def randbit(n):
    randbit = ''
    for i in range(n):
        randbit+=bit[randrange(1,16)]

    return randbit

bit = [
'0', '1', '2', '3', 
'4', '5', '6', '7', 
'8', '9', 'A', 'B', 
'C', 'D', 'E' ,'F'
]
regex = [re.compile('Realtek.*'), re.compile('Intel.*')]
NETWORK_REG_PATH = "SYSTEM\\CurrentControlSet\\Control\\Class\\" \
+ "{4d36e972-e325-11ce-bfc1-08002be10318}"
HKLM_KEY = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, NETWORK_REG_PATH, 
    0, winreg.KEY_ALL_ACCESS)

EnumLIST = []
for i in range(0,512):
    try:
        EnumLIST.append(winreg.EnumKey(HKLM_KEY, i))
    except:
        pass
print(f"SubKey List : {EnumLIST}")
for Enum in EnumLIST:
    try:
        Sub_key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, 
            NETWORK_REG_PATH+'\\'+Enum, 0, winreg.KEY_ALL_ACCESS)
    except OSError:
        pass

    for reg in regex:
        if re.match(reg, winreg.EnumValue(Sub_key, 0)[1]):
            try:
                winreg.DeleteValue(Sub_key, 'NetworkAddress')
            except:
                print('Cannot delete sub key.')

            MAC_VALUE = randbit(12)
            winreg.SetValueEx(Sub_key, 'NetworkAddress', 0, winreg.REG_SZ, 
                MAC_VALUE)
            print(f"MAC Address changed.  Value : {MAC_VALUE}")
            winreg.CloseKey(Sub_key)
            KEYFIND = True
            break
        else:
            KEYFIND = False
            pass

    if KEYFIND == True:
        break

print('network will be restart...')
subprocess.call('netsh interface set interface name = "이더넷" admin=disabled')
subprocess.call('netsh interface set interface name = "이더넷" admin=enable')

#socket기능의 except가 발생하면 subprocess를 사용해 ipconfig 출력
local_ip = [re.compile('127.*'), re.compile('169.*')]
print("Checking IP...")
while True:
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        
        if re.match(local_ip[0], IPAddr) or re.match(local_ip[1], IPAddr):
            pass
        else:
            print("changed IP : ", IPAddr)
            break
    except:
        subprocess.call('ipconfig')

input('press enter to exit...')