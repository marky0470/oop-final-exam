
import tkinter
from Controllers.editController import EditWindowController


class EditGUI():

    def __init__(self, controller : EditWindowController):
        self.controller = controller

        self.editWindow = tkinter.Tk()
        self.editWindow.title("Edit Window")

        self.editWindow.mainloop()
        