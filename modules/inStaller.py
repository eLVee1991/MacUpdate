from messageColor import message
import pexpect

def Install_Homebrew():
	message("succes", "[+] Running script for installing Homebrew for Mac")
	print("")
	install_homebrew = '''/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'''
	command = pexpect.spawnu(install_homebrew)
	command.expect("")
	command.sendline()
	message("succes", "[+] Done installing Homebrew")

def Install_Mas():
	message("succes", "[+] Installing brew package 'MAS'")
	command = pexpect.spawnu("brew install mas")
	command.interact()
	command.close()
	message("succes", "[+] MAS (Mac Apple Store) installed.")

if __name__ == "__main__":
	main()