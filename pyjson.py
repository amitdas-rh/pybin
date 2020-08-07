#
# Date : Aug 2020
# convert a JSON file to py
#

import sys
import json

def conjson():
	# json text
	var = '{ "Country":"Australia", "State":"NSW", "City":"SYD", "License":"NSWXPDDD123" }'
	cvar = json.loads(var)    # parsing to py format
	print(cvar["License"])
	print(cvar["State"])
	print(cvar["Country"])

def conpy():
	# py dictionary
	jvar = {
		"Country": "USA",
		"State": "New York",
		"City": "NY City",
		"License": "NYCFFFDSS9900"
	}
	cjvar = json.dumps(jvar)    # parsing to json format
	print(cjvar)
	
def get_msg():
	print("Enter -j or -p as argument\n")
	print("-j  convert to py\n-p  convert to json")

# user input
if len(sys.argv) > 1:
	upt = str(sys.argv[1])
	#print(+ upt)
 
	if upt == "-j":
		conjson()
	
	elif upt == "-p":
		conpy()

	else:
		get_msg()
else:
	get_msg()
