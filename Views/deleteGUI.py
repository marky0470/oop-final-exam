
import tkinter
from Controllers.deleteController import DeleteWindowController


class DeleteGUI():

    def __init__(self, controller : DeleteWindowController):
        self.controller = controller

        self.deleteWindow = tkinter.Tk()
        self.deleteWindow.title('Delete Window')

        self.deleteWindow.mainloop()
