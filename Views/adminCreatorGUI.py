
import tkinter


class AdminCreatorGUI():

    def __init__(self):

        self.setupWindow()
        self.rootWindow.mainloop()
    
    def setupWindow(self):
        self.rootWindow = tkinter.Tk()
        self.rootWindow.title('Admin Creator GUI')
        self.rootWindow.geometry('480x350')