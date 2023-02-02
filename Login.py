from tkinter import *
from tkinter import ttk
from pil import Image, ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1300x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth = 1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width = 340, height=450)

        img1 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R1.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image = self.photoimage1, bg="black", borderwidth=0)
        lblimage1.place(x=730, y=175, width=100, height=100)
        
        get_str = Label(frame, text = "Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)
        #Label
        username = lbl = Label(frame, text="username", font=("times new roman", 20, "bold"))
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=40, y=195, width=240)

        password = lbl = Label(frame, text="password", font=("times new roman", 20, "bold"))
        password.place(x=70, y=235)
        self.passtxt = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.passtxt.place(x=40, y=275, width=240)

        img2 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\R1.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimage2 = Label(image = self.photoimage2, bg="black", borderwidth=0)
        lblimage2.place(x=650, y=325, width=25, height=25)

        img3 = Image.open(r"C:\Users\zakir\OneDrive\Desktop\github\Login_form\pass.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimage3 = Label(image = self.photoimage3, bg="black", borderwidth=0)
        lblimage3.place(x=650, y=410, width=25, height=25)




        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=320, width=120, height=35)

        forgotbtn = Button(frame, text="Forgotten Password", font=("times new roman", 8, "bold"), borderwidth=0, fg="white", bg="red", activeforeground="white", activebackground="red")
        forgotbtn.place(x=15, y=360, width=160)

        regbtn = Button(frame, text="NEW User: Register Here.", font=("times new roman", 8, "bold"),borderwidth=0, fg="white", bg="red", activeforeground="white", activebackground="red")
        regbtn.place(x=15, y=385, width=160)

        def login(self):
            if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "all fields rewuired")
            elif self.txtuser.get() == "nuhel" and self.txtpass.get()=="Jasmin123":
                messagebox.showinfo("Success", "Welcome to Attendance system")
            else:
                messagebox.showerror("Invalid", "Invalid username & Password")

        





if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()