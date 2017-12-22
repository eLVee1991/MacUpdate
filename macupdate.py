#!/usr/bin/env python

#usage python macupdate.py [-i -u -h -e]


import subprocess
import sys
from modules.messageColor import message
from modules.inStaller import *
from modules.upDater import *
from modules.cryptor import ifExist, notExist
from getpass import getpass


def Main():
	usage = """
usage: python macupdate.py [-i] [-u] [-h] [-s]

optional arguments:
  -i    Install Homebrew and brew MAS (Mac Apple Store) so you can use the script.
  -u.   Update Homebrew, update brew MAS, update OSX and update M.A.S.
  -h.   Show this help message and exit
  -s 	Run macupdate.py on another mac
"""

	argument = sys.argv
	try:
		Text()
		if argument[1] == "-i":
			Install_Homebrew()
			Install_Mas()
			exit()
		elif argument[1] == "-u":
			Update_Homebrew()
			Mac_Update()
			Update_AppleStore()
			exit()
		elif argument[1] == "-h":
			print(usage)
			exit()
		elif argument[1] == "-s":
			pass
			"""
			TO DO:
			- create part that enables pexpect ssh connection.
			"""
		elif argument[1] == "-e":
			pass
		elif argument[1] is not "-i" or "-u" or "-h" or "-s" or "-ip":
			message("warning", usage)
			exit()

	except IndexError:
		message("error", "[+] No 2nd argument added. See the usage below:")
		print("")
		print(usage)
		exit()
	except KeyboardInterrupt:
		print("")
		message("error", "[+] CTRL+C was entered. Stopping the script!")
		exit()

def Text():
	message("info", """

MM    MM   AAA    CCCCC  UU   UU PPPPPP  DDDDD     AAA   TTTTTTT EEEEEEE
MMM  MMM  AAAAA  CC      UU   UU PP   PP DD  DD   AAAAA    TTT   EE      
MM MM MM AA   AA CC      UU   UU PPPPPP  DD   DD AA   AA   TTT   EEEEE   
MM    MM AAAAAAA CC      UU   UU PP      DD   DD AAAAAAA   TTT   EE       
MM    MM AA   AA  CCCCC   UUUUU  PP      DDDDDD  AA   AA   TTT   EEEEEEE  
                                                     
""")
	message("underline", "Version 1.5")
	message("underline", "Created by eLVee")
	print("")


"""
Main functie herschrijven zodat upDater.py/inStaller.py fileExist behandeld ipv dit script.
"""
if __name__ == "__main__":
	Main()
	
