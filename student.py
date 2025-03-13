from tkinter import*
import re
from tkinter import ttk,messagebox
import sqlite3
from tkcalendar import DateEntry

class InvalidEmailException(Exception):
    pass
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="Manage Student Details",font=("times new roman", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,height=50)

        
        #Variables
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.dob=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.state=StringVar()
        self.city=StringVar()
        self.pin=StringVar()
        self.course=StringVar()

        #Widgets
        #column 1
        lbl_roll=Label(self.root,text="Roll No.",font=("times new roman",15,'bold'),bg='white')
        lbl_roll.place(x=10,y=80)
        lbl_name=Label(self.root,text="Name",font=("times new roman",15,'bold'),bg='white')
        lbl_name.place(x=10,y=130)
        lbl_email=Label(self.root,text="Email",font=("times new roman",15,'bold'),bg='white')
        lbl_email.place(x=10,y=180)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15,'bold'),bg='white')
        lbl_gender.place(x=10,y=230)
        
        lbl_state=Label(self.root,text="State",font=("times new roman",15,'bold'),bg='white')
        lbl_state.place(x=10,y=280)
        self.txt_state=ttk.Combobox(self.root,textvariable=self.state,values=("Select","Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ),font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.txt_state.place(x=110,y=280,width=200)
        self.txt_state.current(0)


        lbl_city=Label(self.root,text="City",font=("times new roman",15,'bold'),bg='white')
        lbl_city.place(x=330,y=280)
        txt_city=Entry(self.root,textvariable=self.city,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_city.place(x=380,y=280,width=100)

        lbl_pin=Label(self.root,text="Pin",font=("times new roman",15,'bold'),bg='white')
        lbl_pin.place(x=530,y=280)
        txt_pin=Entry(self.root,textvariable=self.pin,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_pin.place(x=580,y=280,width=120)
        
        
        lbl_address=Label(self.root,text="Address",font=("times new roman",15,'bold'),bg='white')
        lbl_address.place(x=10,y=330)
        self.txt_address=Text(self.root,font=("times new roman",15,'bold'),bg='lightyellow')
        self.txt_address.place(x=110,y=330,width=540,height=100)

        #Entry fields
        self.txt_roll=Entry(self.root,textvariable=self.roll,font=("times new roman",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=110,y=80,width=200)
        txt_name=Entry(self.root,textvariable=self.name,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_name.place(x=110,y=130,width=200)
        txt_email=Entry(self.root,textvariable=self.email,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_email.place(x=110,y=180,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.gender,values=("Select","Male","Female","Other"),font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=110,y=230,width=200)
        self.txt_gender.current(0)

        #column 2
        lbl_dob=Label(self.root,text="D.O.B(DD/MM/YY)",font=("times new roman",15,'bold'),bg='white')
        lbl_dob.place(x=400,y=80)
        self.cal_dob = DateEntry(self.root, date_pattern='dd/mm/yy', set_date=None, font=("times new roman", 15, 'bold'),bg='lightyellow')
        self.cal_dob.place(x=580,y=80,width=200)
        self.cal_dob.set_date(None)
 
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,'bold'),bg='white')
        lbl_contact.place(x=400,y=130)
        lbl_admission=Label(self.root,text="Admission",font=("times new roman",15,'bold'),bg='white')
        lbl_admission.place(x=400,y=180)
        self.cal_admission = DateEntry(self.root, date_pattern='dd/mm/yy', font=("times new roman", 15, 'bold'),bg='lightyellow')
        self.cal_admission.place(x=500,y=180,width=200)
        self.cal_admission.set_date(None)
        lbl_course=Label(self.root,text="Course",font=("times new roman",15,'bold'),bg='white')
        lbl_course.place(x=400,y=230)

        #Entry fields
        self.course_list=["Empty"]
        #function call to update list
        self.fetch_course()
        txt_contact=Entry(self.root,textvariable=self.contact,font=("times new roman",15,'bold'),bg='lightyellow')
        txt_contact.place(x=500,y=130,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.course,values=self.course_list,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=500,y=230,width=200)
        self.txt_course.set("Select")

        

        #buttons
        self.btn_add=Button(self.root,text='Save',font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=110,y=530,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=250,y=530,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("times new roman",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=390,y=530,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear).place(x=530,y=530,width=110,height=40)

        #Search Panel
        self.search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("times new roman",15,'bold'),bg="white").place(x=830,y=80)
        txt_search_roll=Entry(self.root,textvariable=self.search,font=("times new roman",15,'bold'),bg='lightyellow').place(x=980,y=80,width=200)
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.vsearch).place(x=1260,y=80,width=120,height=28)

        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=830,y=140,width=570,height=450)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pin")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=120)
        self.CourseTable.column("email",width=230)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=300)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    
    
    #functions
    def clear(self):
        self.show()
        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("Select")
        self.contact.set("")
        self.date.set("")
        self.course.set("Select")
        self.state.set("Select")
        self.city.set("")
        self.pin.set("")
        
        self.txt_address.delete('1.0',END)
        self.txt_roll.config(state=NORMAL)
        self.search.set("")
        self.cal_dob.delete(0, END)
        self.cal_admission.delete(0,END)

    def delete(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.roll.get()=="":
                messagebox.showerror("Error","Roll No. Required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select a student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.roll.get(),))
                        com.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]

        self.roll.set(row[0]),
        self.name.set(row[1]),
        self.email.set(row[2]),
        self.gender.set(row[3]),
        self.dob.set(row[4]),
        self.contact.set(row[5]),
        self.date.set(row[6]),
        self.course.set(row[7]),
        self.state.set(row[8]),
        self.city.set(row[9]),
        self.pin.set(row[10]),

        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
        
    
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)
    
    def add(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.roll.get()=="":
                messagebox.showerror("Error","Roll No. Required",parent=self.root)
            elif not self.is_valid_email(self.email.get()):
                raise InvalidEmailException("Invalid Email")
            else:
                cur.execute("select * from student where roll=?",(self.roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No. Already Available",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address)values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.roll.get(),
                        self.name.get(),
                        self.email.get(),
                        self.gender.get(),
                        self.cal_dob.get(),
                        self.contact.get(),
                        self.cal_admission.get(),
                        self.course.get(),
                        self.state.get(),
                        self.city.get(),
                        self.pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    com.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except InvalidEmailException as iee:
            messagebox.showerror("Error", f"Email Error: {str(iee)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            if self.roll.get()=="":
                messagebox.showerror("Error","Roll No. Required",parent=self.root)
            elif not self.is_valid_email(self.email.get()):
                raise InvalidEmailException("Invalid Email")
            else:
                cur.execute("select * from student where roll=?",(self.roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from the list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        
                        self.name.get(),
                        self.email.get(),
                        self.gender.get(),
                        self.cal_dob.get_date().strftime('%d/%m/%y'),
                        self.contact.get(),
                        self.cal_admission.get_date().strftime('%d/%m/%y'),
                        self.course.get(),
                        self.state.get(),
                        self.city.get(),
                        self.pin.get(),

                        self.txt_address.get("1.0",END),
                        self.roll.get()
                    ))
                    com.commit()
                    messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                    self.show()
        except InvalidEmailException as iee:
            messagebox.showerror("Error", f"Email Error: {str(iee)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
    
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def vsearch(self):
        com=sqlite3.connect(database="rms.db")
        cur=com.cursor()
        try:
            cur.execute(f"select * from student where roll=?",(self.search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent="self.root")


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()