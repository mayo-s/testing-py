import unittest
from calc import add, subtract, multiply, divide, square, exp_n, sqroot, root_n

class TestCalc(unittest.TestCase):

	# Unit Testing
	def test_add(self):
		result = add(5, 10)
		self.assertEqual(result, 15)

	def test_subtract(self):
		result = subtract(5, 10)
		self.assertEqual(result, -5)

	def test_multiply(self):
		result = multiply(5, 10)
		self.assertEqual(result, 50)

	def test_divide_by_0(self):
		result = divide(10, 0)
		self.assertEqual(result, 'Division by 0 is undefined')

	def test_divide(self):
		result = divide(50, 10)
		self.assertEqual(result, 5)

	def test_square(self):
		result = square(5)
		self.assertEqual(result, 25)

	def test_exp_n(self):
		result = exp_n(5, 3)
		self.assertEqual(result, 125)

	def test_sqroot(self):
		result = sqroot(25);
		self.assertEqual(result, 5)

	def test_sqroot_negative(self):
		result = sqroot(-25);
		self.assertEqual(result, 'Number is undefined')

	def test_root_n_odd(self):
		result = root_n(8, 3)
		self.assertEqual(result, 2)

	def test_root_n_even(self):
		result = root_n(4, 2)
		self.assertEqual(result, 2)

	def test_root_negative_odd_n(self):
		result = root_n(-8, 3)
		self.assertEqual(result, -2)

	def test_root_negative_even_n(self):
		result = root_n(-9, 2)
		self.assertEqual(result, 'Number is undefined')	

	# Manual Testing
	# def test_manual(self):
	# 	print('')
	# 	print('## MANUAL TESTING ##')
	# 	print('add(5, 10): ' + str(add(5, 10)) + ' (expect 15)')
	# 	print('')
	# 	print('subtract(5, 10): ' + str(subtract(5, 10)) + ' (expect -5)')
	# 	print('')
	# 	print('multiply(5, 10): ' + str(multiply(5, 10)) + ' (expect 50)')
	# 	print('')
	# 	print('divide(10, 10): ' + str(divide(10, 10)) + ' (expect 1)')
	# 	print('')
	# 	print('divide(0, 10): ' + str(divide(0, 10)) + ' (expect 0)')
	# 	print('')
	# 	print('divide(10, 0): ' + str(divide(10, 0)) + ' (expect - Division by 0 is undefined -)')
	# 	print('')

if __name__ == '__main__':
	unittest.main()
