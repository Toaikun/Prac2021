import tkinter as tk
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.hint = tk.StringVar()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.input = tk.Text(self)
        self.input.bind("<Motion>", self.showHint)
        self.input.bind("<Enter>", self.color)
        self.input.bind("<KeyPress>", self.color)
        self.input.tag_config('correct', foreground='green')
        self.input.tag_config('incorrect', foreground='red')
        self.drawSpace = tk.Canvas(self, bg="#E4E4E4")
        self.hintLabel = tk.Label(self, textvariable=self.hint)
        self.runButton = tk.Button(self, text='RUN', command=self.run)
        self.clearButton = tk.Button(self, text='CLEAR', command=self.clear)
        self.input.grid(row=0, column=0)
        self.drawSpace.grid(row=0, column=1)
        self.clearButton.grid(row=1, column=0)
        self.runButton.grid(row=1, column=1)
        self.hintLabel.grid(row=2, column=0)
        self.quitButton.grid(row=2,column=1)

    def color(self, event):
        inp = self.input.get("1.0", tk.END).split("\n")
        for i in range(len(inp)):
            if re.match(r"^(oval|rectangle|line|#)", inp[i]) != None:
                self.input.tag_remove('incorrect', str(i+1)+'.0', str(i+1)+'.end')
                self.input.tag_add('correct', str(i+1)+'.0', str(i+1)+'.end')
            else:
                self.input.tag_remove('correct', str(i+1)+'.0', str(i+1)+'.end')
                self.input.tag_add('incorrect', str(i+1)+'.0', str(i+1)+'.end')

    def run(self):
        self.clear()
        figures = ['oval', 'rectangle', 'line']
        inp = self.input.get("1.0", tk.END).split("\n")
        for i, text in enumerate(inp):
            figure, *params = text.split(" ")
            if figure in figures:
                try:
                    eval(f"self.drawSpace.create_{figure}({','.join(params)})")
                    print("!!!!!")
                except:
                    self.input.tag_remove('correct', str(i+1)+'.0', str(i+1)+'.end')
                    self.input.tag_add('incorrect', str(i+1)+'.0', str(i+1)+'.end')
            elif figure != '' and figure[0] == '#':
                self.input.tag_remove('incorrect', str(i+1)+'.0', str(i+1)+'.end')
                self.input.tag_add('correct', str(i+1)+'.0', str(i+1)+'.end')
            else:
                self.input.tag_remove('correct', str(i+1)+'.0', str(i+1)+'.end')
                self.input.tag_add('incorrect', str(i+1)+'.0', str(i+1)+'.end')

    def clear(self):
        for figure in self.drawSpace.find_all():
            self.drawSpace.delete(figure)

    def showHint(self, event):
        xy = self.input.index(tk.CURRENT).split(".")
        x = int(xy[0])-1
        inp = self.input.get("1.0", tk.END).split("\n")
        if re.match(r"^oval", inp[x]) != None:
                self.hint.set("Draw oval: oval x0 y0 x1 y1 outline='color' fill='color' width=width")
        elif re.match(r"^rectangle", inp[x]) != None:
                self.hint.set("Draw rectangle: rectangle x0 y0 x1 y1 outline='color' fill='color' width=width")
        elif re.match(r"^line", inp[x]) != None:
                self.hint.set("Draw line: line x0 y0 x1 y1 fill='color' width=width")   
        elif re.match(r"^#", inp[x]) != None:
                self.hint.set("Comment")
        else:
                self.hint.set("incorrect string")


app = Application()
app.master.title('Events')
app.mainloop()