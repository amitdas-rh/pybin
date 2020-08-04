#
# Date : 4 Aug 2020  
# printing recursion
#

import sys

# funtion for recursion
def get_recur(num):
	if(num > 0):
		result = num + get_recur(num - 1)
		print(result)
	else:
		result = 0
		print(result)
	return result


# message to user input
def get_msg():
	print"\nPlease enter the number "

# type cast to int for input number
if len(sys.argv) > 1:
	anum = int(sys.argv[1])
	get_recur(anum)
else:
	get_msg()

#Sample call
#get_recur(5)
#EOF
