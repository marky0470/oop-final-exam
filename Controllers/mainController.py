
import tkinter

from pip import main
from Model.account import Account
from connection import connectMySQL

from Views.editGUI import EditGUI
from Views.addGUI import AddGUI
from Views.deleteGUI import DeleteGUI
from Views.searchGUI import SearchGUI

from Controllers.editController import EditWindowController
from Controllers.addController import AddWindowController
from Controllers.deleteController import DeleteWindowController
from Controllers.searchController import SearchWindowController
#from Model.account import Account

class MainWindowController():

    def __init__(self):
        self.currentData : Account = None

    def getRecords(self):
        dbConnection = connectMySQL()
        dbCursor = dbConnection.cursor()
        dbCursor.execute("SELECT * FROM user")
        sqlResult = dbCursor.fetchall()

        #studentAccounts = list(map(lambda x : Account(x), sqlResult))
        return sqlResult

    def openEditWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        EditGUI(EditWindowController())

    def openAddWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        AddGUI(AddWindowController())

    def openDeleteWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        DeleteGUI(DeleteWindowController())
    
    def openSearchWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        SearchGUI(SearchWindowController())