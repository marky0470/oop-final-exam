
from tkinter import messagebox
from Model.account import Account
from connection import connectMySQL

from Views.mainGUI import MainGUI
from Controllers.mainController import MainWindowController
from utils.encryption import Encryption


class LoginWindowController():

    def __init__(self):
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor(buffered=True)
    
    def withAdminAccount(self):
        self.dbCursor.execute("SELECT * FROM user WHERE LastName='Admin' or LastName='admin' or LastName='ADMIN'")
        result = self.dbCursor.fetchone()
        return result != None

    def login(self, email : str, password : str, window):
        sql = f"SELECT * FROM user WHERE EmailAdd='{email.strip()}'"
        self.dbCursor.execute(sql)
        result = self.dbCursor.fetchone()
        resultingAccount = Account(result)

        if not result:
            messagebox.showwarning("Login Error", "Account not Found")
            return
        
        decryptedAccountPassword = Encryption().decryptPassword(resultingAccount.password.encode()).decode()
        
        if decryptedAccountPassword != password:
            messagebox.showwarning("Login Error", "Incorrect Password")
            return 

        if resultingAccount.lastName not in ['admin', 'ADMIN', 'Admin']:
            messagebox.showwarning("Login Error", "This Account is not an admin account")
            return

        localStorage = open('current.txt', 'w')
        localStorage.write(f'True {resultingAccount.userID}')
        localStorage.close()
        
        self.dbConnection.close()
        window.loginWindow.destroy()
        MainGUI(MainWindowController())


