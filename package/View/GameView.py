import tkinter
from tkinter.ttk import Style
from PIL import Image,ImageTk
import package
class GameView(tkinter.Frame):
    
    def __init__(self, parent):
        self.root = tkinter.Frame.__init__(self, parent.root)
        img= (Image.open("images/board.png"))
        resized_image= img.resize((780,780), Image.ANTIALIAS)
        self.image= ImageTk.PhotoImage(resized_image)
        
        self.parent = parent
        self.w = 880
        self.h = 800
        
        print("in")
        self.init()
        # self.showSignUpPage()
        
    def init(self):
        self.parent.geometry(str(self.w) + "x" + str(self.h))
        canvas = tkinter.Canvas(self.root, width=self.w, height=self.h, bg="#3B2314")
        canvas.create_image(self.w - (self.w / 2), self.h - (self.h / 2), image=self.image)
        canvas.place(x=-2,y=0)
        
    