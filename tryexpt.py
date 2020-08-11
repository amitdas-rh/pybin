#
# Date Aug 2020
# Try exception sample
#

# v = 500
rx = -256

# try exception block

try:
 print(v)
except NameError:
 print("Val v is not defined")
except:
 print("Other errors")
else:
 print("No error seen")
finally:
 print("Blocked is finished")

# open file with write mode on

try:
 f = open('tmpv.txt', 'w')
 print "File created"
 f.write("Abra kaa dabraa")
except:
 print("Error Raised")
finally:
 f.close()

# Raise exception
'''if rx < 0:
 raise Exception("Value is -ve")'''

# User input for division and exception

try:
 print("Inside try block")
 num1 = int(input("Enter a Numerator: "))
 num2 = int(input("Enter another Denominator: "))
 val = num1/num2
except ZeroDivisionError:
 print("Error ZeroDivisionError block")
 print(">>Denominator 0 is not acceptable")
else:
 print ("Inside else block")
 vprint = "{} divided by {} = {:.2f}"
 print (vprint.format(num1, num2, val))
finally:
 print ("Reseting numerator and demoniator value.")
 num1 = 0
 num2 = 0

print ("Out of all blocks.")

#EOF
