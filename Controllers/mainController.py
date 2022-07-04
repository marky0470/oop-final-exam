
import tkinter
from tkinter import messagebox
from tkinter.messagebox import askyesno
from Controllers.editAdminController import EditAdminWindowController
from Views import loginGUI
from Controllers import loginController

from Model.account import Account
from Views.editAdminGUI import EditAdminGUI
from connection import connectMySQL

from Views.editGUI import EditGUI
from Views.addGUI import AddGUI
from Views.deleteGUI import DeleteGUI
from Views.addAdminGUI import AddAdminGUI

from Controllers.editController import EditWindowController
from Controllers.addController import AddWindowController
from Controllers.deleteController import DeleteWindowController
from Controllers.addAdminController import AddAdminWindowController

class MainWindowController():

    def __init__(self):
        self.currentData : Account = None
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()
        self.loggedInAccount = None

    def getRecords(self):
        self.dbCursor.execute("SELECT * FROM user where LastName != 'Admin'")
        sqlResult = self.dbCursor.fetchall()

        return sqlResult
    
    def searchUser(self, searchTextVar):
        searchValue = searchTextVar.get()
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
        searchTextVar.set("")
        
        return results
    
    def getLoggedInAccount(self) -> Account:
        localStorage = open('current.txt', 'r')
        data = localStorage.read().split(' ')
        sql = f"SELECT * FROM user WHERE UserID = {int(data[1])}"
        self.dbCursor.execute(sql)
        result = self.dbCursor.fetchone()
        self.loggedInAccount = Account(result)
        return self.loggedInAccount
    
    def deleteThisAdminAccount(self, mainGUI):
        confirm = askyesno("Delete Admin Account", "Are you sure you want to delete this Admin Account? This is not reversible.")

        if confirm:
            sql = f"DELETE FROM user WHERE UserID = {self.loggedInAccount.userID}"
            self.dbCursor.execute(sql)
            self.dbConnection.commit()
            self.dbConnection.close()
            self.logout(mainGUI)
            return

    def openAddAdminWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        AddAdminGUI(AddAdminWindowController())
    
    def openEditAdminWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        EditAdminGUI(EditAdminWindowController(self.loggedInAccount))

    def openEditWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        EditGUI(EditWindowController())

    def openAddWindow(self, mainWindow : tkinter.Tk):
        mainWindow.destroy()
        AddGUI(AddWindowController())

    def openDeleteWindow(self, mainWindow : tkinter.Tk, user):
        if user == None:
            messagebox.showerror("Error", "A user must be selected for this operation")
            return
        mainWindow.destroy()
        DeleteGUI(DeleteWindowController(), user)
    

    def logout(self, mainGUI):
        localStorage = open('current.txt', 'w')
        localStorage.write('False')
        localStorage.close()
        mainGUI.mainWindow.destroy()
        loginGUI.LoginGUI(loginController.LoginWindowController())