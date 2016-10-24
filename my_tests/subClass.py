#!/usr/bin/python 

from superClass import SuperClass 

class Sub(SuperClass): 
	def const(self):
		print " this is a sub-class constructor"

	def subMethod(self):
		print " this is a sub-class method"

sub = Sub()
sub.subMethod()
sub.superMethod()
