

from Controllers.loginController import LoginWindowController
from widgets.KEntry import KEntry
from widgets.KButton import KButton
from constants import Constants

import tkinter


class LoginGUI():

    def __init__(self, controller : LoginWindowController):
        self.controller = controller

        self.setupWindow()
        self.loginWindow.update()
        self.emailTextVar = tkinter.StringVar()
        self.passwordTextVar = tkinter.StringVar()
        self.setupForm()
        self.setupImage()

        self.loginWindow.mainloop()

    def setupWindow(self):
        self.loginWindow = tkinter.Tk()
        self.loginWindow.title('Login Window')
        self.loginWindow.geometry('840x520')
        self.loginWindow.resizable(False, False)
        self.loginWindow.configure(background=Constants().windowBackgroundColor)
   
    def setupForm(self):
        self.form = tkinter.Frame(
            self.loginWindow,
            background=Constants().windowBackgroundAccentColor,
            width=self.loginWindow.winfo_width() * 0.30,
            height=self.loginWindow.winfo_height()
        )
        self.formHeaderContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor,
        )
        self.formHeader = tkinter.Label(
            self.formHeaderContainer,
            text="Welcome!",
            justify='left',
            foreground=Constants().buttonAccentColor,
            font=("Century Gothic Bold", 24),
            background=Constants().windowBackgroundColor
        )
        self.formHeader2 = tkinter.Label(
            self.formHeaderContainer,
            text="Please Login",
            justify='left',
            foreground=Constants().buttonAccentColor,
            font=("Century Gothic", 12),
            background=Constants().windowBackgroundColor
        )
        self.emailContainer = tkinter.Frame(
            self.form, 
            background=Constants().windowBackgroundColor,
        )
        self.passwordContainer = tkinter.Frame(
            self.form,
            background=Constants().windowBackgroundColor,
        )

        self.emailLabel = tkinter.Label(
            self.emailContainer,
            text='Email Address',
            foreground=Constants().buttonColor,
            background=Constants().windowBackgroundColor
        )
        self.emailEntry = KEntry(
            self.emailContainer,
            height=self.loginWindow.winfo_height() * 0.07,
            width=self.loginWindow.winfo_width() * 0.3,
            background=Constants().entryBackgroundColor,
            textvariable=self.emailTextVar,
            type='text',
            borderColor=Constants().entryBorderColor
        )
        self.passwordLabel = tkinter.Label(
            self.passwordContainer,
            text='Password',
            foreground=Constants().buttonColor,
            background=Constants().windowBackgroundColor,
        )
        self.passwordEntry = KEntry(
            self.passwordContainer,
            height=self.loginWindow.winfo_height() * 0.07,
            width=self.loginWindow.winfo_width() * 0.3,
            background=Constants().entryBackgroundColor,
            textvariable=self.passwordTextVar,
            type='password',
            borderColor=Constants().entryBorderColor
        )

        self.emailLabel.grid(column=0, row=1, padx=35, sticky=tkinter.W)
        self.emailEntry.grid(column=0, row=2, padx=35, sticky=tkinter.NSEW)
        self.passwordLabel.grid(column=0, row=3, padx=35, sticky=tkinter.W)
        self.passwordEntry.grid(column=0, row=4, padx=35, sticky=tkinter.NSEW)

        self.loginButton = KButton(
            self.form,
            text='Login',
            background=Constants().buttonColor,
            onHoverBackground=Constants().buttonAccentColor,
            onClick=lambda : self.controller.login(self.emailTextVar.get(), self.passwordTextVar.get(), self),
            column=0,
            row=4,
            height=self.loginWindow.winfo_height() * 0.08, 
            width=self.loginWindow.winfo_width() * 0.3,
        )


        #self.form.grid(column=0, row=0, padx=10, pady=10, sticky=tkinter.NS)
        self.formHeader.grid(column=0, row=1, sticky=tkinter.W)
        self.formHeader2.grid(column=0, row=2, sticky=tkinter.W)

        self.formHeaderContainer.grid(column=0, row=1, padx=35, pady=35, sticky=tkinter.EW)
        self.emailContainer.grid(column=0, row=2, pady=15, sticky=tkinter.NSEW)
        self.passwordContainer.grid(column=0, row=3, sticky=tkinter.NSEW)
        self.loginButton.grid(column=0, row=4, padx=35, pady=45, sticky=tkinter.EW)
        self.form.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    
    def setupImage(self):
        self.imageContainer = tkinter.Frame(
            self.loginWindow,
            background=Constants().windowBackgroundColor,
            height=self.loginWindow.winfo_height(),
            width=self.loginWindow.winfo_width() * 0.65
        )
        self.imageFile = tkinter.PhotoImage(file='./bg.png')
        self.image = tkinter.Label(
            self.imageContainer,
            background=Constants().windowBackgroundColor,
            image=self.imageFile,
        )

        self.image.place(x=0, y=0, relheight=1, relwidth=1)
        self.imageContainer.pack(side=tkinter.RIGHT)
