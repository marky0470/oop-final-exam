
from Controllers.mainController import MainWindowController

import tkinter


class MainGUI():

    def __init__(self, controller : MainWindowController):
        self.controller = controller
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("CRUD Main Window") 
        self.mainWindow.geometry("720x480")
        
        self.mainWindow.mainloop()
