#
# Date Aug 2020
# File handling
#

import os

# Filename input function

def filenm():
	global tmpv
	# tmpv = input("Enter FileName: ")     # py format in v3.6 
	tmpv =  raw_input("Enter FileName: ")  # py format in v2.7 
		
# reading txt file

def rdin():
	f = open(tmpv, "w+")
	for ix in range(10):
		f.write("Intitial line:" + str(ix) + "\n")
	f.close()

#f1 = open("tmpv.txt","r")
#f2 = open("tmpv.txt","r")
#print(f2.read(10))
#print(f3.readline())

# writing text file

def ltin():
	i = 0
	f1 = open(tmpv, "r")
	for line in f1:
		print("In loop: " + str(i) + " " + line)
		#print(line)
		i += 1
	f1.close()

# appending lines

def apndin():
	f2 = open(tmpv,"a+")
	for apnd in range(2):
		f2.write("Appending lines: " + str(apnd) + "\n")
	f2.close()

# deleting file

def delin():
	del_tmpv = raw_input("Re-enter filename to delete: ")   # py raw_input() format in v2.7
	if os.path.exists(del_tmpv):
		if del_tmpv == tmpv:
			os.remove(del_tmpv)
			print("File deleted")
		else:
			print("Created file " + tmpv  + " and delete file " + del_tmpv + " are not matching.")
	else:
		print("File " + del_tmpv + " doesnot exist")

filenm()	
rdin()
apndin()
ltin()

# deleting request by user:wq

if raw_input("Press 'y' to delete the file :") == 'y':
	delin()
else:
	pass

#f2.close()
#f3.close()
#f.close()
