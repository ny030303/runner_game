import tkinter
from tkinter.ttk import Style
from PIL import Image,ImageTk
import package
class MainView(tkinter.Frame):
    
    def __init__(self, parent):
        self.root = tkinter.Frame.__init__(self, parent.root)
        img= (Image.open("images/PNG/environment/layers/background.png"))
        resized_image= img.resize((380,240), Image.ANTIALIAS)
        self.image= ImageTk.PhotoImage(resized_image)
        # self.image= tkinter.PhotoImage(file="a.png")
        self.parent = parent
        
        print("in")
        self.init()
        # self.showSignUpPage()
        
    def init(self):
        # self.parent.geometry(str(self.w) + "x" + str(self.h))
        canvas = tkinter.Canvas(self.root, width=320, height=240, bg="#3B2314")
        canvas.create_image(0,0, image=self.image)
        canvas.place(x=-2,y=0)
        
    