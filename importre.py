#
# Date Aug 2020
# Understanding regular expression
# Understanding named index
#

import re

wrds = "Python language is on the top\n" + "Hello World\n" + "This is top"
print wrds

# search() function
str1 = re.search("^This*", wrds)
str2 = re.search("^This.*top$", wrds)

if str2:
	print "YES! Available"
else:
	print "Try Again!"

# findall() function
str3 = re.findall("on", wrds)
print str3

str4 = re.findall("off", wrds)

if str3:
	print "YES! Avilable"
elif str4:
	print "YES! Available too" 
else:
	print "Try Again!"

# sub() function
str5 = re.sub("\s", "@", wrds, 6)  # substitute first 4 occurence
print str5


# understanding placeholder

tag = 99.9
val = "The price is {} dollars"
print (val.format(tag))

val1 = "The price is {:f} dollars"  # adding ".2" in {:.2f} will give 2 decimal format
print (val1.format(tag))

# Other format() example

chrg = .25
orderno = "345FF4R"
price = 165

val2 = "Please pay {:.3f} dollars for order no {} with {:%} surcharge"
print (val2.format(price, orderno, chrg))

# Example with named index
val3 = "This is {adr}, and the captail is {cap} with pincod {code}."
print (val3.format(adr = "AUS", cap = "Canbera", code = "26000"))

#EOF
