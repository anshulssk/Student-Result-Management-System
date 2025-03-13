import sqlite3
def create_db():
    com=sqlite3.connect(database="rms.db")
    cur=com.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text,charges text, description text)")
    com.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    com.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text,course text, marks text, fullmarks text, per text)")
    com.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, f_name text, l_name text, contact text, email text, question text, answer text, password text)")
    com.commit()

    com.close()
create_db()