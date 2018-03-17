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

def ifExist(file_name, key):
	"""
	This function checks if the keys.enc file exists.
	"""
	if exists(file_name) and exists(key):
		return True
	else:
		return False

def notExist():
	"""
	This functions creates a new keys.enc file if none exists. Otherise manuallpass will be selected.
	"""
	while True:
		message("warning", "[+] The password file cannot be found. Do you want to create it? y/n.")
		answer = raw_input("> ")
		if answer == "y" or answer == "Y":
			randomKeyFile(randomKey)
			keys = getpass.getpass()
			encryptor(fileName, randomKey, keys)
			message("succes", "[+] Succes! The password file has been created.")
			break
		elif answer == "n" or answer == "N":
			message("warning", "[+] Manual pass selected.")
			keys = getpass.getpass()
			return keys
			break
		else:
			message("warning", "[+] Wrong input. Please enter y/n.")

def stringGen(size, chars=string.ascii_uppercase + string.digits):
	"""
	This function creates a random string of characters of the given size in the first keyword argument.
	"""
	return ''.join(random.choice(chars) for _ in range(size))

def randomKeyFile(file_name):
	"""
	This function creates a random keyfile used for encryption and saves it as the first keyword argument.
	"""
	with open(file_name, "w") as kfile:
		key = stringGen(256)
		kfile.write(key)
		kfile.close()

def encryptor(file_name, key, plaintext):
	"""
	This function encrypt the the password using AES256 encryption and saves it as the first keyword argument.
	"""
	with open(file_name, 'w') as efile:
		enc = encrypt(key, plaintext)
		efile.write(enc)
		efile.close()
		etext = "An encrypted passfile was created named key.enc for further use in this script by the user: "
		createLog(etext, 'logs/macupdate.log')

def decryptor(file_name, key):
	"""
	This function decrypts the the password and returns it as a variable.
	"""
	with open(file_name, 'rb') as dfile:
		ciphertext = dfile.read()
		dec = decrypt(key, ciphertext)
		dfile.close()
		dtext = "The encrypted file was opened by macupdate.py by the user: "
		createLog(dtext, 'logs/macupdate.log')
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
