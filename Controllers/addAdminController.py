
import tkinter
from tkinter import messagebox


from Views import mainGUI
from Controllers import mainController

from connection import connectMySQL
from utils.encryption import Encryption


class AddAdminWindowController():

    def __init__(self):
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()
    
    def cancelCreation(self, window : tkinter.Tk):
        window.destroy()
        mainGUI.MainGUI(mainController.MainWindowController())

    def registerAccountToDatabase(self, firstName, lastName, email, password):
        sql = f"""
        INSERT INTO user (FirstName, LastName, EmailAdd, Password) VALUES (
            %s, %s, %s, %s 
        )
        """
        try:
            self.dbCursor.execute(sql, (firstName, lastName, email, password))
            self.dbConnection.commit()
        finally:
            self.dbConnection.close()
            messagebox.showinfo('Registration Success', 'Admin Account successfully created. You can now use this account to log into the App.')
    
    def inconsistentPasswords(self, password, confirm):
        print(password != confirm)
        return password != confirm
    
    def createAdminAccount(self, data : dict, window: tkinter.Tk):
        firstName = data['firstName']
        lastName = data['lastName']
        email = data['email']
        password = data['password']
        confirmPassword = data['confirmPassword']

        if '' in data.values():
            messagebox.showwarning('Registration Error', 'Please make sure to fill up all the fields.')
            return

        if self.inconsistentPasswords(password, confirmPassword):
            messagebox.showwarning('Registration Error', 'Please make sure your passwords match')
            return 
        
        encryptedPassword = Encryption().encryptPassword(password)
        self.registerAccountToDatabase(firstName, lastName, email, encryptedPassword)
        window.destroy()
        mainGUI.MainGUI(mainController.MainWindowController())