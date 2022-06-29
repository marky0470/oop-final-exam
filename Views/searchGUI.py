
import tkinter

from Controllers.searchController import SearchWindowController


class SearchGUI():

    def __init__(self, controller : SearchWindowController):
        self.controller = controller

        self.searchWindow = tkinter.Tk()
        self.searchWindow.title('Search Window')

        self.searchWindow.mainloop()

