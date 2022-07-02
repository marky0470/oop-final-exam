
import tkinter
from Views import loginGUI
from Controllers import loginController

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

class MainWindowController():

    def __init__(self):
        self.currentData : Account = None
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()

    def getRecords(self):
        self.dbCursor.execute("SELECT * FROM user where LastName != 'Admin'")
        sqlResult = self.dbCursor.fetchall()

        return sqlResult
    
    def searchUser(self, searchValue):
        sql = f"""
            SELECT * FROM user 
            WHERE (
                UserId LIKE '%{searchValue}%' OR 
                FirstName LIKE '%{searchValue}%' OR 
                LastName LIKE '%{searchValue}%' OR 
                EmailAdd LIKE '%{searchValue}%'
            ) AND (
                LastName != 'Admin' OR
                LastName != 'ADMIN' OR
                LastName != 'admin'
            )
        """
        self.dbCursor.execute(sql)
        results = self.dbCursor.fetchall()
        
        return results

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
    
    def logout(self, mainGUI):
        localStorage = open('current.txt', 'w')
        localStorage.write('False')
        localStorage.close()
        mainGUI.mainWindow.destroy()
        loginGUI.LoginGUI(loginController.LoginWindowController())