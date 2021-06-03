import unittest
from unittest.mock import MagicMock
from model import Model
from sqreq import solveSquare as sqr

class TestMo(unittest.TestCase):

	def setUp(self):
		self.model = Model()
		self.view = MagicMock()
		self.view.answerLabel = {}
		self.model.start(self.view)

	def test_Dgr0(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value="-26")
		self.view.cStringVar.get = MagicMock(return_value="120")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "6.0 20.0")

	def test_Deq0(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value="4")
		self.view.cStringVar.get = MagicMock(return_value="4")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "-2.0")

	def test_Dls0(self):
		self.view.aStringVar.get = MagicMock(return_value="2")
		self.view.bStringVar.get = MagicMock(return_value="1")
		self.view.cStringVar.get = MagicMock(return_value="2")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "∅")

	def test_000(self):
		self.view.aStringVar.get = MagicMock(return_value='0')
		self.view.bStringVar.get = MagicMock(return_value='0')
		self.view.cStringVar.get = MagicMock(return_value='0')
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "∞")

	def test_001(self):
		self.view.aStringVar.get = MagicMock(return_value='0')
		self.view.bStringVar.get = MagicMock(return_value='0')
		self.view.cStringVar.get = MagicMock(return_value="2")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "∅")

	def test_010(self):
		self.view.aStringVar.get = MagicMock(return_value='0')
		self.view.bStringVar.get = MagicMock(return_value="1")
		self.view.cStringVar.get = MagicMock(return_value='0')
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "0.0")

	def test_011(self):
		self.view.aStringVar.get = MagicMock(return_value='0')
		self.view.bStringVar.get = MagicMock(return_value="1")
		self.view.cStringVar.get = MagicMock(return_value="2")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "-2.0")

	def test_100(self):
		self.view.aStringVar.get = MagicMock(return_value="2")
		self.view.bStringVar.get = MagicMock(return_value='0')
		self.view.cStringVar.get = MagicMock(return_value='0')
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "0.0")

	def test_101(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value='0')
		self.view.cStringVar.get = MagicMock(return_value="-4")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "-2.0 2.0")

	def test_110(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value="2")
		self.view.cStringVar.get = MagicMock(return_value='0')
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "-2.0 0.0")

	def test_wronginput1(self):
		self.view.aStringVar.get = MagicMock(return_value="a")
		self.view.bStringVar.get = MagicMock(return_value="b")
		self.view.cStringVar.get = MagicMock(return_value="c")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "invalid literal for int() with base 10: 'a'")

	def test_wronginput2(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value="b")
		self.view.cStringVar.get = MagicMock(return_value="c")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "invalid literal for int() with base 10: 'b'")

	def test_wronginput3(self):
		self.view.aStringVar.get = MagicMock(return_value="1")
		self.view.bStringVar.get = MagicMock(return_value="1")
		self.view.cStringVar.get = MagicMock(return_value="c")
		self.model.solve()
		self.assertEqual(self.view.answerLabel["text"], "invalid literal for int() with base 10: 'c'")


