
import tkinter
from tkinter import ttk

class KTable(ttk.Frame):

    def __init__(self, parent, headers, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.headers = headers
        self.data = data
        self.draw()

    def drawHeader(self):
        self.headerCanvas = tkinter.Canvas(
            self,
            height=self['height'] * 0.1,
            width=self['width'] * 0.97,
            background="#e3e3e3",
            bd=0,
            highlightthickness=0
        )
        self.headerCanvas.bind("<Button-1>", lambda x: print("click"))

        for idx, val in enumerate(self.headers):
            self.headerCanvas.create_text(
                self['width'] - ((self['width'] // 6) * (5-idx)),
                self['height'] *0.1 * 0.5,
                text=val,
                fill="black",
            )

        #self.headerCanvas.grid(column=0, row=0, sticky=tkinter.EW)
        self.headerCanvas.pack()

    def drawData(self):
        for idx, row in enumerate(self.data):
            dataCanvas = tkinter.Canvas(
                self,
                height=self['height'] * 0.1,
                width=self['width'] * 0.97,
                background= "white" if idx % 2 == 0 else "#f0f0f0",
                bd=0,
                highlightthickness=0
            )
            dataCanvas.bind("<Button-1>", lambda x: print("click"))

            for jdx, val in enumerate(row):
                dataCanvas.create_text(
                    self['width'] - ((self['width'] // 6) * (5-jdx)),
                    self['height'] *0.1 * 0.5,
                    text=val,
                    fill="black",
                )

            #dataCanvas.grid(column=0, row=idx+1, sticky=tkinter.EW)
            dataCanvas.pack()

    # def createScrollbar(self):
    #     self.scrollbar = tkinter.Scrollbar(self, orient=tkinter.VERTICAL, command=self.canvas.yview)
    #     self.scrollbar.pack(side="right", fill="y")

    #     self.canvas.configure(yscrollcommand=self.scrollbar.set)

    def draw(self):
        self.drawHeader()
        self.drawData()
        #self.createScrollbar()

