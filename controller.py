from pexpect import pxssh
import subprocess
import sys
from modules.messageColor import message
from modules.inStaller import *
from modules.upDater import *
from modules.cryptor import ifExist


"""
- sshcontroler aanpassen naar een autoconnect via ssh (keychain onthouden en toevoegen aan servers CMD+K)
als sshcontroler werkt, dan zorgen dat de keys.enc en gen.enc gehost staan op de sshserver en via ssh
worden verstuurd, zodat daar alleen het wachtwoord staat. En nergerns anders. Tot slot cronjob van maken, zodat hij
het automatisch verstuurd.


- IPV SSH kan je ook een server, en client aanmaken....


- een optie argv. -e toevoegen om een encryptie bestand aan te maken, lostaant van het macupdate script.
"""

def Update_OS():
	for connection in connection_list:
		message("succes", "[+] Connecting to "+username+"@"+connection+" to update mac OS software")
		child = pxssh.pxssh()
		child.login(connection, username, password)
		message("succes", "[+] Updating your mac. Please wait.")
		child.sendline('sudo softwareupdate -ia --verbose')
		child.expect('Password:')
		child.sendline(password)
		child.sendline()
		message("succes", "[+] Updating mac OS software")
		child.interact()
		child.logout()
		message("succes", "[+] Done updating mac OS software")

def Main():
	usage = """
usage: python controller.py [-c] user ip [-i] or [-u] 
example: python controller.py -c admin 192.168.0.1 -u
or user the [-h] for this usage page.
optional arguments:
  -c.   Creates a connection to the given ip.
  -i.   Install Homebrew and brew MAS (Mac Apple Store) so you can use the script.
  -u.   Update Homebrew, update brew MAS, update OSX and update M.A.S.
  -h.   Show this help message and exit
"""

	arg = sys.argv
	username = arg[2]
	ip = arg[3]
	try:
		if arg[1] == "-c" and arg[4] == "-i":
			message("succes", "[+] Connecting to "+username+"@"+ip+" to run macupdate.py script (script must be installed!)")
			child = pxssh.pxssh()
			child.login(connection, username, password)
			message("succes", "[+] Updating your mac. Please wait.")
			child.sendline("python macupdate.py -i")
			exit()
		elif arg[1] == "-c" and arg[4] == "-u"::
			message("succes", "[+] Connecting to "+username+"@"+ip+" to run macupdate.py script (script must be installed!)")
			child.login(connection, username, password)
			message("succes", "[+] Updating your mac. Please wait.")
			child.sendline("python macupdate.py -u")
			exit()
		elif arg[1] == "-h":
			print(usage)
			exit()
		else:
			message("warning", usage)
			exit()

	except IndexError:
		print("-"*60)
		message("error", "[+] No 2nd argument added. See the usage below:")
		print("-"*60)
		print("")
		print(usage)
		exit()

def Text():
	message("info", """
                        .dP"Y8 .dP"Y8 88  88                            
                        `Ybo." `Ybo." 88  88                            
                        o.`Y8b o.`Y8b 888888                            
                        8bodP' 8bodP' 88  88

8b    d8    db     dP""b8 88   88 88""Yb 8888b.     db    888888 888888 
88b  d88   dPYb   dP   `" 88   88 88__dP  8I  Yb   dPYb     88   88__   
88YbdP88  dP__Yb  Yb      Y8   8P 88.     8I  dY  dP__Yb    88   88   
88 YY 88 dP    Yb  YboodP `YbodP' 88     8888Y"  dP    Yb   88   888888 

""")                                
	message("underline", "Version 1.3")
	message("underline", "Created by eLVee")
	print("")


if __name__ == "__main__":
	Text()
	fileExist = ifExist('logs/keys.enc', "logs/gen.enc")
	if fileExist:
		message("succes", "[+] The script will continue to run now")
		Main()
	else:
		notExist()
		message("info", "[+] Please run the script again.")
		exit()
