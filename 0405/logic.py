"""Application logic."""
import tkinter as tk


class Application(tk.Frame):
    """Main application class."""

    def __init__(self, master=None):
        """Create root window."""
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """Create widgets."""
