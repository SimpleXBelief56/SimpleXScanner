import time
import random
import os
import sys
import nmap
from termcolor import colored

class NetworkScanner():
	def __init__(self):
		self.deviceCounter = 0
		self.network = nmap.PortScanner()

	def ScanNetwork(self):
		self.hosts_dict = self.network.scan(hosts='192.168.1.1/24', arguments='-sP')
		print "IP ADDRESS \t\t MAC ADDRESS \t\t HOST NAME"
		for scan_section in self.hosts_dict['scan']:
			self.deviceCounter += 1
			for host_information in self.hosts_dict['scan'][scan_section]:
				if host_information == 'vendor':
					for host_name in self.hosts_dict['scan'][scan_section][host_information]:
						print colored("[{}]: {} \t {} \t {}".format(self.deviceCounter, scan_section, host_name, self.hosts_dict['scan'][scan_section][host_information][host_name]), "blue")
						
			time.sleep(0.1)

		return self.deviceCounter


