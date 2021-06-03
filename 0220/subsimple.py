import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.dirButton = tk.Button(self, text='dir', command=self.dir)
        self.outputLabel = tk.Label(self, text = "<result>")
        self.dirButton.grid()
        self.quitButton.grid(row = 0, column = 1)
        self.outputLabel.grid(row=1, columnspan = 2)

    def dir(self):
    	self.outputLabel["text"] = subprocess.run("dir", capture_output=True).stdout

app = Application()
app.master.title('dir/date/git')
app.mainloop()