from model import Model
from view import View

AppModel = Model()
AppView = View(model = AppModel)
AppModel.start(AppView)
AppView.mainloop()