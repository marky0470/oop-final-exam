
import sys

from Views import loginGUI
from Views.mainGUI import MainGUI 
# from Views import adminCreatorGUI
from Controllers import loginController
from Controllers.mainController import MainWindowController
# from Controllers.adminCreatorController import AdminCreatorWindowController

from connection import connectMySQL

def isLoggedIn():
    currentLoggedInFile = open('current.txt', 'r')
    return False if currentLoggedInFile.read() == "False" else True

def withAdminAccount():
    dbConnection = connectMySQL()
    dbCursor = dbConnection.cursor()
    dbCursor.execute("SELECT * FROM user WHERE LastName='Admin' or LastName='admin' or LastName='ADMIN'")
    result = dbCursor.fetchone()
    return result != None

if __name__ == "__main__":
    # if not withAdminAccount():
    #     adminCreatorGUI.AdminCreatorGUI(AdminCreatorWindowController())
    #     sys.exit()

    if isLoggedIn():
        MainGUI(MainWindowController())
        sys.exit()

    loginGUI.LoginGUI(loginController.LoginWindowController())
    sys.exit()
