import view
from sqreq import solveSquare

class Model:

	def start(self, view):
		self.view = view

	def solve(self):
		try:
			self.view.answerLabel["text"] = solveSquare(int(self.view.aStringVar.get()),
                                         				int(self.view.bStringVar.get()),
                        				 				int(self.view.cStringVar.get()))
		except Exception as E:
			self.view.answerLabel["text"] = f"{E}"