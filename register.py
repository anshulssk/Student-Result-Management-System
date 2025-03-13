from tkinter import*
import re
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
class InvalidEmailException(Exception):
    pass
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Window")
        self.root.geometry("1920x1080+0+0")

        self.bg_img=Image.open("register_img.jpg")
        self.bg_img=self.bg_img.resize((1920, 1080),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(width=1920,height=1080)

        #Register Frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=600)

        title=Label(frame1, text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white", fg="green").place(x=50, y=30)
        self.logo_dash=Image.open("register_img.jpg")
        self.logo_dash=self.logo_dash.resize((1920,1080),Image.LANCZOS)
        self.logo_dash=ImageTk.PhotoImage(self.logo_dash)
        
        #Row1
        
        f_name=Label(frame1, text="First Name",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name=Label(frame1, text="Last Name",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        #Row2
        contact=Label(frame1, text="Contact No.",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        self.email=StringVar()
        lbl_email=Label(frame1, text="Email",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=370, y=170)
        self.txt_email=Entry(frame1,textvariable=self.email, font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        #Row3
        question=Label(frame1, text="Security Question",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly', justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1, text="Answer",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        #Row4
        password=Label(frame1, text="Password",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword=Label(frame1, text="Confirm Password",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #Terms

        self.v_chk=IntVar()
        chk=Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.v_chk, onvalue=1, offvalue=0, bg="white",font=("times new roman",12)).place(x=50, y=400)
        btn_register=Button(frame1, text=" Register Now",font=("times new roman", 20), bd=4, cursor="hand2", command=self.register_data).place(x=50, y=460,width=180)
        lbl_or=Label(frame1, text="OR",font=("times new roman", 20),bg="white").place(x=300, y=470,width=50)
        btn_login=Button(frame1, text="Sign In", font=("times new roman",20), bd=4, cursor="hand2",command=self.login_window).place(x=400, y=460, width=150)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)
    
    def register_data(self):    
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same", parent=self.root)
        elif self.v_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Termssd   & Conditions", parent=self.root)
        elif not self.is_valid_email(self.email.get()):
            messagebox.showerror("Error", "Invalid Email", parent=self.root)    
        else:
            try:    
                com=sqlite3.connect(database="rms.db")
                cur=com.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row=cur.fetchone()                              
                if row!=None:
                    messagebox.showerror("Error","User already exist, Please try with another email")
                else:
                    cur.execute("insert into employee (f_name, l_name, contact, email, question, answer, password)values(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))
                    com.commit()
                    com.close()
                    messagebox.showinfo("Success","Registration Successful", parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()