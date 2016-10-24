#!/usr/bin/python
def manipulate_data(mylist=[]):
    try:
        if type(mylist) is list:
            newlist = []
            sums = 0
            count = 0
            for ints in mylist:
                if ints >= 0:
                    count += 1
                if ints < 0:
                    sums += ints
            newlist.insert(0, count)
            newlist.insert(1, sums)
            return newlist
        else:
            return 'Only lists allowed'
    except (AttributeError, TypeError):
        return 'Input is invalid'


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

if __name__ == '__main__':
     unittest.main()   
   
     