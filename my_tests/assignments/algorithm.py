#!/usr/bin/python


def binary_converter(maxno):
    try:
        if maxno in range(0, 255):
            binary = 0
            binary = bin(maxno)[2:]
            if binary is None:
                raise TypeError
            else:
                return binary
        else:
            return 'Invalid input'
    except TypeError:
        return ValueError('Input is invalid')


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

if __name__ == '__main__':
     unittest.main()
    