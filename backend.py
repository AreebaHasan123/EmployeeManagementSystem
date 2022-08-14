#if you run the function like connect()-> since frontend imports backend 
#it will still run if I run the frontend.py file

import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(empID INTEGER PRIMARY KEY, l_name text, f_name text, address text, email text, phone_num text)")
    conn.commit()
    conn.close()

def drop():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE book")
    print("Table dropped... ")
    conn.commit()
    conn.close()

def insert(l_name,f_name,address,email,phone_num):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(l_name,f_name,address,email,phone_num))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows
    
#search has 4 parameters: put them as empty strings otherwise will need to have all 4 for the
#function to run

def search(l_name="",f_name="",address="",email="",phone_num=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE l_name=? OR f_name=? OR address=? OR email=? OR phone_num=?",(l_name,f_name,address,email,phone_num))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(empID):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE empID=?",(empID,))
    conn.commit()
    conn.close()

def update(empID,l_name,f_name,address,email,phone_num):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET l_name=?, f_name=?, address=?, email=?, phone_num=? WHERE empID=?",(l_name,f_name,address,email,phone_num, empID))
    conn.commit()
    conn.close()
#connect()
#drop()
#insert("Halpert","John","3425 W Kingsley Rd Garland, Texas 75042", "halpjohn@gmail.com","1234567890")
#print(view())
#print(search(f_name="John"))


#insert("Halpert","John","3425 W Kingsley Rd Garland, Texas 75042", "halpjohn@gmail.com","1234567890")
#print(view())
#update(1,"Schrute", "Dwight","3425 W Kingsley Rd Garland, Texas 75042", "schjohn@gmail.com","258963142")
#print(view())