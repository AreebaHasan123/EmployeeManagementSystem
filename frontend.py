"""
A program that stores Employees information for the admin.
Last Name, First Name, Emp_Num, Address, Email, Phone Num
User can:
View all records
search an entry
add entry
update entry
delete 
close
"""

from select import select
from tkinter import *
import backend

selected_tuple = ()


#we first binded this to the list1
def get_selected_row(event):
    try:
        global selected_tuple
        """
        curselection()will be an empty list with no items.
         Trying to access the first item of that list with [0]
        """
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #once i select the row, I want it to show it in the top entries
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

    

def view_command():
    #ensure you are deleting everything from index
        #from the row with index of 0 to the end to last row
    list1.delete(0,END)
    for row in backend.view():
        #new rows will be put at the END of listbox
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(lName_text.get(),fName_text.get(),address_text.get(),email_text.get(),phone_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(lName_text.get(),fName_text.get(),address_text.get(),email_text.get(),phone_text.get())
    list1.delete(0,END)
    list1.insert(END,(lName_text.get(),fName_text.get(),address_text.get(),email_text.get(),phone_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],lName_text.get(),fName_text.get(),address_text.get(),email_text.get(),phone_text.get())
    view_command()
   
window=Tk()

l1=Label(window,text="Last Name")
l1.grid(row=0,column=0)

lName_text=StringVar()
e1=Entry(window, textvariable=lName_text)
e1.grid(row=0,column=1)

l2=Label(window,text="First Name")
l2.grid(row=0,column=2)

fName_text=StringVar()
e2=Entry(window, textvariable=fName_text)
e2.grid(row=0,column=3)


l3=Label(window,text="Address")
l3.grid(row=1,column=0)

address_text=StringVar()
e3=Entry(window, textvariable=address_text)
e3.grid(row=1,column=1)

l4=Label(window,text="Email")
l4.grid(row=1,column=2)

email_text=StringVar()
e4=Entry(window, textvariable=email_text)
e4.grid(row=1,column=3)


l5=Label(window,text="Phone Num")
l5.grid(row=0,column=4)

phone_text=StringVar()
e5=Entry(window, textvariable=phone_text)
e5.grid(row=0,column=5)

"""
bind is used to bind a function to a widget event
takes two arguements
takes the event type and a function

"""
list1=Listbox(window, height=6, width=50)
list1.grid(row=2,column=1, rowspan=6,columnspan=2)

#attach a scrollbox
sb1=Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
#Now the buttons

b1=Button(window, text='View all', width=12, command=view_command)
b1.grid(row=3, column=4)

b2=Button(window, text='Search Employee', width=12, command=search_command)
b2.grid(row=3, column=5)

b3=Button(window, text='Add Employee', width=12, command=add_command)
b3.grid(row=4, column=4)

b4=Button(window, text='Update Employee', width=12, command=update_command)
b4.grid(row=5, column=4)

b5=Button(window, text='Delete Employee', width=12, command=delete_command)
b5.grid(row=4, column=5)

b6=Button(window, text='Close Application', width=12, command=window.destroy)
b6.grid(row=5, column=5)

window.mainloop()