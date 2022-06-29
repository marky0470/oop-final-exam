
from connection import connection
from Model.account import Account

class MainWindowController():

    def __init__(self):
        pass

    def getRecords(self):
        dbCursor = connection.cursor()
        dbCursor.execute("SELECT * FROM students")
        sqlResult = dbCursor.fetchall()

        #studentAccounts = list(map(lambda x : Account(x), sqlResult))
        return sqlResult
