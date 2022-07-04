
from utils.encryption import Encryption


class Account():

    def __init__(self, data):
        self.userID = data[0] if data else ""
        self.firstName = data[1] if data else ""
        self.lastName = data[2] if data else ""
        self.emailAddress = data[3] if data else ""
        self.password = data[4] if data else ""

        if len(self.password) > 20: 
            self.decryptPassword()
    
    def decryptPassword(self):
        decryptedPassword = Encryption().decryptPassword(self.password.encode())
        self.password = decryptedPassword.decode()

    def getColumns(self):
        return ["UserID", "First Name", "Last Name", "Email Address", "Password"]

    def __str__(self):
        return f"{self.userID} - {self.firstName} - {self.lastName} - {self.emailAddress} - {self.password}"
