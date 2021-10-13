from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class OnOff:
    def __init__(self):
        self.root = Tk()
        self.root.title("On/off")
        self.root.geometry("600x600+450+50")
        self.root.resizable(False, False)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, width=600, height=600)
        lbl_password = Label(Frame_login, text="ON/OFF", font=("Goudy old style", 15, "bold"), fg="grey",
                             bg="white").place(x=50, y=250)
        # on_off = Button(Frame_login, text="ON/OFF", bd=0, font=("Goudy old style", 15),
        #                 bg="#6162FF",
        #                 fg="white").place(x=50, y=50, width=500, height=140)
        # show_details = Button(Frame_login, text="Show Details", bd=0, font=("Goudy old style", 15),
        #                 bg="#6162FF",
        #                 fg="white").place(x=50, y=250, width=500, height=140)
        # parking_information = Button(Frame_login, text="Parking Information", bd=0, font=("Goudy old style", 15),
        #                 bg="#6162FF",
        #                 fg="white").place(x=50, y=450, width=500, height=140)