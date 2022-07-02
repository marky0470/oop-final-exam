
from Controllers.mainController import MainWindowController
from constants import Constants
from widgets.KButton import KButton
from widgets.KEntry import KEntry
from widgets.KTable import KTable
from Model.account import Account

import tkinter


class MainGUI():

    def __init__(self, controller : MainWindowController, loginGUI=None, loginController=None):
        self.controller = controller
        self.loginGUI = loginGUI
        self.loginController= loginController
        self.loggedInAccount = self.controller.getLoggedInAccount()

        self.setup()
        self.mainWindow.update()

        self.searchTextVar = tkinter.StringVar()

        self.buttonWidth = self.mainWindow.winfo_width() * 0.13
        self.buttonHeight = self.mainWindow.winfo_height() * 0.06

        self.setupHeader()
        self.setupNavigation()
        self.setupContent()
        self.mainWindow.mainloop()

    def setup(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("CRUD Main Window")
        self.mainWindow.geometry("1080x620")
        self.mainWindow.configure(background=Constants().windowBackgroundColor)
        self.mainWindow.resizable(False, False)
    
    def __searchButtonCallback(self):
        results = self.controller.searchUser(self.searchTextVar)
        self.dataTable.data = results
        self.dataTable.redraw()
    
    def __resetButtonCallback(self):
        results = self.controller.getRecords()
        self.dataTable.data = results
        self.dataTable.redraw()
    
    def setupHeader(self):
        self.headerFrame = tkinter.Frame(
            self.mainWindow,
            background='white',
            width=self.mainWindow.winfo_width(),
            height=self.mainWindow.winfo_height() * 0.1,
        )

        self.headerTextOne = tkinter.Label(
            self.headerFrame,
            text='User Management System',
            font=('Century Gothic Bold', 14),
            foreground=Constants().buttonColor,
            background='white'
        )

        # self.headerTextTwo = tkinter.Label(
        #     self.headerFrame,
        #     text='Group 9',
        #     font=('Century Gothic Bold', 14),
        #     foreground=Constants().buttonColor,
        #     background='white'
        # )

        self.searchContainer = tkinter.Frame(
            self.headerFrame,
            background='white',
            height=self.mainWindow.winfo_height() * 0.08,
        )

        self.searchEntry = KEntry(
            self.searchContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.searchTextVar,
            type='text',
            borderColor=Constants().entryBorderColor,
            frameColor='white',
            height=self.buttonHeight,
            width=self.mainWindow.winfo_width() * 0.35
        )

        self.searchButton = KButton(
            self.searchContainer,
            text="Search",
            background=Constants().creamButtonColor,
            onHoverBackground=Constants().creamButtonAccentColor,
            column=1,
            row=1,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.__searchButtonCallback,
            textfill=Constants().creamButtonTextColor,
        )

        self.headerTextOne.grid(column=0, row=0, pady=10, padx=15, sticky=tkinter.W)
        # self.headerTextTwo.grid(column=4, row=0, pady=10, padx=15, sticky=tkinter.E)
        
        self.searchContainer.rowconfigure(0, weight=1)
        self.searchContainer.rowconfigure(2, weight=1)
        self.searchEntry.grid(column=0, row=1, sticky=tkinter.NSEW)
        self.searchButton.grid(column=1, row=1, padx=15, sticky=tkinter.NSEW)
        self.searchContainer.grid(column=2, row=0, sticky=tkinter.NSEW)

        self.headerFrame.columnconfigure(1, weight=1)
        self.headerFrame.columnconfigure(1, weight=1)

        self.headerFrame.grid(column=0, row=0, columnspan=2, sticky=tkinter.NSEW)
    
    def setupNavigation(self):
        self.navigationFrame = tkinter.Frame(
            self.mainWindow,
            background='white',
            height=self.mainWindow.winfo_height() * 0.9,
            width=self.mainWindow.winfo_width() * 0.22
        )
        self.navigationFrame.update()
        self.emailLabel = tkinter.Label(
            self.navigationFrame,
            text=self.loggedInAccount.emailAddress,
            background='white',
            font=(Constants().labelFont, 11),
            foreground=Constants().creamButtonTextColor
        )
        self.homeButton = KButton(
            self.navigationFrame,
            text="Home",
            background=Constants().creamButtonColor,
            onHoverBackground=Constants().creamButtonAccentColor,
            column=0,
            row=1,
            height=self.mainWindow.winfo_height() * 0.07,
            width=self.mainWindow.winfo_width() * 0.22,
            type='rect',
            textfill=Constants().creamButtonTextColor
        )
        self.createAdminButton = KButton(
            self.navigationFrame,
            text="Create New Admin",
            background=Constants().whiteButtonColor,
            onHoverBackground=Constants().creamButtonColor,
            column=0,
            row=2,
            height=self.mainWindow.winfo_height() * 0.07,
            width=self.mainWindow.winfo_width() * 0.22,
            type='rect',
            textfill=Constants().creamButtonTextColor
        )
        self.editAccountButton = KButton(
            self.navigationFrame,
            text="Edit Admin Account",
            background=Constants().whiteButtonColor,
            onHoverBackground=Constants().creamButtonColor,
            column=0,
            row=3,
            height=self.mainWindow.winfo_height() * 0.07,
            width=self.mainWindow.winfo_width() * 0.22,
            type='rect',
            textfill=Constants().creamButtonTextColor
        )
        self.deleteThisAccountButton = KButton(
            self.navigationFrame,
            text="Delete Admin Account",
            background=Constants().whiteButtonColor,
            onHoverBackground=Constants().creamButtonColor,
            column=0,
            row=4,
            height=self.mainWindow.winfo_height() * 0.07,
            width=self.mainWindow.winfo_width() * 0.22,
            type='rect',
            textfill=Constants().creamButtonTextColor,
            onClick=lambda: self.controller.deleteThisAdminAccount(self)
        )
        self.logoutButton = KButton(
            self.navigationFrame,
            text="Logout",
            background='white',
            onHoverBackground=Constants().creamButtonColor,
            column=0,
            row=6,
            height=self.mainWindow.winfo_height() * 0.07,
            width=self.mainWindow.winfo_width() * 0.22,
            type='rect',
            textfill=Constants().creamButtonTextColor,
            onClick=lambda : self.controller.logout(self)
        )

        self.emailLabel.grid(column=0, row=0, pady=20, sticky=tkinter.EW)
        self.navigationFrame.grid(column=0, row=1, sticky=tkinter.NSEW)
        self.navigationFrame.rowconfigure(5, weight=1)

    def setupContent(self):
        self.contentFrame = tkinter.Frame(
            self.mainWindow,
            background=Constants().creamButtonColor,
            height=self.mainWindow.winfo_height(),
            width=self.mainWindow.winfo_width() * 0.78
        )

        self.usersText = tkinter.Label(
            self.contentFrame,
            text='Users',
            font=('Century Gothic Bold', 18)
        )
        self.contentFrame.columnconfigure(4, weight=1)
        self.setupButtons()
        self.setupTable()

        self.usersText.grid(column=0, row=0, padx=5, sticky=tkinter.W)
        self.contentFrame.grid(column=1, row=1, sticky=tkinter.NSEW)

    def setupButtons(self):
        self.resetButton = KButton(
            self.contentFrame,
            text="Reset Data",
            background=Constants().whiteButtonColor,
            onHoverBackground=Constants().whiteButtonAccentColor,
            column=1,
            row=0,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=self.__resetButtonCallback,
            textfill=Constants().creamButtonTextColor,
            frameColor=Constants().creamButtonColor,
            type='rounded'
        )
        self.editButton = KButton(
            self.contentFrame,
            text="Edit",
            background=Constants().whiteButtonColor,
            onHoverBackground=Constants().whiteButtonAccentColor,
            column=2,
            row=0,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=lambda : self.controller.openEditWindow(self.mainWindow),
            frameColor=Constants().creamButtonColor,
            textfill=Constants().creamButtonTextColor,
        )
        self.deleteButton = KButton(
            self.contentFrame,
            text="Delete",
            background=Constants().orangeButtonColor,
            onHoverBackground=Constants().orangeButtonAccentColor,
            column=3,
            row=0,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=lambda : self.controller.openDeleteWindow(self.mainWindow)
        )
        
        self.addButton = KButton(
            self.contentFrame,
            text="Create User",
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            column=4,
            row=0,
            height=self.buttonHeight,
            width=self.buttonWidth,
            onClick=lambda : self.controller.openAddWindow(self.mainWindow)
        )

        self.editButton.grid(column=2, row=0, sticky=tkinter.W)
        self.deleteButton.grid(column=3, row=0, padx=10, sticky=tkinter.W)
        self.resetButton.grid(column=1, row=0, padx=10, sticky=tkinter.EW)
        self.addButton.grid(column=5, row=0, padx=15, pady=10, sticky=tkinter.E)

    def setupTable(self):
        self.studentAccounts = self.controller.getRecords()
        self.tableHeaders = Account(None).getColumns()

        self.tableWrapper = tkinter.Frame(
            self.contentFrame,
            height=self.mainWindow.winfo_height() * 0.8,
            background="white"
        )
        self.tableCanvas = tkinter.Canvas(
            self.tableWrapper,
            height=self.mainWindow.winfo_height() * 0.83,
            width=self.mainWindow.winfo_width() * 0.75,
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
            height=self.mainWindow.winfo_height() * 0.83,
            width=self.mainWindow.winfo_width() * 0.8,
            currentData=self.controller.currentData
        )

        self.tableCanvas.bind('<Configure>', lambda e: self.tableCanvas.configure(scrollregion=self.tableCanvas.bbox('all')))

        self.dataTable.pack()
        self.tableCanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand='True')
        self.tableScrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.tableWrapper.grid(column=0, row=3, columnspan=6, padx=10, sticky=tkinter.NSEW)
