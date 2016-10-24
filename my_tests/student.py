#!/usr/bin/python 

class Student:

	'Base class for all students'

	studentCount = 0

	def __init__(self,name,age):
		self.name = name
		self.age = age 
		Student.studentCount += 1 

	def showCount(self):	
		print "Total students %d " % Student.studentCount


	def displayStudent(self):
		print "Name: ", self.name, ", Age: ", self.age


student1 = Student("Peter Mwenda",26) 
student1.displayStudent()
print "Total students %d " % Student.studentCount