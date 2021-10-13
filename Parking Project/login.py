from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from mainpage import MainPage


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # background Image
        # self.bg =ImageTk.P#hotoImage(file="..")
        # self.bg_imge=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)
        # title and subtitle
        title = Label(Frame_login, text="Login here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,
                                                                                                                   y=30)
        subtitle = Label(Frame_login, text="Members Area Login", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                         bg="white").place(x=90, y=100)
        # username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
                             bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        # button
        forget = Button(Frame_login, text="Forget Password?", bd=0, font=("Goudy old style", 12), fg="#6162FF",
                        bg="white").place(x=90, y=280)
        submit = Button(Frame_login, command=self.check_function, text="Login", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=90, y=320, width=180, height=40)
        face_cam = Button(Frame_login, text="UseCamera", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=300, y=320, width=180, height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All field are required", parent=self.root)
        elif self.username.get() != "admin" or self.password.get() != "1234":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
            self.close_window()
            MainPage(Tk())

    def close_window(self):
        self.root.destroy()


