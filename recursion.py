#
# Date : 4 Aug 2020  
# printing recursion
#

def get_recur(num):
	if(num > 0):
		result = num + get_recur(num - 1)
		print(result)
	else:
		result = 0
		print(result)
	return result


print("\n\nExample for Recursion")

get_recur(10)
