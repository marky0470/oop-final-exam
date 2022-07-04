
import tkinter
from Controllers.editAdminController import EditAdminWindowController

from widgets.KEntry import KEntry
from widgets.KButton import KButton
from constants import Constants


class EditAdminGUI():

    def __init__(self, controller : EditAdminWindowController):
        self.controller = controller

        self.setupWindow()
        self.rootWindow.update()

        self.firstNameTextVar = tkinter.StringVar()
        self.firstNameTextVar.set(self.controller.account.firstName)
        self.lastNameTextVar = tkinter.StringVar()
        self.lastNameTextVar.set(self.controller.account.lastName)
        self.emailAddressTextVar= tkinter.StringVar()
        self.emailAddressTextVar.set(self.controller.account.emailAddress)
        self.passwordTextVar = tkinter.StringVar()
        self.passwordTextVar.set(self.controller.account.password)
        self.newPasswordTextVar = tkinter.StringVar()

        self.setupHeader()
        self.setupForm()
        self.rootWindow.mainloop()
    
    def setupWindow(self):
        self.rootWindow = tkinter.Tk()
        self.rootWindow.title('Create new Admin')
        self.rootWindow.geometry('350x530')
        self.rootWindow.configure(background=Constants().windowBackgroundColor)
        self.rootWindow.resizable(False, False)
    
    def setupHeader(self):
        self.headerFrame = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor
        )
        self.headerText = tkinter.Label(
            self.headerFrame,
            text='Update',
            font=('Century Gothic Bold', 20),
            justify='left',
            foreground=Constants().buttonAccentColor,
            background=Constants().windowBackgroundColor
        )
        self.headerText2 = tkinter.Label(
            self.headerFrame,
            text='Admin Account Information',
            font=('Century Gothic', 10),
            justify='left',
            foreground=Constants().buttonAccentColor,
            background=Constants().windowBackgroundColor
        )

        self.headerText.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.headerText2.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.headerFrame.grid(column=0, row=0, pady=20, sticky=tkinter.NSEW)
    
    def setupFirstNameField(self):
        self.firstNameContainer = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor,
        )
        self.firstNameLabel = tkinter.Label(
            self.firstNameContainer,
            text="First Name",
            background=Constants().windowBackgroundColor,
            font=('Century Gothic', 10),
            foreground=Constants().buttonColor
        )
        self.firstNameEntry = KEntry(
            self.firstNameContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.firstNameTextVar,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.8,
            type="text",
            borderColor=Constants().entryBorderColor
        )

        self.firstNameLabel.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.firstNameEntry.grid(column=0, row=1, padx=35, sticky=tkinter.NSEW)
        self.firstNameContainer.grid(column=0, row=1, sticky=tkinter.NSEW)
    
    def setupLastNameField(self):
        self.lastNameContainer = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor,
        )
        self.lastNameLabel= tkinter.Label(
            self.lastNameContainer,
            text="Last Name",
            font=('Century Gothic', 10),
            background=Constants().windowBackgroundColor,
            foreground=Constants().buttonColor
        )
        self.lastNameEntry = KEntry(
            self.lastNameContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.lastNameTextVar,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.8,
            type="text",
            state='disabled',
            borderColor=Constants().entryBorderColor,
        )

        self.lastNameLabel.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.lastNameEntry.grid(column=0, row=1, padx=35, sticky=tkinter.NSEW)
        self.lastNameContainer.grid(column=0, row=2, pady=10, sticky=tkinter.NSEW)

    def setupEmailAddressField(self):
        self.emailAddressContainer = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor
        )
        self.emailAddressLabel = tkinter.Label(
            self.emailAddressContainer,
            text="Email Address",
            font=('Century Gothic', 10),
            background=Constants().windowBackgroundColor,
            foreground=Constants().buttonColor
        )
        self.emailAddressEntry = KEntry(
            self.emailAddressContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.emailAddressTextVar,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.8,
            type="text",
            borderColor=Constants().entryBorderColor,
        )

        self.emailAddressLabel.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.emailAddressEntry.grid(column=0, row=1, padx=35, sticky=tkinter.NSEW)
        self.emailAddressContainer.grid(column=0, row=3, sticky=tkinter.NSEW)

    def setupPasswordField(self):
        self.passwordContainer = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor
        )
        self.passwordLabel = tkinter.Label(
            self.passwordContainer,
            text="Password",
            font=('Century Gothic', 10),
            background=Constants().windowBackgroundColor,
            foreground=Constants().buttonColor
        )
        self.passwordEntry = KEntry(
            self.passwordContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.passwordTextVar,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.8,
            type="text",
            state='disabled',
            borderColor=Constants().entryBorderColor,
        )

        self.passwordLabel.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.passwordEntry.grid(column=0, row=1, padx=35, sticky=tkinter.NSEW)
        self.passwordContainer.grid(column=0, row=4, pady=10, sticky=tkinter.NSEW)
    
    def setupNewPasswordField(self):
        self.newPasswordContainer = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor
        )
        self.newPasswordLabel = tkinter.Label(
            self.newPasswordContainer,
            text="New Password",
            font=('Century Gothic', 10),
            background=Constants().windowBackgroundColor,
            foreground=Constants().buttonColor
        )
        self.newPasswordEntry = KEntry(
            self.newPasswordContainer,
            background=Constants().entryBackgroundColor,
            textvariable=self.newPasswordTextVar,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.8,
            type="password",
            borderColor=Constants().entryBorderColor,
        )

        self.newPasswordLabel.grid(column=0, row=0, padx=35, sticky=tkinter.W)
        self.newPasswordEntry.grid(column=0, row=1, padx=35, sticky=tkinter.NSEW)
        self.newPasswordContainer.grid(column=0, row=5, sticky=tkinter.NSEW)
    
    def __getData(self):
        return {
            'firstName': self.firstNameTextVar.get(),
            'lastName': self.lastNameTextVar.get(),
            'email': self.emailAddressTextVar.get(),
            'password': self.passwordTextVar.get(),
            'newPassword': self.newPasswordTextVar.get()
        }
    
    def setupButtons(self):
        self.buttonsFrame = tkinter.Frame(
            self.rootWindow,
            background=Constants().windowBackgroundColor
        )
        self.cancelButton = KButton(
            self.buttonsFrame,
            text='Cancel',
            background=Constants().windowBackgroundColor,
            onHoverBackground=Constants().windowBackgroundColor,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.3,
            column=0,
            row=0,
            textfill='red',
            onClick=lambda : self.controller.cancelUpdate(self.rootWindow)
        )
        self.updateButton = KButton(
            self.buttonsFrame,
            text='Update',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            height=self.rootWindow.winfo_height() * 0.07,
            width=self.rootWindow.winfo_width() * 0.5,
            column=1,
            row=0,
            onClick=lambda : self.controller.updateAdminAccount(data=self.__getData(), window=self.rootWindow)
        )

        self.cancelButton.grid(column=0, row=0, sticky=tkinter.W)
        self.updateButton.grid(column=1, row=0, padx=10, sticky=tkinter.E)
        self.buttonsFrame.grid(column=0, row=6, padx=25, pady=20, sticky=tkinter.NSEW)
        
    def setupForm(self):
        self.setupFirstNameField()
        self.setupLastNameField()
        self.setupEmailAddressField()
        self.setupPasswordField()
        self.setupNewPasswordField()

        self.setupButtons()
        
       

        