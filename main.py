
from Controllers.loginController import LoginWindowController
from Views.loginGUI import LoginGUI
from Views.mainGUI import MainGUI 
from Controllers.mainController import MainWindowController

def isLoggedIn():
    currentLoggedInFile = open('current.txt', 'r')
    return False if currentLoggedInFile.read() == "False" else True

if __name__ == "__main__":
    if isLoggedIn():
        MainGUI(MainWindowController())
    else:
        LoginGUI(LoginWindowController())
