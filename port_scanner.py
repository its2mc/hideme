"""
This script was ported from the python for beginners website
Although it is probably free for use.. check out the link
http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

The port scanner just finds ports, you have to implement
a traffic sniffer.
http://www.binarytides.com/python-packet-sniffer-code-linux/
"""
import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('clear',shell=True)

#Ask for input
remoteServer = raw_input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scannning remote host", remoteServerIP
print "-" * 60

#Check what time the scan started
t1 = datetime.now()

#Using the range function to specify ports (here it will scan all ports between 1 and 1024)

#We also put in some error handling for catching errors

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result =  sock.connect_ex((remoteServerIP,port))
		if result == 0:
			print "Port {}: \t Open".format(port)
		sock.close()

except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit()

except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

except socket.error:
	print "Couldnt connect to server"
	sys.exit()

#Checking the time again
t2 = datetime.now()

#Calculates the difference in time, to see hwo long it took to run the script
total = t2- t1

print "Scanning compeleted in:",total