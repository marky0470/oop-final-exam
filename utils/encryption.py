
from cryptography.fernet import Fernet 

class Encryption():

    def __init__(self):
        self.key = "GS6_tCABEb2_xGePdfglSgMY-GRBzxC1eMAxfgNohCE=".encode() 
        self.cipher = Fernet(self.key)

    def encryptPassword(self, password : str):
        return self.cipher.encrypt(password.encode())
    
    def decryptPassword(self, encryptedPassword : str):
        return self.cipher.decrypt(encryptedPassword)

##### TESTING #####
#print(Encryption().encryptPassword('Francis James'))
#print(Encryption().decryptPassword('gAAAAABivvzw2hyBUGQxu5c-Dke9ZOp88MHi0e3K8g-MHWNwFoBb3pkZ_WgJIHy-cCKb81M5vmCWTzkWTMy3sSYqZ5thySmSeg=='.encode()))
