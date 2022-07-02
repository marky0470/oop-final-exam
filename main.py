
import sys

from Views.loginGUI import LoginGUI
from Views.mainGUI import MainGUI 
from Views.adminCreatorGUI import AdminCreatorGUI
from Controllers.loginController import LoginWindowController
from Controllers.mainController import MainWindowController
from Controllers.adminCreatorController import AdminCreatorWindowController

from connection import connectMySQL

def isLoggedIn():
    currentLoggedInFile = open('current.txt', 'r')
    return False if currentLoggedInFile.read() == "False" else True

def withAdminAccount():
    dbConnection = connectMySQL()
    dbCursor = dbConnection.cursor()
    dbCursor.execute("SELECT * FROM user WHERE LastName='Admin' or LastName='admin' or LastName='ADMIN'")
    result = dbCursor.fetchone()
    dbConnection.close()
    return result != None

if __name__ == "__main__":
    if not withAdminAccount():
        AdminCreatorGUI(AdminCreatorWindowController())
        sys.exit()

    if isLoggedIn():
        MainGUI(MainWindowController())
        sys.exit()

    LoginGUI(LoginWindowController())
    sys.exit()
