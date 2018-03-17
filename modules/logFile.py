import logging
from messageColor import message
import subprocess as s

def createLog(message, logFilename):
	"""
	This function creates a logfile with the message as the first keyword 
	argument and the name of the logfile as the second keyword argument.
	"""
	username = s.Popen("whoami", shell=True, stdout=s.PIPE)
	userOutput = username.communicate()[0]
	logging.basicConfig(format='%(asctime)s %(message)s', filename=logFilename, level=logging.DEBUG)
	logging.warning(message+userOutput)

def main():
	createLog("read")

if __name__ == "__main__":
	main()
