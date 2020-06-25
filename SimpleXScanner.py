import time
import random
import os
import sys
import requests
import platform
from scan import NetworkScanner
from termcolor import colored

if platform.system() == "Windows":
    print "ERROR: SimpleXScanner only supports Linux"
    exit()
else:
    if os.geteuid() != 0:
        print "ERROR: Run script as root with sudo"
        exit()

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


defaultNetworkGetaway = raw_input("Default Getaway: ")

clear()
print "Scanning Network, Please Wait....."
nmap = NetworkScanner()
scanInformation = nmap.ScanNetwork(defaultNetworkGetaway)
vendorNames = []

url = "http://macvendors.co/api/"

for counter in range(len(scanInformation)):
    mac = scanInformation[counter][1]
    mac_vendor_requests = requests.get(url+mac+"/json")
    mac_vendor_json = mac_vendor_requests.json()
    vendorNames.append(mac_vendor_json['result']['company'])


for connectedDevicesCounter in range(len(scanInformation)):
    print colored("[{}]: {} \t {} \t {}".format(connectedDevicesCounter, scanInformation[connectedDevicesCounter][0], scanInformation[connectedDevicesCounter][1], vendorNames[connectedDevicesCounter]), "blue")
    time.sleep(0.1)
print "------------------------"
time.sleep(0.1)
print colored("Connected Devices: {}".format(NumberOfDevices), "blue")
