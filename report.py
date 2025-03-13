from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="View Student Results",font=("times new roman", 20, "bold"), bg="orange", fg="#262626").place(x=0, y=0, relwidth=1,height=50)
        

        #search
        self.search=StringVar()
        self.id=StringVar()
        lbl_search=Label(self.root,text="Search By Roll No.",font=("times new roman",20,'bold'),bg='white')
        lbl_search.place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.search,font=("times new roman",20,'bold'),bg='lightyellow')
        txt_search.place(x=520,y=100,width=150)
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.vsearch).place(x=700,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2", command=self.clear).place(x=820,y=100,width=100,height=35)

        #resultlabels
        lbl_roll=Label(self.root, text="Roll No.",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_name=Label(self.root, text="Name",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_course=Label(self.root, text="Course",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_marks=Label(self.root, text="Marks Obtained",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_full=Label(self.root, text="Total Marks",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)
        lbl_per=Label(self.root, text="Percentage",font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE).place(x=1050, y=230, width=150, height=50)

        self.roll=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=300, y=280, width=150, height=50)
        self.name=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.name.place(x=450, y=280, width=150, height=50)
        self.course=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.course.place(x=600, y=280, width=150, height=50)
        self.marks=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=750, y=280, width=150, height=50)
        self.full=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.full.place(x=900, y=280, width=150, height=50)
        self.per=Label(self.root,font=("Times new roman",15,"bold"),bg="white", bd=2, relief=GROOVE)
        self.per.place(x=1050, y=280, width=150, height=50)

        #button delete
        btn_delete=Button(self.root,text='Delete',font=("times new roman",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=650,y=400,width=150,height=35)

    def vsearch(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.search.get( )=="":
                messagebox.showerror("Error","Roll No. required", parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def clear(self):
        self.id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.search.set("")


    def delete(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.id=="":
                messagebox.showerror("Error","Search Student result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.id,))
                        com.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()