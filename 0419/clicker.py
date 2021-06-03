import tkinter as tk
import gettext

gettext.install("clicker", ".", names=("ngettext", ))

click = 0

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)


    def createWidgets(self):
        self.counter = tk.StringVar()
        self.counter.set(_("0 times clicked"))
        self.quitButton = tk.Button(self, text=_('Quit'), command=self.quit)
        self.pressButton = tk.Button(self, text=_('Press Me'), command=self.clicker)
        self.countLabel = tk.Label(self, textvariable=self.counter)
        self.pressButton.grid(sticky="NEWS")
        self.quitButton.grid(row=0, column=1, sticky="NEWS")
        self.countLabel.grid(row=1, columnspan=2, sticky="NEWS")

    def clicker(self):
        global click
        click += 1
        self.counter.set(ngettext("%d time clicked", "%d times clicked", click) % (click, ))

app = Application()
app.master.title(_('Clicker counter'))
app.mainloop()