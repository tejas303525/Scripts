#simple sql injection model for automating injection 

import requests 

#url should be changed 

url = 'https://redtiger.labs.overthewire.org/level1.php'

#open the txt file containing the cheat sheet 
#taken for example about the cheatsheet.txt 

f=open("cheatsheet.txt" , "r") # "read mode - r"

#fill the file name and complete the loop 
#readline fuction to read single line  

for line in f:
	
#use appropriate params

data = {"user": "test" , "password": "test" , "login": "Login"}


r = requests.post(url , data = data )
if "Login incorrect!" in r.text :
	print("incorrect")
else :
	print("success")	
