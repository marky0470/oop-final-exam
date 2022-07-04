
import tkinter
from tkinter import messagebox
from Model.account import Account


from Views import mainGUI
from Controllers import mainController

from connection import connectMySQL
from utils.encryption import Encryption


class EditAdminWindowController():

    def __init__(self, account : Account):
        self.account = account

        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()
    
    def cancelUpdate(self, window : tkinter.Tk):
        window.destroy()
        mainGUI.MainGUI(mainController.MainWindowController())

    def updateAccountInDatabase(self, firstName, lastName, email, password):
        sql = f"""
        UPDATE user
        SET 
            FirstName=%s,
            LastName=%s,
            EmailAdd=%s,
            Password=%s
        WHERE
            UserID={self.account.userID}
        """
        try:
            self.dbCursor.execute(sql, (firstName, lastName, email, password))
            self.dbConnection.commit()
        finally:
            self.dbConnection.close()
            messagebox.showinfo('Account Updated', 'Admin Account Information successfully updated.')
    
    def inconsistentPasswords(self, password, confirm):
        print(password != confirm)
        return password != confirm
    
    def updateAdminAccount(self, data : dict, window: tkinter.Tk):
        firstName = data['firstName']
        lastName = data['lastName']
        email = data['email']
        password = data['password']
        newPassword = data['newPassword']

        if '' in data.values():
            messagebox.showwarning('Form Error', 'Please make sure to fill up all the fields.')
            return

        # if self.inconsistentPasswords(password, confirmPassword):
        #     messagebox.showwarning('Form Error', 'Please make sure your passwords match')
        #     return 
        
        encryptedPassword = Encryption().encryptPassword(newPassword)
        self.updateAccountInDatabase(firstName, lastName, email, encryptedPassword)
        window.destroy()
        mainGUI.MainGUI(mainController.MainWindowController())