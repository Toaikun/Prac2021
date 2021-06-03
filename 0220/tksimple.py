import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeButton = tk.Button(self, text='Time', command=self.settime)
        self.timeLabel = tk.Label = tk.Label(self, text = "<time>")
        self.quitButton.grid(row = 0, column = 1)
        self.timeButton.grid(row = 0, column = 0)
        self.timeLabel.grid(columnspan = 2)

    def settime(self):
    	self.timeLabel["text"] = time.strftime("%c")

app = Application()
app.master.title('Sample timer application')
app.mainloop()