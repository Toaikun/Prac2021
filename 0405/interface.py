"""Application interface."""
import tkinter as tk
from logic import Application


class App(Application):
    """Main application class."""

    def createWidgets(self):
        """Widgets."""
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        optionList = ('One', 'Two', 'Three')
        self.choice = tk.StringVar()
        self.choice.set(optionList[0])
        self.input = tk.StringVar()
        check = self.register(self.check)
        self.inputEntry = tk.Entry(self, textvariable=self.input,
                                   validate='all',
                                   validatecommand=(check, '%P'))
        self.optionButton = tk.OptionMenu(self, self.choice, *optionList)
        self.insertButton = tk.Button(self, text="Insert", command=self.insert)
        self.showButton = tk.Button(self, text="Show", command=self.show)
        self.textLabel = tk.Label(self, text="Default")
        self.textLabel.bind('<Enter>', self.enter)
        self.textLabel.bind('<Leave>', self.leave)
        self.inputEntry.grid(columnspan=2)
        self.insertButton.grid(row=1)
        self.optionButton.grid(row=1, column=1)
        self.showButton.grid(row=2)
        self.textLabel.grid(row=2, column=1)
        self.quitButton.grid(row=3, columnspan=2)

    def insert(self):
        """Insert button."""
        inp = self.input.get()
        add = self.choice.get()
        if self.check(inp+add):
            self.input.set(inp + add)

    def show(self):
        """Show button."""
        self.textLabel["text"] = self.input.get()

    def check(self, text):
        """Entry validator."""
        if len(text) <= 10:
            return True
        else:
            return False

    def enter(self, event):
        """Enter event."""
        self.textLabel["text"] = "Hi Mouse"

    def leave(self, event):
        """Leave event."""
        self.textLabel["text"] = "Bye Mouse"


app = App()
app.master.title('Events')
app.mainloop()
