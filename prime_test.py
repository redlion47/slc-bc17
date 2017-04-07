import unittest
from prime_numbers import prime_no

class LoanCalculator(unittest.TestCase):
	def test_negative_input(self):
		self.assertEqual(prime_no(-9), "invalid input")
	def test_zero_input(self):
		self.assertEqual(prime_no(0), "invalid input")
	def test_working(self):
		self.assertEqual(prime_no(9), [2, 3, 5, 7] , "Code Error")
	def test_output_type(self):
		self.assertEqual(type(prime_no(9))==list,True, "type Error")
	def test_input_type(self):
		self.assertEqual(prime_no(20.6), "invalid input type")
		
if __name__ == "__main__":
	unittest.main()
