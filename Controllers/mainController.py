
from connection import connection

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
        pass

    def getRecords(self):
        dbCursor = connection.cursor()
        dbCursor.execute("SELECT * FROM students")
        sqlResult = dbCursor.fetchall()

        #studentAccounts = list(map(lambda x : Account(x), sqlResult))
        return sqlResult
    
    def openEditWindow(self):
        EditGUI(EditWindowController())

    def openAddWindow(self):
        AddGUI(AddWindowController())

    def openDeleteWindow(self):
        DeleteGUI(DeleteWindowController())
    
    def openSearchWindow(self):
        SearchGUI(SearchWindowController())