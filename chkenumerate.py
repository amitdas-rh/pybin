#
# Understanding Enumerate
# Date: Sep 29 2020
#

vlist = ['red', 'blue', 'green', 'black', 'megenta', 'purple']
enu_vlist = enumerate(vlist)
enu_vlist10 = enumerate(vlist, 10)

for counter, value in enu_vlist:
      #	print counter, value		#py2.7
	print (counter, value)		#py3

print('\n')
for counter, value in enu_vlist10:
	print (counter, value)

print('\n')
for counter, value in enumerate(vlist, 20):
	print (counter, value)

print('\n')
for c, v in enumerate(vlist, 100):
	if (c % 2 == 0):
		print (c, v, " ~> even")
	else:
		print (c, v, " ~> odd") 

