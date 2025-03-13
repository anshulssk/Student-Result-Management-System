from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="Add Student Results",font=("times new roman", 20, "bold"), bg="orange", fg="#262626").place(x=0, y=0, relwidth=1,height=50)
        
        #widgets
        #varibles
        self.roll=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.marks=StringVar()
        self.fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        lbl_select=Label(self.root,text="Select Student",font=("times new roman",20,'bold'),bg='white')
        lbl_select.place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("times new roman",20,'bold'),bg='white')
        lbl_name.place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("times new roman",20,'bold'),bg='white')
        lbl_course.place(x=50,y=220)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("times new roman",20,'bold'),bg='white')
        lbl_marks.place(x=50,y=280)
        lbl_fullmarks=Label(self.root,text="Full Marks",font=("times new roman",20,'bold'),bg='white')
        lbl_fullmarks.place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.roll,values=self.roll_list,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.vsearch).place(x=500,y=100,width=120,height=28)

        txt_name=Entry(self.root,textvariable=self.name,font=("times new roman",20,'bold'),bg='lightyellow',state="readonly")
        txt_name.place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.course,font=("times new roman",20,'bold'),bg='lightyellow',state="readonly")
        txt_course.place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.marks,font=("times new roman",20,'bold'),bg='lightyellow')
        txt_marks.place(x=280,y=280,width=320)
        txt_fullmarks=Entry(self.root,textvariable=self.fullmarks,font=("times new roman",20,'bold'),bg='lightyellow')
        txt_fullmarks.place(x=280,y=340,width=320)

        

        #buttons
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        
        #image
        self.bg_img=Image.open("res.jpeg")
        self.bg_img=self.bg_img.resize((1000, 1000),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=700,y=50,width=850,height=750)

    #functions
    def fetch_roll(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
    
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def vsearch(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute(f"select name,course from student where roll=?",(self.roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.name.set(row[0])
                self.course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent="self.root")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.roll.get(),self.course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already Present",parent=self.root)
                else:
                    per=(int(self.marks.get())*100)/int(self.fullmarks.get())
                    cur.execute("insert into result(roll,name,course,marks,fullmarks,per) values(?,?,?,?,?,?)",(
                        self.roll.get(),
                        self.name.get(),
                        self.course.get(),
                        self.marks.get(),
                        self.fullmarks.get(),
                        str(per)
                    ))
                    com.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.roll.set("Select")
        self.name.set("")
        self.course.set("")
        self.marks.set("")
        self.fullmarks.set("")



if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()