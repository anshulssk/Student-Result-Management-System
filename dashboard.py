from tkinter import*
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import sqlite3
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        
        #icons
        self.logo_dash=Image.open("img.png")
        self.logo_dash=self.logo_dash.resize((140,80),Image.LANCZOS)
        self.logo_dash=ImageTk.PhotoImage(self.logo_dash)
        
        #title
        title=Label(self.root,text="Student Result Management System",compound=LEFT,image=self.logo_dash,font=("times new roman",20,"bold"),bg="#033054", fg="white")
        title.place(x=0,y=0,relwidth=1,height=50) #label is class visit in tkinter

        #Menu
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)

        btn_course=Button(M_Frame,text="Course",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course)
        btn_course.place(x=20,y=5,width=200,height=30)
        btn_student=Button(M_Frame,text="Student",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student)
        btn_student.place(x=270,y=5,width=200,height=30)
        btn_result=Button(M_Frame,text="Result",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result)
        btn_result.place(x=530,y=5,width=200,height=30)
        btn_view=Button(M_Frame,text="Student Result",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report)
        btn_view.place(x=780,y=5,width=200,height=30)
        btn_logout=Button(M_Frame,text="Logout",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=1030,y=5,width=200,height=30)
        btn_exit=Button(M_Frame,text="Exit",font=("times new roman",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_out)
        btn_exit.place(x=1270,y=5,width=200,height=30)

        #content
        self.bg_img=Image.open("bg.png")
        self.bg_img = self.bg_img.resize((650  , 500),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=450,y=150,width=650,height=500)

        #details
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=290,y=620,width=300,height=100)

        self.lbl_student=Label(self.root, text="Total Students\n[ 0 ]", font=("times new roman", 20), bd=10,relief=RIDGE, bg="orange", fg="white")
        self.lbl_student.place(x=650, y=620, width=300, height=100)

        self.lbl_result=Label(self.root, text="Total Results\n[ 0 ]", font=("times new roman", 20), bd=10,relief=RIDGE, bg="green", fg="white")
        self.lbl_result.place(x=1020, y=620, width=300, height=100)
        
        #footer
        footer=Label(self.root,text="SRMS-Student Result Management System\n Contact Us for any Technical Issue:745xxxxx70",font=("times new roman",12),bg="#262626", fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()

    def update_details(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really  want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
    def exit_out(self):
        op=messagebox.askyesno("Confirm","Do you really  want to exit?", parent=self.root)
        if op==True:
            self.root.destroy()




if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
