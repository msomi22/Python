
import unittest
class CurrentAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.ca = CurrentAccount()
    
  def tearDown(self):
    del self.ca

  def test_current_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.ca, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')
  
  def test_current_account_can_deposit_valid_amounts(self):
    balance = self.ca.deposit(1500)
    self.assertEquals(balance, 1500)
  
  def test_current_account_cannot_withdraw_more_than_current_balance(self):
    message = self.ca.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  
  def test_current_account_can_withdraw_valid_cash_amounts(self):
    self.ca.deposit(23001)
    self.ca.withdraw(437)
    self.assertEquals(self.ca.balance, 22564, msg='Incorrect balance after withdrawal')
    
class SavingsAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.sa = SavingsAccount()
    
  def tearDown(self):
    del self.sa
  
  def test_savings_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')

  def test_savings_account_can_deposit_valid_amounts(self):
    init_balance = self.sa.balance
    balance = self.sa.deposit(1500)
    self.assertEquals(balance, (1500 + init_balance), msg='Balance does not match deposit')

  def test_savings_account_cannot_withdraw_more_than_current_balance(self):
    message = self.sa.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')

  def test_savings_account_can_withdraw_valid_amounts_successfully(self):
    self.sa.deposit(2300)
    self.sa.withdraw(543)
    self.assertEquals(2257, self.sa.balance, msg="Incorrect balance after withdrawal")
 








 

import unittest

class BinaryConverterTestCases(unittest.TestCase):
  def test_conversion_one(self):
    result = binary_converter(0)
    self.assertEqual(result, '0', msg='Invalid conversion')

  def test_conversion_two(self):
    result = binary_converter(62)
    self.assertEqual(result, '111110', msg='Invalid conversion')

  def test_no_negative_numbers(self):
    result = binary_converter(-1)
    self.assertEqual(result, 'Invalid input', msg='Input below 0 not allowed')

  def test_no_numbers_above_255(self):
    result = binary_converter(300)
    self.assertEqual(result, 'Invalid input', msg='Input above 255 not allowed')












manuplate_data([1, -9, 2, 3, 4, -5]) 


import unittest

class ManipulateDataTestCases(unittest.TestCase):
  def test_only_lists_allowed(self):
    result = manipulate_data({})
    self.assertEqual(result, 'Only lists allowed', msg='Invalid argument')

  def test_it_returns_correct_output_with_positives(self):
    result = manipulate_data([1, 2, 3, 4])
    self.assertEqual(result, [4, 0], msg='Invalid output')
    
  def test_returns_correct_ouptut_with_negatives(self):
    result = manipulate_data([1, -9, 2, 3, 4, -5]);
    self.assertEqual(result, [4, -14], msg='Invalid output')





import unittest

class ReplicateIterTestCases(unittest.TestCase):
  def test_it_returns_a_list_of_replicated_numbers(self):
    result = replicate_iter(3, 5)
    self.assertEqual(result, [5, 5, 5], msg='It should produce a list of three fives for the input 3, 5')

  def test_it_returns_an_empty_list_for_0_times(self):
    result = replicate_iter(0, 5)
    self.assertEqual(result,[], msg='It should return an empty list if times == 0')

  def test_it_returns_an_empty_list_for_negative_times(self):
    result = replicate_iter(-1, 20)
    self.assertEqual(result, [], msg='It should return an empty list for negative times.')

  def test_it_raises_value_error_if_invalid_input(self):
    with self.assertRaises(ValueError):
      replicate_iter(1, [])

  def test_it_raises_value_error_if_invalid_number_of_times_to_repeat(self):
    with self.assertRaises(ValueError):
      replicate_iter([], 3)

  def test_it_can_repeat_strings(self):
    result = replicate_iter(3, 'str')
    self.assertEqual(result, ['str', 'str', 'str'], msg='Should replicate strings too')
      
class ReplicateRecurTestCases(unittest.TestCase):
  def test_it_returns_a_list_of_replicated_numbers(self):
    result = replicate_recur(4, 5)
    self.assertEqual(result, [5, 5, 5, 5], msg='It should produce a list of four fives for the input 4, 5')

  def test_it_returns_an_empty_list_for_0_times(self):
    result = replicate_recur(0, 5)
    self.assertEqual(result,[], msg='It should return an empty list if times == 0')

  def test_it_returns_an_empty_list_for_negative_times(self):
    result = replicate_recur(-1, 20)
    self.assertEqual(result, [], msg='It should return an empty list for negative times.')
        
  def test_it_raises_value_error_if_invalid_input(self):
    with self.assertRaises(ValueError):
      replicate_recur(1, [])

  def test_it_raises_value_error_if_invalid_number_of_times_to_repeat(self):
    with self.assertRaises(ValueError):
      replicate_recur([], 3)

















describe('canIWatch tests', function () {
  it('Should return the appropriate message for age less than 6', function () {
    expect(canIWatch(5)).toEqual('You are not allowed to watch Deadpool after 6.00pm.');
  });

  it('Should return the appropriate message for age less than 17', function () {
    expect(canIWatch(15)).toEqual('You must be accompanied by a guardian who is 21 or older.');
  });

  it('Should return the appropriate message for age less than 25', function () {
    expect(canIWatch(20)).toEqual('You are allowed to watch Deadpool, right after you show some ID.');
  });

  it('Should return the appropriate message for age above 25 than 6', function () {
    expect(canIWatch(30)).toEqual('Yay! You can watch Deadpool with no strings attached!');
  });

  it('should return an appropriate message if provided age is invalid', function () {
    expect(canIWatch(-1)).toEqual('Invalid age.');
  });
});