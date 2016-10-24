#!/usr/bin/python 
#super,base,parent class
class Parent:

	parentName = ''

	def __init__(self):
		print " this is the parent constructor"

	def parentFunction(self):
		print " this is a menthod in parent class"

	def setName(self,name):
		Parent.parentName = name
		
	def getName(self):
		print " parent name: ", Parent.parentName


#sub,child class that inherite from parent class
class Child(Parent):
     
     def __init__(self):
     	print " this is the child constructor"

     def childFunction(self):
     	print " this is a method in child class"

c = Child()
c.childFunction()

c.parentFunction()

c.setName("Peter Mwenda")
c.getName()