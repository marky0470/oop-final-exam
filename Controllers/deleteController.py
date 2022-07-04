from connection import connectMySQL
from tkinter import messagebox
from Views import mainGUI
from Controllers import mainController

class DeleteWindowController():

    def __init__(self):
        pass

    def deleteEntry(self, user, window):
        dbConnection = connectMySQL()
        dbCursor = dbConnection.cursor()

        sql = f"DELETE FROM user WHERE UserID='{user.userID}'"

        dbCursor.execute(sql)
        dbConnection.commit()

        dbCursor.close()
        dbConnection.close()

        messagebox.showinfo("Success", f"Successfully deleted {user.firstName} {user.lastName} from the database")
        window.destroy()
        mainGUI.MainGUI(mainController.MainWindowController())