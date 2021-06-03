import tkinter as tk


class View(tk.Frame):

    def __init__(self, master=None, model=None):
        tk.Frame.__init__(self, master)
        self.model = model

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)


    def createWidgets(self):
        self.aLabel = tk.Label(self, text="a = ")
        self.bLabel = tk.Label(self, text="b = ")
        self.cLabel = tk.Label(self, text="c = ")

        self.aStringVar = tk.StringVar()
        self.bStringVar = tk.StringVar()
        self.cStringVar = tk.StringVar()

        self.aStringVar.set("0")
        self.bStringVar.set("0")
        self.cStringVar.set("0")

        self.answer = tk.StringVar()

        self.aEntry = tk.Entry(self, textvariable=self.aStringVar)
        self.bEntry = tk.Entry(self, textvariable=self.bStringVar)
        self.cEntry = tk.Entry(self, textvariable=self.cStringVar)

        self.solveButton = tk.Button(self, text="Solve", command=self.model.solve)
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.answerLabel = tk.Label(self, text="")

        self.aLabel.grid(row=0, column=0, sticky="NEWS")
        self.aEntry.grid(row=0, column=1, sticky="NEWS")
        self.bLabel.grid(row=0, column=2, sticky="NEWS")
        self.bEntry.grid(row=0, column=3, sticky="NEWS")
        self.cLabel.grid(row=0, column=4, sticky="NEWS")
        self.cEntry.grid(row=0, column=5, sticky="NEWS")
        self.solveButton.grid(row=0, column=6, sticky="NEWS")

        self.answerLabel.grid(row=1, column=0, columnspan=6, sticky="NEWS")
        self.quitButton.grid(row=1, column=6, sticky="NEWS")