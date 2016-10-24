#!/usr/bin/python
import uuid
class Employee:

   'An employee object'
    
   def __init__(self,empNo,name,phone,email):
   	self.empNo = empNo
   	self.name = name
   	self.phone = phone
   	self.email = email 

   def setEmpNo(self,empNo):
  	Employee.empNo = empNo

   def getEmpNo(self):
   	print "empNo ", Employee.empNo

   def setName(self,name):
  	Employee.name = name

   def getName(self):
   	print "name ", Employee.name
  	
   def setPhone(self,phone):
  	Employee.phone = phone

   def getPhone(self):
   	print "phone ", Employee.phone
  	
   def setEmail(self,email):
  	Employee.email = email		

   def getEmail(self):
   	print "email ", Employee.email	

   def displayEmployee(self):
    print "uuid: " , uuid.uuid4() , ", empNo: ", self.empNo , ", name: " , self.name , ", phone: " , self.phone , ", email: " , self.email

emp = Employee("100","Peter Mwenda","0718953974","mwendapeter72@gmail.com")
emp.displayEmployee()