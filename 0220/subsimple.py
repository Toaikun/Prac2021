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
        self.dateButton = tk.Button(self, text='date', command=self.date)
        self.gitButton = tk.Button(self, text='git', command=self.git)
        self.outputLabel = tk.Label(self, text = "<result>")
        self.dirButton.grid()
        self.gitButton.grid(row = 0, column = 1)
        self.dateButton.grid(row = 0, column = 2)
        self.quitButton.grid(row = 0, column = 3)
        self.outputLabel.grid(row=1, columnspan = 4)

    def dir(self):
    	self.outputLabel["text"] = subprocess.run("dir", capture_output=True).stdout

    def git(self):
        self.outputLabel["text"] = subprocess.run("git", capture_output=True).stdout

    def date(self):
        self.outputLabel["text"] = subprocess.run("date", capture_output=True).stdout

app = Application()
app.master.title('dir/date/git')
app.mainloop()