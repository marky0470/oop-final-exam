from connection import connectMySQL
from tkinter import messagebox
import Views.addGUI

class AddWindowController():

    def __init__(self):
        pass

    def addEntry(self, fName, lName, email, password):
        if "" in [fName, lName, email, password]:
            messagebox.showwarning("Error", "All entries must be filled in")
            return

        sqlConnection = connectMySQL()
        sqlCommand = "INSERT INTO user (FirstName, LastName, EmailAdd, Password) VALUES (%s, %s, %s, %s)"
        sqlValues = (fName, lName, email, password)

        sqlCursor = sqlConnection.cursor()
        sqlCursor.execute(sqlCommand, sqlValues)
        sqlConnection.commit()

        sqlCursor.close()
        sqlConnection.close()

        messagebox.showinfo("", f"Successfully added {fName} {lName} to the database")

