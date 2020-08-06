#
# Date 6th Aug 2020
# Super() format differnt in py2.7 
# Class code for experiment.
#

class MyClass:
	x = 5

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfun(self):
        	print("Hello the Name is " + self.name)

p1 = MyClass()
p2 = Person("Rav", 22)

p2.myfun()
print(p2.name)
print(p2.age)
print(p1.x)

#
# Humman code for verification
#

class Human():
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname


class Freshman(Human):
	def __init__(self, fname, lname, year):
		super(Freshman, self).__init__(fname, lname, year)    # super format mistake
		self.year = year

	def examl(self):
		print("Exam for ", self.fname, self.lname, "for ths year")


x = Freshman("Rav", "Holo", "2020")
x.examl()		
