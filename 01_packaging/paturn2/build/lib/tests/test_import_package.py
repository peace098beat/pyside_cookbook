

import unittest
import sys
for p in sys.path:
	print(p)

class TestImport(unittest.TestCase):

	def test_import(self):
		import fifilib
		print(">> test_import")

	def test_application(self):
		from fifilib.api import Application

		test_value = 10
		A = Application()
		A.set_value(test_value)
		v = A.get_value()

		self.assertEqual(test_value, v)

if __name__ == '__main__':
	unittest.main()