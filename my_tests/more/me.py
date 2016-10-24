def calculate_tax(dict = {}): 
  try:
      yearlyTax = 0
      income = 0
      name = ''
      empDict = {}
      for key, value in dict.items(): 
         name = key
         income = value

         if(income >= 50000):
            yearlyTax = (income - 50000) * 0.3
            yearlyTax += (50000 - 30750) * 0.25
            yearlyTax += (30750 - 20200) * 0.2 
            yearlyTax += (20200 - 10000) * 0.15
            yearlyTax += (10000 - 1000) * 0.1
          
         if(income < 50000 and income > 30750):
            yearlyTax = (income - 30750) * 0.25
            yearlyTax += (30750 - 20200) * 0.2 
            yearlyTax += (20200 - 10000) * 0.15
            yearlyTax += (10000 - 1000) * 0.1
         
         if(income < 30750 and income > 20200):
            yearlyTax = (income - 20200) * 0.2 
            yearlyTax += (20200 - 10000) * 0.15
            yearlyTax += (10000 - 1000) * 0.1
          
         if(income < 20200 and income > 10000):
            yearlyTax = (income - 10000) * 0.15
            yearlyTax += (10000 - 1000) * 0.1
         
         if(income < 10000 and income > 1000): 
            yearlyTax = (income - 1000) * 0.1
         
         if(income < 1000 and income > 0): 
            yearlyTax = 0
         
         empDict.update({name:yearlyTax}) 
      print empDict 
      return empDict
  except (AttributeError,TypeError):
    raise ValueError("Invalid input of type int not allowed") 
  

calculate_tax({"James": 20500, "Mary": 500, "Evan": 70000})
#calculate_tax({"Peter":20500.0,"Mwenda":43000,"Kendi":'200'})
#calculate_tax({"Peter":15352.5})
calculate_tax({})
#calculate_tax(1)
#calculate_tax({"Peter"})    