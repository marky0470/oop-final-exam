import mysql.connector as mysql
from tkinter import messagebox

def connectMySQL():
    try:
        connection = mysql.connect(
            host="localhost",
            user="cpeoop",
            password="123123",
            port="3306",
            database="mysqldemo"
        )
        return connection
    except:
        messagebox.showwarning("Connection Error", "SQL Connection Error, please contact network administrator")
