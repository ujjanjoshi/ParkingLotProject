from tkinter import *
from login import Login


class Welcome:
    def __init__(self, welcome_root):#tk()
        self.welcome_root = welcome_root
        self.welcome_root.title("Welcome Page")
        self.welcome_root.geometry("900x600+250+50")
        self.welcome_root.resizable(False, False)
        Frame_welcome = Frame(self.welcome_root, bg="white")
        Frame_welcome.place(x=0, y=0, width=900, height=600)
        next = Button(Frame_welcome, command=self.login_function,text="Next", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=350, y=280, width=200, height=100)
        title = Label(Frame_welcome, text="Welcome to Smart Parking System", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=100, y=150)

    def login_function(self):
        self.close_window()
        Login(Tk())

    def close_window(self):
        welcome_root.destroy()


welcome_root = Tk()#frame
obj = Welcome(welcome_root)
welcome_root.mainloop()
