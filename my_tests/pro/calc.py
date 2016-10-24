

numbers = {}
def sum(numbers):
	try:
		pass
		sum = 0
		keys = numbers.keys()
		for key in keys: 
			num = numbers[key] 
			sum += num 
		return sum 


	except (AttributeError,TypeError): 
		raise ValueError('The provided input is not a dictionary')
	
print sum({"1":30,"2":50,"3":20}) 	
print sum({"1":30}) 
print sum({}) 
print sum(1) 
print sum({"1":30,"2":'50',"3":20})      
	    	
	    	


