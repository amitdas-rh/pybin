#
# Date : 5 Aug 2020
# py version 2.7
#

# Stop Iterating to proceed

class stopnbr():
	def __iter__(self):
		self.selfy = 1
		return self
	
	# on py version 3
	# def __next__(self): 

	def next(self):   #__next__(self): 
		if self.selfy <= 20:
			nwselfy = self.selfy
			self.selfy += 1
			return nwselfy
		else:
			print("Stopping")
			raise StopIteration

itrnbr = stopnbr()
newitr = iter(itrnbr)

for x in newitr:
	print(x)


# tuble sample

ctuble = ("India", "Russia", "Australia", "Japan")
cit = iter(ctuble)

print(next(cit))
print(next(cit))
print(next(cit))
print(next(cit))


# String Iterate

dstring = "VeryGood"
dit = iter(dstring)

print(next(dit))
print(next(dit))
print(next(dit))
print(next(dit))


for x in ctuble:
	print(x)

for y in dstring:
	print(y) 

# using class

class chknbr():
	def __iter__(self):
		self.a = 1
		return self

	def next(self):
		x = self.a
		self.a += 1
		return x

newnbr = chknbr()
newitr = iter(newnbr)

print(next(newitr))
print(next(newitr))
print(next(newitr))
print(next(newitr))
