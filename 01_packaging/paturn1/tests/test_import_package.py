

import unittest


class TestImport(unittest.TestCase):

	def test_import(self):
		import ffp2
		print(">> test_import")

	def test_application(self):
		from ffp2.api import Application

		test_value = 10
		A = Application()
		A.set_value(test_value)
		v = A.get_value()

		self.assertEqual(test_value, v)
	