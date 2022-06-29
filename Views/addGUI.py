
from Controllers.addController import AddWindowController

import tkinter


class AddGUI():

    def __init__(self, controller : AddWindowController):
        self.controller = controller

        self.addWindow = tkinter.Tk()
        self.addWindow.title("Add Window")

        self.addWindow.mainloop()