
from tkinter import messagebox
import tkinter
from Model.account import Account
from connection import connectMySQL

from Views.mainGUI import MainGUI
from Controllers.mainController import MainWindowController

class LoginWindowController():

    def __init__(self):
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()
    
    def login(self, email : str, password : str, window: tkinter.Tk):
        sql = f"SELECT * FROM user WHERE EmailAdd='{email.strip()}'"
        self.dbCursor.execute(sql)
        result = self.dbCursor.fetchone()
        resultingAccount = Account(result)

        if not result:
            messagebox.showwarning("Login Error", "Account not Found")
            return
        
        if resultingAccount.password != password:
            messagebox.showwarning("Login Error", "Incorrect Password")
            return 

        if resultingAccount.lastName not in ['admin', 'ADMIN', 'Admin']:
            messagebox.showwarning("Login Error", "This Account is not an admin account")
            return

        localStorage = open('current.txt', 'w')
        localStorage.write('True')
        localStorage.close()
        self.dbConnection.close()
        window.destroy()
        MainGUI(MainWindowController())


