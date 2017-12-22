import logging
from messageColor import message
import subprocess as s



def createLog(status):
	username = s.Popen("whoami", shell=True, stdout=s.PIPE)
	userOutput = username.communicate()[0]
	LOG_FILENAME = 'logs/run.log'
	if status == "read":
		logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
		logging.warning("The encrypted file was opened by macupdate.py by the user: "+userOutput)
	if status == "wrote":
		logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
		logging.warning("An encrypted passfile was created named key.enc for further use in this script by the user:"+userOutput)

def main():
	createLog("read")

if __name__ == "__main__":
	main()