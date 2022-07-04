
import sys

from Views import loginGUI
from Views.mainGUI import MainGUI 
from Controllers import loginController
from Controllers.mainController import MainWindowController

from connection import connectMySQL

def isLoggedIn():
    currentLoggedInFile = open('current.txt', 'r')
    return False if currentLoggedInFile.read() == "False" else True

if __name__ == "__main__":

    if isLoggedIn():
        MainGUI(MainWindowController())
        sys.exit()

    loginGUI.LoginGUI(loginController.LoginWindowController())
    sys.exit()
