#!/usr/bin/python this

class SuperClass(object):
	def __init__(self):
		print " this is a super constructor"

	def superMethod(self):
		print " this is a super method"

	if __name__ == '__main__':
		superInstance = SuperClass()
		