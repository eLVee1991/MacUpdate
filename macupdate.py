#!/usr/bin/env python3

#usage python3 macupdate.py [-i -u -h -s -ip]

import subprocess
import sys
import getpass

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

	Text()
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
					subprocess.Popen("sudo systemsetup -f -setremotelogin on", shell=True)
					print("SSh was enabled")
					print("-"*60)
					print("")
					break
				elif ssh == "d":
					subprocess.Popen("sudo systemsetup -f -setremotelogon off", shell=True)
					print("SSH was disabled.")
					print("-"*60)
					print("")
					break
				else:
					print("Error: wrong input. Please enter e/d")
		elif argument[1] == "-ip":
			ip = input("Please enter the ip you want to give this mac: ")
			subprocess.Popen("sudo ipconfig set en1 INFORM "+ip, shell=True)
			print("Changed the ip to: "+ip)
			print("-"*60)
			print("")
		elif argument[1] is not "-i" or "-u" or "-h" or "-s" or "-ip":
			print(usage)
			exit()

	except IndexError:
		print("-"*60)
		print("Error: No 2nd argument added. See the usage below:")
		print("-"*60)
		print("")
		print(usage)
		exit()

def Mac_Update():
	while True:
		try:
			import pexpect
			#Run the command in the terminal before running the script.
			print("Please enter your password here to be able to install/update: ")
			password = getpass.getpass()
			print("-"*60)
			command_1 = pexpect.spawnu('sudo softwareupdate -ia --verbose')
			#command_1.interact()
			print("Running script for updating the mac from commandline.")
			command_1.expect('Password:')
			print("Asking for password. Passing it now.")
			command_1.sendline(password)
			command_1.sendline()
			print("Done")
			print("Updating now.")
			#command_1.close()
			print("Done updating Mac OS Software")
			print("-"*60)
			print("")
			break
		except ModuleNotFoundError:
			while True:
				print("The python module 'pexpect' is needed for this script to work.")
				module = input("Do you want to install pexpect now? y/n: ")
				if module == "y":
					subprocess.Popen("pip3 install pexpect", shell=True)
					print("Done installing pexpect")
					print("Please run the script again.")
					print("-"*60)
					print("")
					break
				elif module == "n":
					print("Closing the script.")
					print("-"*60)
					print("")
					break
				else:
					print("-"*60)
					print("Error: Please answer with y/n")
					print("-"*60)
					print("")

def Text():
	print("""
######################################################
#						     #
#	     MAC OS AND APPSTORE UPDATER	     #
#		       				     #
######################################################
""")
	print("Version 1.3")
	print("Created by eLVee")
	print("-"*60)

def Install_Homebrew():
	print("Running script for installing Homebrew for Mac")
	print("")
	command_2 = '''/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'''
	subprocess.Popen(command_2, shell=True)
	print("Done installing Homebrew")
	print("-"*60)
	print("")

def Update_Homebrew():
	print("Installing update of homebrew.")
	subprocess.Popen("brew update", shell=True)
	print("-"*60)
	print("")

def Install_Mas():
	subprocess.Popen("brew install mas", shell=True)
	print("MAS (Mac Apple Store) package installed.")
	print("-"*60)
	print("")

def Update_AppleStore():
	print("Running MAS (Mac Apple Store) updater")
	print("Showing outdated apps.")
	subprocess.Popen('mas outdated', shell=True)
	print("Updating the apps now..")
	subprocess.Popen('mas upgrade', shell=True)	
	print("Done updating Apple Store apps")
	print("-"*60)
	print("")

if __name__ == "__main__":
	Main()
