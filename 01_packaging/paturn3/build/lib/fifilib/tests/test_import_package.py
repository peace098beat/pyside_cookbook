import unittest
import sys

print("*"*79)
for p in sys.path:
	print(p)
print("*"*79)

class TestImport(unittest.TestCase):

	def test_import(self):
		import fifilib

	def test_application(self):
		from fifilib.api import Application

		test_value = 10
		A = Application()
		A.set_value(test_value)
		v = A.get_value()

		self.assertEqual(test_value, v)

if __name__ == '__main__':
	unittest.main()