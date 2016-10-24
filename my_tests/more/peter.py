def calculate_tax(dict):
            try:
                iterating_dict = dict.keys()
                yearlyTax = 0
                for key in iterating_dict:
                    income = dict[key]
                    if income <= 1000:
                        dict[key] = 0 
                    elif income in range(1001,10001):
                        yearlyTax = 0 * 1000
                        yearlyTax += 0.1 * (income - 1000)
                        dict[key] = yearlyTax
                    elif income in range(10001,20201):
                        yearlyTax = 0 * 1000
                        yearlyTax += 0.1 *9000
                        yearlyTax += 0.15 * (income - 10000)
                        dict[key] = yearlyTax
                    elif income in range(20201,30751):
                        yearlyTax = 0 * 1000
                        yearlyTax += 0.1 * 9000
                        yearlyTax += 0.15 * 10200
                        yearlyTax += 0.20 * (income - 20200)
                        dict[key] = yearlyTax
                    elif income in range(30751,50001):
                        yearlyTax = 0 * 1000
                        yearlyTax += 0.1 * 9000
                        yearlyTax += 0.15 * 10200
                        yearlyTax += 0.20 * 10550
                        yearlyTax += 0.25 * (income - 30750)
                        dict[key] = yearlyTax
                    elif income > 50000:
                        yearlyTax = 0 * 1000
                        yearlyTax += 0.1 * 9000
                        yearlyTax += 0.15 * 10200
                        yearlyTax += 0.20 * 10550
                        yearlyTax += 0.25 * 19250
                        yearlyTax += 0.3 * (income - 50000)
                        dict[key] = yearlyTax
                print dict 
                return dict
            except (AttributeError,TypeError):
                raise ValueError('The provided input is not a dictionary')

calculate_tax({"Peter":20500.0,"Mwenda":43000,"Kendi":'200'})
#calculate_tax({"Peter":15352.5})
#calculate_tax({})
#calculate_tax(1)
#calculate_tax({"Peter"})                