#!/usr/bin/env python3

#usage python3 macupdate.py [-i -u -h -s -ip]

import subprocess
import sys
import getpass
import pexpect

class colors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def message(state, msg):
	if state == "succes":
		print(colors.GREEN + msg + colors.END)
	elif state == "warning":
		print(colors.WARNING + msg + colors.END)
	elif state == "header":
		print(colors.HEADER + msg + colors.END)
	elif state == "underline":
		print(colors.UNDERLINE + msg + colors.END)
	elif state == "bold":
		print(colors.BOLD + msg + colors.END)
	elif state == "info":
		print(colors.RED + msg + colors.END)
	else:
		print(msg)

def Main():
	usage = """
usage: python3 macupdate.py [-i] [-u] [-h] [-s] [-ip]

optional arguments:
  -i    Install Homebrew and brew MAS (Mac Apple Store) so you can use the script.
  -u.   Update Homebrew, update brew MAS, update OSX and update M.A.S.
  -h.   Show this help message and exit
  -s    Enable/Disable SSH on a mac.
  -ip    Setup a static ip on a mac.
"""

	argument = sys.argv
	try:
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
			while True:
				ssh = input("Do you want to enable/disable? e/d: ")
				if ssh == "e":
					command = pexpect.spawnu("sudo systemsetup -f -setremotelogin on")
					command.expect("Password:")
					command.sendline(password)
					message("succes", "[+] SSH was enabled")
					print("")
					break
				elif ssh == "d":
					command = pexpect.spawnu("sudo systemsetup -f -setremotelogon off")
					command.expect("Password:")
					command.sendline(password)
					message("succes", "[+] SSH was disabled")
					print("")
					break
				else:
					message("warning", "[+] Wrong input. Please enter 'e'or 'd'")
		elif argument[1] == "-ip":
			ip = input("Please enter the ip you want to give this mac: ")
			command = pexpect.spawnu("sudo ipconfig set en1 INFORM "+ip)
			command.expect("Password:")
			command.sendline(password)
			message("succes", "[+] Changed the ip to: "+ip)
			print("-"*60)
			print("")
		elif argument[1] is not "-i" or "-u" or "-h" or "-s" or "-ip":
			message("warning", usage)
			exit()

	except IndexError:
		print("-"*60)
		message("error", "[+] No 2nd argument added. See the usage below:")
		print("-"*60)
		print("")
		print(usage)
		exit()

def Mac_Update():
	#Run the command in the terminal before running the script.
	command_1 = pexpect.spawnu('sudo softwareupdate -ia --verbose')
	message("succes", "[+] Updating your mac. Please wait.")
	command_1.expect('Password:')
	command_1.sendline(password)
	command_1.sendline()
	command_1.interact()
	command_1.close()
	message("succes", "[+] Done updating Mac OS Software")
	print("")

def Text():
	message("info", """

	 MM    MM   AAA    CCCCC    OOOOO   SSSSS  
	 MMM  MMM  AAAAA  CC    C  OO   OO SS      
	 MM MM MM AA   AA CC       OO   OO  SSSSS  
	 MM    MM AAAAAAA CC    C  OO   OO      SS 
	 MM    MM AA   AA  CCCCC    OOOO0   SSSSS  
                                          
  AAA   PPPPPP  PPPPPP   SSSSS  TTTTTTT  OOOOO  RRRRRR  EEEEEEE 
 AAAAA  PP   PP PP   PP SS        TTT   OO   OO RR   RR EE      
AA   AA PPPPPP  PPPPPP   SSSSS    TTT   OO   OO RRRRRR  EEEEE   
AAAAAAA PP      PP           SS   TTT   OO   OO RR  RR  EE      
AA   AA PP      PP       SSSSS    TTT    OOOO0  RR   RR EEEEEEE 
                                                                
  UU   UU PPPPPP  DDDDD     AAA   TTTTTTT EEEEEEE RRRRRR  
  UU   UU PP   PP DD  DD   AAAAA    TTT   EE      RR   RR 
  UU   UU PPPPPP  DD   DD AA   AA   TTT   EEEEE   RRRRRR  
  UU   UU PP      DD   DD AAAAAAA   TTT   EE      RR  RR  
   UUUUU  PP      DDDDDD  AA   AA   TTT   EEEEEEE RR   RR 
                                                        
""")
	message("underline", "Version 1.4")
	message("underline", "Created by eLVee")
	print("")

def Install_Homebrew():
	message("succes", "[+] Running script for installing Homebrew for Mac")
	print("")
	install_homebrew = '''/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'''
	command = pexpect.spawnu(install_homebrew)
	command.expect("")
	command.sendline()
	message("succes", "[+] Done installing Homebrew")

def Update_Homebrew():
	message("succes", "[+] Installing update of homebrew.")
	command = pexpect.spawnu("brew update")
	command.interact()
	command.close()
	message("succes", "[+] Done installing homebrew")

def Install_Mas():
	message("succes", "[+] Installing brew package 'MAS'")
	pexpect.spawnu("brew install mas")
	command.interact()
	command.close()
	message("succes", "[+] MAS (Mac Apple Store) installed.")

def Update_AppleStore():
	message("succes", "[+] Running MAS (Mac Apple Store) updater")
	print("Showing outdated apps:")
	command = pexpect.spawnu('mas outdated')
	command.interact()
	command.close()
	message("succes", "[+] Updating the apps now..")
	command = pexpect.spawnu('mas upgrade')
	command.interact()
	command.close()
	message("succes", "[+] Done updating Apple Store apps")

if __name__ == "__main__":
	Text()
	message("warning", "[+] Before you can use this script you need to fill in your password below. This will make sure the script can update automatically.")
	password = getpass.getpass()
	if password != None:
		message("succes", "[+] The script will continue to run now")
	else:
		message("warning", "No/bank password was entered..")
	Main()
