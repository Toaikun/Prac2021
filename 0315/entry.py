import tkinter as tk
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        check = self.register(self.check)
        self.str = tk.StringVar()
        self.quitButton = tk.Button(self, text='Quit', command=self.realquit)
        self.inputEntry = tk.Entry(self, textvariable=self.str, validate='all', validatecommand=(check, '%P'))
        self.inputEntry.grid(columnspan = 2)
        self.quitButton.grid(row = 0, column = 2)

    def check(self, text):
        if re.match(r"[+-]?[0-9]*[.,]?[0-9]*$", text):
            return True
        else:
            return False

    def realquit(self):
        if (self.str.get() == '+' or self.str.get() == '-'):
            print(0)
        else:
            print(self.str.get())
        self.master.quit()


app = Application()
app.master.title('Entry only real numbers')
app.mainloop()