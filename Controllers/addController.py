from email import message
from connection import connectMySQL
from tkinter import messagebox
import Views.addGUI
from utils.encryption import Encryption

class AddWindowController():

    def __init__(self):
        pass

    def addEntry(self, fName, lName, email, password):
        if "" in [fName, lName, email, password]:
            messagebox.showwarning("Error", "All entries must be filled in")
            return

        dbConnection = connectMySQL()
        dbCursor = dbConnection.cursor()

        if self.checkExistingEmail(email, dbCursor):
            messagebox.showwarning("Error", "User with this email address already exists")
            return
    
        sql = "INSERT INTO user (FirstName, LastName, EmailAdd, Password) VALUES (%s, %s, %s, %s)"

        encryptedPassword = Encryption().encryptPassword(password)

        dbCursor.execute(sql, (fName, lName, email, encryptedPassword))
        dbConnection.commit()

        dbCursor.close()
        dbConnection.close()

        messagebox.showinfo("Success", f"Successfully added {fName} {lName} to the database")

    def checkExistingEmail(self, email, cursor):
        sql = f"SELECT * FROM user WHERE EmailAdd='{email.strip()}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        return True if result else False






