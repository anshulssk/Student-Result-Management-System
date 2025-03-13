from tkinter import*
import re
from PIL import Image,ImageTk,ImageDraw
from tkinter import messagebox,ttk
import sqlite3
import os
from math import*
class InvalidEmailException(Exception):
    pass
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1920x1080+0+0")
        
        self.bg_img=Image.open("register_img.jpg")
        self.bg_img=self.bg_img.resize((1920, 1080),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(width=1920,height=1080)
        #frames
        self.email=StringVar()
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=370, y=100, width=800, height=500)
        title=Label(login_frame, text="LOGIN HERE", font=("times new roman",30,"bold"),bg="white", fg="#08A3D2").place(x=250, y=50)
        lbl_email=Label(login_frame, text="EMAIL ADDRESS", font=("times new roman",18,"bold"),bg="white", fg="gray").place(x=250, y=150)
        self.txt_email=Entry(login_frame, textvariable=self.email, font=("times new roman",15,"bold"), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        password=Label(login_frame, text="PASSWORD", font=("times new roman",18,"bold"),bg="white", fg="gray").place(x=250, y=250)
        self.txt_password=Entry(login_frame, font=("times new roman",15,"bold"), bg="lightgray")
        self.txt_password.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame, text="Register new Account",font=("times new roman",14),bg="white", bd=0, fg="#B00857",cursor="hand2", command=self.register_window).place(x=250, y=320)
        btn_forgot=Button(login_frame, text="Forget password?", font=("times new roman",14),bg="white", bd=0, fg="#B00857",cursor="hand2", command=self.forget_password_window).place(x=450, y=320)
        btn_login=Button(login_frame, text="Login",font=("times new roman",20),fg="white", bg="#B00857",cursor="hand2", command=self.login).place(x=250, y=380, width=180, height=40)
    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root2)
        else:
            try:
                com=sqlite3.connect(database="rms.db")
                cur=com.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select correct Security Question / Enter Answer", parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_pass.get(), self.txt_email.get()))
                    com.commit()
                    com.close()
                    messagebox.showinfo("Success","your password has been reset, Please login with new password", parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
            except Exception as es: 
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter valid email address to reset your password", parent=self.root)
        else:
            try:
                com=sqlite3.connect(database="rms.db")
                cur=com.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter valid email address to reset your password", parent=self.root)
                else:
                    com.close() 
                    self.root2=Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t=Label(self.root2, text="Forget Password", font=("times new roman",20,"bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
        
                    #forget password
                    question=Label(self.root2, text="Security Question",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=100)
                    
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly', justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2, text="Answer",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15), bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password=Label(self.root2, text="New Password",font=("times new roman",15,"bold"),bg="white", fg="gray").place(x=50, y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    btn_change_password=Button(self.root2, text="Reset Password", font=("times new roman",15,"bold"), bg="green", fg="white",command=self.forget_password).place(x=80, y=340)

                    
            except Exception as es: 
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)

            
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)
    

    def register_window(self):
        self.root.destroy()
        import register
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif not self.is_valid_email(self.email.get()):  
            messagebox.showerror("Error", "Invalid Email", parent=self.root)
        else:
            try:
                com=sqlite3.connect(database="rms.db")
                cur=com.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(), self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","INVALID USERNAME & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                com.close()  
            except Exception as es: 
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)
        
    
root=Tk()
obj=Login_window(root)
root.mainloop()