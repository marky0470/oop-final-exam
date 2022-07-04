
import tkinter
from Controllers.deleteController import DeleteWindowController
from constants import Constants
from widgets.KButton import KButton

import Views.mainGUI as mainGUI


class DeleteGUI():

    def __init__(self, controller : DeleteWindowController, user):
        self.controller = controller

        self.user = user
        self.setup()
        self.deleteWindow.update()
        self.setupForm()

        self.deleteWindow.mainloop()

    def setup(self):
        self.deleteWindow = tkinter.Tk()
        self.deleteWindow.title("Delete Window")
        self.deleteWindow.geometry("300x170")
        self.deleteWindow.configure(background=Constants().windowBackgroundColor)
        self.deleteWindow.resizable(False,False)

    def setupForm(self):
        self.form = tkinter.Frame(
            self.deleteWindow,
            background=Constants().windowBackgroundAccentColor,
            width=self.deleteWindow.winfo_width(),
            height=self.deleteWindow.winfo_height() * 0.80
        )
        self.promptContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.userInfoContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )
        self.buttonContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor
        )

        self.promptLabel = tkinter.Label(
            self.promptContainer,
            text="Are you sure you want to delete this user?",
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )
        data = self.user
        self.userInfoLabel = tkinter.Label(
            self.promptContainer,
            justify=tkinter.LEFT,
            text=f"First name: {data.firstName}\nLast name: {data.lastName}\nEmail: {data.emailAddress}\nPassword: {data.password}",
            foreground="#000000",
            background=Constants().windowBackgroundColor
        )

        self.confirmButton = KButton(
            self.buttonContainer,
            text='Confirm',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            onClick=lambda : self.controller.deleteEntry(self.user, self.deleteWindow),
            column=1,
            row=0,
            height=self.deleteWindow.winfo_height() * 0.16, 
            width=self.deleteWindow.winfo_width() * 0.3,
        )
        self.cancelButton = KButton(
            self.buttonContainer,
            text='Back',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            onClick=lambda : self.back(),
            column=0,
            row=0,
            height=self.deleteWindow.winfo_height() * 0.16, 
            width=self.deleteWindow.winfo_width() * 0.3,
        )

        self.promptContainer.grid(column=0, row=0)
        self.userInfoContainer.grid(column=0, row=1, pady=7.5)
        self.buttonContainer.grid(column=0, row=2)

        self.promptLabel.grid(column=0, row=0)
        self.userInfoLabel.grid(column=0, row=1)

        self.confirmButton.grid(padx=7.5)
        self.cancelButton.grid(padx=7.5)  

        self.form.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def back(self):
        self.deleteWindow.destroy()
        mainGUI.MainGUI(mainGUI.MainWindowController())
