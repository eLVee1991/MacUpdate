from messageColor import message
import pexpect
from cryptor import decryptor, ifExist, notExist
import getpass

def Mac_Update():
	fileExist = ifExist("logs/keys.enc", "logs/gen.enc")
	if fileExist:
		data = decryptor("logs/keys.enc", "logs/gen.enc")
	else:
		notExist()
		data = getpass.getpass()
	#Run the command in the terminal before running the script.
	command_1 = pexpect.spawnu('sudo softwareupdate -ia --verbose')
	message("succes", "[+] Updating your mac. Please wait.")
	command_1.expect('Password:'.decode('utf8'))
	command_1.sendline(data)
	command_1.sendline()
	command_1.interact()
	command_1.close()
	message("succes", "[+] Done updating Mac OS Software")

def Update_Homebrew():
	message("succes", "[+] Installing update of homebrew.")
	command = pexpect.spawnu("brew update")
	command.interact()
	command.close()
	message("succes", "[+] Done installing homebrew")

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

def main():
	Mac_Update()
	Update_Homebrew()
	Update_AppleStore()

if __name__ == "__main__":
	main()

