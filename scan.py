import time
import random
import os
import sys
import nmap
import platform
from termcolor import colored

class NetworkScanner():
	def __init__(self):
		self.deviceCounter = 0
		self.network = nmap.PortScanner()
		self.deviceInformation = []

	def clear(self):
		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

	def ScanNetwork(self, networkDefaultGetaway):
		self.hosts_dict = self.network.scan(hosts='{}/24'.format(networkDefaultGetaway), arguments='-sn')
		self.clear()
		print colored("IP ADDRESS \t\t MAC ADDRESS \t\t HOST NAME", "cyan", attrs=['bold'])
		for scan_section in self.hosts_dict['scan']:
			self.deviceCounter += 1
			for host_information in self.hosts_dict['scan'][scan_section]:
				if host_information == 'vendor':
					for host_name in self.hosts_dict['scan'][scan_section][host_information]:
						self.deviceInformation.append([str(scan_section), str(host_name)])

		return self.deviceInformation


