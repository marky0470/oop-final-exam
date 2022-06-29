
from turtle import back
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

        self.buttonWidth = self.mainWindow.winfo_width() * 0.13
        self.buttonHeight = self.mainWindow.winfo_height() * 0.07
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
        self.mainWindow.geometry("1000x520")
        self.mainWindow.configure(background="white")
        self.mainWindow.resizable(False, False)

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
            onClick=lambda : self.controller.openAddWindow(self.mainWindow)
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
            onClick=lambda : self.controller.openEditWindow(self.mainWindow)
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
            onClick=lambda : self.controller.openDeleteWindow(self.mainWindow)
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
            onClick=lambda : self.controller.openSearchWindow(self.mainWindow)
        )

        self.addButton.grid(column=1, row=1, padx=10, pady=10, sticky=tkinter.EW)
        self.editButton.grid(column=2, row=1, sticky=tkinter.EW)
        self.deleteButton.grid(column=3, row=1, padx=10, sticky=tkinter.EW)
        self.searchButton.grid(column=5, row=1, padx=10, sticky=tkinter.EW)

    def setupTable(self):
        self.studentAccounts = self.controller.getRecords()
        self.tableHeaders = Account(None).getColumns()

        self.tableWrapper = tkinter.Frame(
            self.mainWindow,
            height=self.mainWindow.winfo_height() * 0.8,
            background="white"
        )
        self.tableCanvas = tkinter.Canvas(
            self.tableWrapper,
            height=self.mainWindow.winfo_height() * 0.8,
            width=self.mainWindow.winfo_width() * 0.96,
            bd=0,
            highlightthickness=0 
        )
        self.tableScrollbar = tkinter.Scrollbar(self.tableWrapper, command=self.tableCanvas.yview)
        self.tableCanvas.configure(yscrollcommand=self.tableScrollbar.set)

        self.interior = tkinter.Frame(self.tableCanvas, height=self.mainWindow.winfo_height() * 0.8)
        self.tableCanvas.create_window(0, 0, window=self.interior, anchor=tkinter.NW)

        self.dataTable = KTable(
            self.interior,
            headers=self.tableHeaders,
            data=self.studentAccounts,
            height=self.mainWindow.winfo_height() * 0.8,
            width=self.mainWindow.winfo_width(),
            currentData=self.controller.currentData
        )

        self.tableCanvas.bind('<Configure>', lambda e: self.tableCanvas.configure(scrollregion=self.tableCanvas.bbox('all')))

        self.dataTable.pack()
        self.tableCanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand='True')
        self.tableScrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.tableWrapper.grid(column=0, row=3, columnspan=6, padx=10, sticky=tkinter.NSEW)
