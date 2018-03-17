from pexpect import pxssh
import subprocess
import getpass
import argparse
from modules.messageColor import message
from modules.logFile import createLog
from modules.cryptor import decryptor, ifExist, notExist


"""
- een losse logfile aanmaken voor de SSH controller
- een mogelijkheid maken om geen ip maar een txtfile met ip's in te geven (miss gebruik maken van argparse ipv sys.argv)
- cryptor gebruiken om het wachtwoord op te slaan voor de ssh controller in een aparte file (cryptor file encrypt & decrypt functies aanpassen) bijv keys2.enc
hierdoor kan het script als een cronjob draaien. Wel zo hendig :)

"""

def connectToServer(client, ipaddress, password, settings):
	"""
	This function creates a connection to the host via ssh using pxssh.
	"""
	message("succes", "[+] Connecting to "+args.client+"@"+args.ipadress+" to run macupdate.py script.")
	child = pxssh.pxssh()
	child.login(ipadress, client, password)
	message("succes", "[+] Settings has been set to "+settings+". Running script on client. Please wait.")
	# Change the line below to the correct folder.
	child.sendline("cd Projects/MacUpdate/1.5/ && python macupdate.py "+settings)
	child.prompt()
	print(child.before)
	child.logout()


def Main():
	scriptSettings = ""
	try:
		if args.install:
			scriptsSettings == "-i"
			connectToServer(args.client, args.ipaddress, password, scriptSettings)
		if args.update:
			scriptSettings == "-u"
			connectToServer(args.client, args.ipaddress, password, scriptSettings)
		else:
			message("warning", args)
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
	message("underline", "Version 1.5")
	message("underline", "Created by eLVee")
	print("")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--client", type=str,
	                    help="The username of the client")
	parser.add_argument("-ip", "--ipaddress", type=str,
	                    help="The ip address of the client")
	parser.add_argument("-u", "--update", action="store_true", 
						help="This will set mode to 'update'")
	parser.add_argument("-i", "--install", action="store_true",
						help="This will set mode to 'install'")
	args = parser.parse_args()
	Text()
	message("succes", "[+] The script will continue to run now")
	logMessage = "The controller script has been run by the user: "
	createLog(logMessage, "logs/controller.log")
	Main()

