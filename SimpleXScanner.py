import time
import random
import os
import sys
from scan import NetworkScanner
from termcolor import colored

os.system("clear")
nmap = NetworkScanner()
NumberOfDevices = nmap.ScanNetwork()
print "------------------------"
time.sleep(0.1)
print colored("Connected Devices: {}".format(NumberOfDevices), "blue")
