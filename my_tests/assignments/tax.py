
def calculate_tax(peoplelist = {}):
        while True:
            try:
                iterating_peoplelist = peoplelist.keys()
                for key in iterating_peoplelist:
                    earning = peoplelist[key]
                    mytax = 0
                    if earning <= 1000:
                        peoplelist[key] = 0 
                    elif earning in range(1001,10001):
                        mytax = 0 * 1000
                        mytax += 0.1 * (earning - 1000)
                        peoplelist[key] = mytax
                    elif earning in range(10001,20201):
                        mytax = 0 * 1000
                        mytax += 0.1 *9000
                        mytax += 0.15 * (earning - 10000)
                        peoplelist[key] = mytax
                    elif earning in range(20201,30751):
                        mytax = 0 * 1000
                        mytax += 0.1 * 9000
                        mytax += 0.15 * 10200
                        mytax += 0.20 * (earning - 20200)
                        peoplelist[key] = mytax
                    elif earning in range(30751,50001):
                        mytax = 0 * 1000
                        mytax += 0.1 * 9000
                        mytax += 0.15 * 10200
                        mytax += 0.20 * 10550
                        mytax += 0.25 * (earning - 30750)
                        peoplelist[key] = mytax
                    elif earning > 50000:
                        mytax = 0 * 1000
                        mytax += 0.1 * 9000
                        mytax += 0.15 * 10200
                        mytax += 0.20 * 10550
                        mytax += 0.25 * 19250
                        mytax += 0.3 * (earning - 50000)
                        peoplelist[key] = mytax
                return peoplelist
                break
            except (AttributeError,TypeError):
                raise ValueError('Invalid input of type int not allowed')



from unittest import TestCase

class CalculateTaxTests(TestCase):
  def test_it_calculates_tax_for_one_person(self):
    result = calculate_tax({"James": 20500})
    self.assertEqual(result, {"James": 2490.0}, msg="Should return {'James': 2490.0} for the input {'James': 20500}")

  def test_it_calculates_tax_for_several_peoplelist(self):
    income_input = {"James": 20500, "Mary": 500, "Evan": 70000}
    result = calculate_tax(income_input)
    self.assertEqual({"James": 2490.0, "Mary": 0, "Evan": 15352.5}, result,
      msg="Should return {} for the input {}".format(
            {"James": 2490.0, "Mary": 0, "Evan": 15352.5},
            {"James": 20500, "Mary": 500, "Evan": 70000}
      )
    )

  def test_it_does_not_accept_integers(self):
    with self.assertRaises(ValueError) as context:
      calculate_tax(1)
      self.assertEqual(
        "The provided input is not a dictionary.",
        context.exception.message, "Invalid input of type int not allowed"
      )
        
  def test_calculated_tax_is_a_float(self):
    result = calculate_tax({"Jane": 20500})
    self.assertIsInstance(
      calculate_tax({"Jane": 20500}), dict, msg="Should return a result of data type dict")
    self.assertIsInstance(result["Jane"], float, msg="Tax returned should be an float.")

  def test_it_returns_zero_tax_for_income_less_than_1000(self):
    result = calculate_tax({"Jake": 100})
    self.assertEqual(result, {"Jake": 0}, msg="Should return zero tax for incomes less than 1000")

  def test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric(self):
    with self.assertRaises(ValueError, msg='Allow only numeric input'):
      calculate_tax({"James": 2490.0, "Kiura": '200', "Kinuthia": 15352.5})

  def test_it_return_an_empty_dict_for_an_empty_dict_input(self):
    result = calculate_tax({})
    self.assertEqual(result, {}, msg='Should return an empty dict if the input was an empty dict')
if __name__ == '__main__':
    unittest.main()  
     
    
    