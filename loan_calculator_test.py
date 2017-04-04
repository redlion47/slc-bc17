import unittest
from loan_calculator import loan_func

class LoanCalculator(unittest.TestCase):
	def test_it_works(self):
		self.assertEqual(loan_func(100000,12,12), 112000, "error")
	def test_lower_month(self):
		self.assertEqual(loan_func(100000,-13,12), "Invalid month")
		pass
	def test_higher_month(self):
		self.assertEqual(loan_func(100000,13,12), "Invalid month")
		pass
	def test_lower_rate_input(self):
		self.assertEqual(loan_func(100000,12,-12), "Invalid Interest Rate")
		pass
	def test_higher_rate_input(self):
		self.assertEqual(loan_func(100000,12,-12), "Invalid Interest Rate")
		pass
	def test_amount_value_exception(self):
		self.assertRaises(ValueError, loan_func("ten", 12,12))
		pass
	def test_time_value_exception(self):
		self.assertRaises(ValueError, loan_func(100000, "twelve",12))
		pass
	def test_rate_value_exception(self):
		self.assertRaises(ValueError, loan_func(100000, 12,"twelve"))
		pass
	def test_amount_input(self):
		self.assertEqual(loan_func(0,12,12), "Enter an amount please")
		pass
		
if __name__ == "__main__":
	unittest.main()


	
