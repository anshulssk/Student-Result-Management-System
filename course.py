from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
    
        # title
        
        title = Label(self.root, text="Manage Course Details",font=("times new roman", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,height=50)

        #Variables
        self.course=StringVar()
        self.duration=StringVar()
        self.charges=StringVar()

        #Widgets
        lbl_courseName=Label(self.root,text="Course Name",font=("times new roman",15,'bold'),bg='white')
        lbl_courseName.place(x=10,y=100)
        lbl_duration=Label(self.root,text="Duration(yrs)",font=("times new roman",15,'bold'),bg='white')
        lbl_duration.place(x=10,y=160)
        lbl_charges=Label(self.root,text="Charges",font=("times new roman",15,'bold'),bg='white')
        lbl_charges.place(x=10,y=220)
        lbl_description=Label(self.root,text="Description",font=("times new roman",15,'bold'),bg='white')
        lbl_description.place(x=10,y=280)

        #Entry fields
        self.txt_courseName=Entry(self.root,textvariable=self.course,font=("times new roman",15,'bold'),bg='lightyellow')
        self.txt_courseName.place(x=150,y=100,width=200)
        txt_duration=Entry(self.root,textvariable=self.duration,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_duration.place(x=150,y=160,width=200)
        txt_charges=Entry(self.root,textvariable=self.charges,font=("times new roman",15,'bold'),bg='lightyellow').place(x=150,y=220,width=200)
        self.txt_description=Text(self.root,font=("times new roman",15,'bold'),bg='lightyellow')
        self.txt_description.place(x=150,y=280,width=500,height=100)

        #buttons
        self.btn_add=Button(self.root,text='Save',font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=500,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=500,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("times new roman",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=390,y=500,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=510,y=500,width=110,height=40)

        #Search Panel
        self.search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("times new roman",15,'bold'),bg="white").place(x=830,y=100)
        txt_search_courseName=Entry(self.root,textvariable=self.search,font=("times new roman",15,'bold'),bg='lightyellow').place(x=980,y=100,width=250)
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.vsearch).place(x=1260,y=100,width=120,height=28)

        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=830,y=200,width=570,height=450)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=500)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def clear(self):
        self.show()
        self.course.set("")
        self.duration.set("")
        self.charges.set("")
        self.search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.course.get()=="":
                messagebox.showerror("Error","Course Name Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select a course from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.course.get(),))
                        com.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        
        self.course.set(row[1])
        self.duration.set(row[2])
        self.charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    def add(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.course.get()=="":
                messagebox.showerror("Error","Course Name Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name Already Available",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description)values(?,?,?,?)",(
                        self.course.get(),
                        self.duration.get(),
                        self.charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    com.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.course.get()=="":
                messagebox.showerror("Error","Course Name Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from the list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.duration.get(),
                        self.charges.get(),
                        self.txt_description.get("1.0",END),
                        self.course.get()
                    ))
                    com.commit()
                    messagebox.showinfo("Success","Course Updated Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def vsearch(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()