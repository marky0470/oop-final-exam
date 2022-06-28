
from Controllers.mainController import MainWindowController
from widgets.KButton import KButton

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
        
    def windowPadding(self):
        self.mainWindow.grid_columnconfigure(4, weight=1)

    def setupHeader(self):
        self.header = tkinter.Frame(
            self.mainWindow,
            height=20,
            width=self.mainWindow.winfo_width()
        )
        self.headerText = tkinter.Label(
            self.header,
            text="Basic CRUD Application - Final Examination",
            font=("Verdana", 12),
        )
        self.headerTextSecond = tkinter.Label(
            self.mainWindow,
            justify="right",
            text="Group 9",
            font=("Verdana", 12),
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
        )

        self.addButton.grid(column=1, row=1, padx=10, pady=10, sticky=tkinter.EW)
        self.editButton.grid(column=2, row=1, sticky=tkinter.EW)
        self.deleteButton.grid(column=3, row=1, padx=10, sticky=tkinter.EW)
        self.searchButton.grid(column=5, row=1, padx=10, sticky=tkinter.EW)

    def setupTable(self):
        self.tableFrame = tkinter.Frame(
            self.mainWindow,
            width=self.mainWindow.winfo_width(),
            height=self.mainWindow.winfo_height() * 0.75
        )

        self.tableScrollbar = tkinter.Scrollbar(self.tableFrame)
        #self.tableScrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.tableScrollbar.grid(column=5, row=0, rowspan=10, sticky=tkinter.NSEW)

        """
        """
        self.tableView = tkinter.ttk.Treeview(
            self.tableFrame,
            yscrollcommand=self.tableScrollbar.set,
            xscrollcommand=self.tableScrollbar.set
        )

        self.tableScrollbar.config(command=self.tableView.yview)

        #define our column
        
        self.tableView['columns'] = ('UserID', 'First Name', 'Last Name', 'Email Address', 'Password')

        # format our column
        self.tableView.column("#0", width=0, stretch=tkinter.NO)
        self.tableView.column("UserID",anchor=tkinter.CENTER, stretch=tkinter.YES, width=int(self.mainWindow.winfo_width() * 0.19))
        self.tableView.column("First Name",anchor=tkinter.CENTER, stretch=tkinter.YES, width=int(self.mainWindow.winfo_width() * 0.193))
        self.tableView.column("Last Name",anchor=tkinter.CENTER, stretch=tkinter.YES, width=int(self.mainWindow.winfo_width() * 0.193))
        self.tableView.column("Email Address",anchor=tkinter.CENTER, stretch=tkinter.YES, width=int(self.mainWindow.winfo_width() * 0.193))
        self.tableView.column("Password",anchor=tkinter.CENTER, stretch=tkinter.YES, width=int(self.mainWindow.winfo_width() * 0.193))

        #Create Headings 
        self.tableView.heading("#0",text="",anchor=tkinter.CENTER)
        self.tableView.heading("UserID",text="User ID",anchor=tkinter.CENTER)
        self.tableView.heading("First Name",text="First Name",anchor=tkinter.CENTER)
        self.tableView.heading("Last Name",text="Last Name",anchor=tkinter.CENTER)
        self.tableView.heading("Email Address",text="Email Address",anchor=tkinter.CENTER)
        self.tableView.heading("Password",text="Password",anchor=tkinter.CENTER)

        #add data 
        self.tableView.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        self.tableView.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        self.tableView.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        self.tableView.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        self.tableView.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))
        self.tableView.insert(parent='',index='end',iid=5,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        self.tableView.insert(parent='',index='end',iid=6,text='',
        values=('7','RayRizzo','107','Colorado' , 'Denver'))
        self.tableView.insert(parent='',index='end',iid=7,text='',
        values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
        self.tableView.insert(parent='',index='end',iid=8,text='',
        values=('9','Trink','109','Ohio' , 'Cleveland'))
        self.tableView.insert(parent='',index='end',iid=9,text='',
        values=('10','Twitch','110','Georgia' , 'Duluth'))
        self.tableView.insert(parent='',index='end',iid=10,text='',
        values=('11','Animus','111', 'Connecticut' , 'Hartford'))


        #self.tableView.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.tableView.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.tableFrame.grid(column=1,columnspan=5, row=2, padx=10, pady=10, sticky=tkinter.NSEW)