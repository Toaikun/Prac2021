import unittest

from solveSquare import solveSquare

class TestSolveSquare(unittest.TestCase):

	def test_Dgr0(self):
		self.assertEqual(solveSquare(1, -26, 120), (6, 20))

	def test_Deq0(self):
		self.assertEqual(solveSquare(1, 6, 9), (-3, -3))

	def test_Dls0(self):
		self.assertEqual(solveSquare(2, 1, 2), None)