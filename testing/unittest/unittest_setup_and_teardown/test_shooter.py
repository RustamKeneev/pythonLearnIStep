# setUp() - runs before each test method - запускается перед каждым тестовым методом
# tearDown() - runs after each test method - выполняется после каждого метода тестирования

import unittest
from shooter import Shooter


class ShooterTest(unittest.TestCase):

	mock_data = []

	def test_get_cash(self):
		jake = Shooter('Jake')
		jake.get_cash(500)
		self.assertEqual(jake.money, 1500)
		# print(self.mock_data)

	def test_greet(self):
		jake = Shooter('Jake')
		self.assertEqual(jake.greet(), 'Hello! How are you?')
		jake.money = 50
		self.assertEqual(jake.greet(), 'Hello! I need cash!')

	# def setUp(self):
	# 	self.jake = Shooter('Jake')
	# 	print(self.mock_data)
	# 	self.mock_data = [1, 2, 3, 4, 5]
	#
	# def tearDown(self):
	# 	print(self.mock_data)
	# 	self.mock_data = []




if __name__ == '__main__':
	unittest.main()


