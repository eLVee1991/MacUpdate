from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink
from messageColor import message
import getpass
import string
import random
from logFile import createLog

randomKey = "logs/gen.enc"
fileName =  "logs/keys.enc"
settingsfile = "logs/settings.txt"

def ifExist(file_name, key):
	if exists(file_name) and exists(key):
		return True
	# elif exist(settings_file):
	# 	with open ("logs/settings.txt", "r") as sfile:
	# 		settingsFileExist = sfile.read()
	# 		sfile.close()
	# 		if settingsFileExist == "pass_settings = nopass":
	# 			print("settingsfile exist")
	# 		else:
	# 			print("settingsfile doesn't exist")
	else:
		return False

def notExist():
	while True:
		"""
		Maak dit morgen maar af. Zorgen dat het script de settingsfile uitleest als hij bestaat.
		en anders het onderstaande draaid. Nog wat error handling toevoegen enzo.
		Als dit werkt verder met ssh controller script. Zodat die main.py can draaien.
		
		"""
		message("warning", "[+] The password file cannot be found. Do you want to create it? y/n.")
		answer = raw_input("> ")
		if answer == "y" or answer == "Y":
			randomKeyFile(randomKey)
			keys = getpass.getpass()
			encryptor(fileName, randomKey, keys)
			message("succes", "[+] Succes! The password file has been created.")
			break
		elif answer == "n" or answer == "N":
			message("warning", "[+] Do you want to save these settings for later usage? y/n.")
			answer2 = raw_input("> ")
			if answer2 == "y" or answer2 == "Y":
				message("info", "[+] Creating settings file. Script will remember input.")
				with open ("logs/settings.txt", "rw") as sfile:
					sfile.write("pass_settings = nopass")
					sfile.close()
			elif answer2 == "n" or answer2 == "N":
				message("info", "[+] Please fill in your password below so the script can use it.")
				break
			else:
				break
		else:
			message("warning", "[+] Wrong input. Please enter y/n.")

def stringGen(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def randomKeyFile(file_name):
	with open(file_name, "w") as kfile:
		key = stringGen(256)
		kfile.write(key)
		kfile.close()

def encryptor(file_name, key, plaintext):
	with open(file_name, 'w') as efile:
		enc = encrypt(key, plaintext)
		efile.write(enc)
		efile.close()
		createLog("wrote")

def decryptor(file_name, key):
	with open(file_name, 'rb') as dfile:
		ciphertext = dfile.read()
		dec = decrypt(key, ciphertext)
		dfile.close()
		createLog("read")
		return dec

def main():
	# read or create the file
	dExist = ifExist(fileName, randomKey)
	if dExist:
		message("succes", "[+] The password was found. It will now be used.")
		decryptor(randomKey, fileName)
	else:
		notExist()

if __name__ == "__main__":
	main()

	

