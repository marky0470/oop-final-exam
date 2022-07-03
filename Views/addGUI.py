
from ast import Constant

#from mysqlx import Row
from Controllers.addController import AddWindowController
import Views.mainGUI as mainGUI

from constants import Constants
from widgets.KEntry import KEntry
from widgets.KButton import KButton
import tkinter


class AddGUI():

    def __init__(self, controller : AddWindowController):
        self.controller = controller

        self.setup()
        self.addWindow.update()
        self.fNameTextVar = tkinter.StringVar()
        self.lNameTextVar = tkinter.StringVar()        
        self.emailTextVar = tkinter.StringVar()
        self.passwordTextVar = tkinter.StringVar()        
        self.setupForm()
        self.addWindow.update()

        self.addWindow.mainloop()

    def setup(self):
        self.addWindow = tkinter.Tk()
        self.addWindow.title("Add Window")
        self.addWindow.geometry("300x440")
        self.addWindow.configure(background=Constants().windowBackgroundColor)
        self.addWindow.resizable(False,False)
    
    def windowPadding(self):
        self.addWindow.grid_columnconfigure(4, weight=1)
    
    def setupForm(self):
        self.form = tkinter.Frame(
            self.addWindow,
            background=Constants().windowBackgroundAccentColor,
            width=self.addWindow.winfo_width(),
            height=self.addWindow.winfo_height() * 0.80
        )
        self.addFirstNameContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.addLastNameContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.addEmailContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.addPasswordContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.buttonContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        
        self.addFirstNameLabel = tkinter.Label(
            self.addFirstNameContainer,
            text="First Name",
            font=(Constants().labelFont, 10),
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )
        self.addFirstNameEntry = KEntry(
            self.addFirstNameContainer,
            height=self.addWindow.winfo_height() * 0.07,
            width=self.addWindow.winfo_width() * 0.7,
            background=Constants().entryBackgroundColor,
            textvariable=self.fNameTextVar,
            type='text',
            borderColor=Constants().entryBorderColor
        )

        self.addLastNameLabel = tkinter.Label(
            self.addLastNameContainer,
            text="Last Name",
            font=(Constants().labelFont, 10),
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )
        self.addLastNameEntry = KEntry(
            self.addLastNameContainer,
            height=self.addWindow.winfo_height() * 0.07,
            width=self.addWindow.winfo_width() * 0.7,
            background=Constants().entryBackgroundColor,
            textvariable=self.lNameTextVar,
            type='text',
            borderColor=Constants().entryBorderColor
        )

        self.addEmailLabel = tkinter.Label(
            self.addEmailContainer,
            text="Email",
            font=(Constants().labelFont, 10),
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )
        self.addEmailEntry = KEntry(
            self.addEmailContainer,
            height=self.addWindow.winfo_height() * 0.07,
            width=self.addWindow.winfo_width() * 0.7,
            background=Constants().entryBackgroundColor,
            textvariable=self.emailTextVar,
            type='text',
            borderColor=Constants().entryBorderColor
        )

        self.addPasswordLabel = tkinter.Label(
            self.addPasswordContainer,
            text="Password",
            font=(Constants().labelFont, 10),
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )
        self.addPasswordEntry = KEntry(
            self.addPasswordContainer,
            height=self.addWindow.winfo_height() * 0.07,
            width=self.addWindow.winfo_width() * 0.7,
            background=Constants().entryBackgroundColor,
            textvariable=self.passwordTextVar,
            type='password',
            borderColor=Constants().entryBorderColor
        )

        self.addFirstNameLabel.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.addFirstNameEntry.grid(column=0, row=2, padx=35, sticky=tkinter.NSEW)
        self.addLastNameLabel.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.addLastNameEntry.grid(column=0, row=2, padx=35, sticky=tkinter.NSEW)
        self.addEmailLabel.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.addEmailEntry.grid(column=0, row=2, padx=35, sticky=tkinter.NSEW)
        self.addPasswordLabel.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.addPasswordEntry.grid(column=0, row=2, padx=35, sticky=tkinter.NSEW)

        self.addButton = KButton(
            self.buttonContainer,
            text='Add',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            onClick=lambda : self.controller.addEntry(self.fNameTextVar.get(), self.lNameTextVar.get(), self.emailTextVar.get(), self.passwordTextVar.get(), self.addWindow),
            column=1,
            row=4,
            height=self.addWindow.winfo_height() * 0.08, 
            width=self.addWindow.winfo_width() * 0.3,
        )
        self.cancelButton = KButton(
            self.buttonContainer,
            text='Back',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            onClick=lambda : self.back(),
            column=0,
            row=4,
            
            height=self.addWindow.winfo_height() * 0.08, 
            width=self.addWindow.winfo_width() * 0.3,
        )

        self.addFirstNameContainer.grid(column=0, row=1)
        self.addLastNameContainer.grid(column=0, row=2)
        self.addEmailContainer.grid(column=0, row=3)
        self.addPasswordContainer.grid(column=0, row=4)

        self.buttonContainer.grid(column=0, row=5, pady=30)
        self.addButton.grid(padx=7.5)
        self.cancelButton.grid(padx=7.5)        

        self.form.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    def back(self):
        self.addWindow.destroy()
        mainGUI.MainGUI(mainGUI.MainWindowController())


