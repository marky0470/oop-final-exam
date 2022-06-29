
from Controllers.mainController import MainWindowController
from widgets.KButton import KButton
from widgets.KTable import KTable
from Model.account import Account

import tkinter


class MainGUI():

    def __init__(self, controller : MainWindowController):
        self.controller = controller

        self.setup()
        self.mainWindow.update()

        self.buttonWidth = self.mainWindow.winfo_width() * 0.15
        self.buttonHeight = self.mainWindow.winfo_height() * 0.08
        self.buttonColor = "#e3e3e3"
        self.buttonAccentColor = "#d5d1e0"

        self.windowPadding()

        self.setupHeader()
        self.setupButtons()
        self.setupTable()
        self.mainWindow.mainloop()

    def setup(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("CRUD Main Window")
        self.mainWindow.geometry("940x480")
        self.mainWindow.configure(background="white")

    def windowPadding(self):
        self.mainWindow.grid_columnconfigure(4, weight=1)

    def setupHeader(self):
        self.header = tkinter.Frame(
            self.mainWindow,
            height=20,
            background="white",
            width=self.mainWindow.winfo_width()
        )
        self.headerText = tkinter.Label(
            self.header,
            text="Basic CRUD Application - Final Examination",
            font=("Verdana", 12),
            foreground="black",
            background="white",
        )
        self.headerTextSecond = tkinter.Label(
            self.mainWindow,
            justify="right",
            text="Group 9",
            font=("Verdana", 12),
            foreground="black",
            background="white",
        )
        self.headerText.grid(column=0, row=0, padx=10, pady=5, sticky=tkinter.EW)
        self.headerTextSecond.grid(column=5, row=0, padx=10, sticky=tkinter.EW)
        self.header.grid(column=0, row=0, columnspan=6, sticky=tkinter.EW)

    def setupButtons(self):
        self.addButton = KButton(
            self.mainWindow,
            text="Add",
            background=self.buttonColor,
            onHoverBackground=self.buttonAccentColor,
            column=1,
            row=1,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.controller.openAddWindow
        )
        self.editButton = KButton(
            self.mainWindow,
            text="Edit",
            background=self.buttonColor,
            onHoverBackground=self.buttonAccentColor,
            column=2,
            row=1,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.controller.openEditWindow
        )
        self.deleteButton = KButton(
            self.mainWindow,
            text="Delete",
            background=self.buttonColor,
            onHoverBackground=self.buttonAccentColor,
            column=3,
            row=1,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.controller.openDeleteWindow
        )
        self.searchButton = KButton(
            self.mainWindow,
            text="Search",
            background=self.buttonColor,
            onHoverBackground=self.buttonAccentColor,
            column=4,
            row=1,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.controller.openSearchWindow
        )

        self.addButton.grid(column=1, row=1, padx=10, pady=10, sticky=tkinter.EW)
        self.editButton.grid(column=2, row=1, sticky=tkinter.EW)
        self.deleteButton.grid(column=3, row=1, padx=10, sticky=tkinter.EW)
        self.searchButton.grid(column=5, row=1, padx=10, sticky=tkinter.EW)

    def setupTable(self):
        self.studentAccounts = self.controller.getRecords()
        self.tableHeaders = Account(None).getColumns()

        self.dataTable = KTable(
            self.mainWindow,
            headers=self.tableHeaders,
            data=self.studentAccounts,
            height=self.mainWindow.winfo_height() * 0.8,
            width=self.mainWindow.winfo_width() * 0.99,
        )

        self.dataTable.grid(column=1, row=3, columnspan=6, padx=10, sticky=tkinter.NSEW)
