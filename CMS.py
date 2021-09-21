from tkinter import *
import tkinter.font
import sqlite3

conn = sqlite3.connect("MyDB.db") #Connect to the DB

#conn.execute("DELETE FROM DETAILS") #Delete all records

## ID          = TRACKING ID - AUTOMATICALLY ASSIGNED
## NAME        = NAME OF THE PERSON 
## DEPARTURE   = STARTING ADDRESS OF PACKAGE
## DESTINATION = DELIVERY ADDRESS OF PACKAGE
## TYPE        = FAST DELIVERY OR NORMAL DELIVERY 


root=Tk()
root.geometry("800x400+200+200")
root.title("Courier Management System")

table=conn.execute("SELECT * FROM DETAILS") # Total number of orders
orders=0
for item in table:
    orders+=1

def header(window,rows): # Used to add the tabular headers

    f1=Label(window,text="TrackID",bg="#fc9126")
    f2=Label(window,text="Name",bg="#fc9126")
    f3=Label(window,text="Departing From",bg="#fc9126")
    f4=Label(window,text="Destination",bg="#fc9126")
    f5=Label(window,text="Order Priority",bg="#fc9126")

    f1.config(font=("Helvetica", 20,"bold"))
    f2.config(font=("Helvetica", 20,"bold"))
    f3.config(font=("Helvetica", 20,"bold"))
    f4.config(font=("Helvetica", 20,"bold"))
    f5.config(font=("Helvetica", 20,"bold"))
    
    f1.grid(row=rows,column=0)
    f2.grid(row=rows,column=1)
    f3.grid(row=rows,column=2)
    f4.grid(row=rows,column=3)
    f5.grid(row=rows,column=4)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)


def complete_db(): # View the complete DB

    window=Toplevel(root)
    window.geometry("800x400+200+200")
    window.title("Database")

    table=conn.execute("SELECT * FROM DETAILS")

    header(window,0)
    
    rows=1
    for item in table:
        cols=0
        for i in item:
            new1=Label(window,text=i)
            new1.config(font=("Helvetica", 10,"bold"))
            new1.grid(row=rows,column=cols)
            cols+=1
        rows+=1
        
    
def search_screen(): 

    def submit():
        new=Toplevel(window)
        new.geometry("800x400+200+200")
        new.title("Results")
        x=e1.get()
        query="SELECT * FROM DETAILS WHERE ID='{}'"
        table=conn.execute(query.format(x))
        header(new,2)
        rows=3
        for item in table:
            cols=0
            for i in item:
                new1=Label(new,text=i)
                new1.config(font=("Helvetica", 10,"bold"))
                new1.grid(row=rows,column=cols)
                cols+=1
            rows+=1
        
    
    window=Toplevel(root)
    window.geometry("400x100+300+300")
    window.title("Search a record")

    lab1=Label(window,text="Enter the Tracking ID")
    lab1.config(font=("Helvetica", 10,"bold"))
    lab1.grid(row=0,column=0)
    e1=Entry(window)
    e1.grid(row=0,column=1)
    
    b1=Button(window,text="Search",command=submit,width=12,height=2,bg="#cfc8c8")
    b1.config(font=("Helvetica", 10,"bold"))
    b1.grid(row=1,column=1)
        
def add_db(): # Add new entry
    global orders
    def submit():
        def close():
            window.destroy()
        global orders
        a=e1.get()
        b=e2.get()
        c=e3.get()
        d=e4.get()
        if a and b and c and d: # Do not accept NULL values
            e=orders+1
            newEntry=(e,a,b,c,d)
            query="INSERT INTO DETAILS(ID,NAME,DEPARTURE,DESTINATION,TYPE) VALUES{}"
            table=conn.execute(query.format(newEntry))
            
            rows=1
            for item in table:
                cols=0
                for i in item:
                    new1=Label(window,text=i)
                    new1.config(font=("Helvetica", 10,"bold"))
                    new1.grid(row=rows,column=cols)
                    cols+=1
                rows+=1
            new=Toplevel(window)
            new.geometry("400x100+350+350")
            lab1=Label(new,text="Entry Added Successfully")
            lab1.config(font=("Helvetica", 10,"bold"))
            lab1.grid(row=0,column=0)
            b1=Button(new,text="OK",command=close,width=12,height=2,bg="#cfc8c8")
            b1.config(font=("Helvetica", 10,"bold"))
            b1.grid(row=1,column=0)
            conn.commit()
    
    window=Toplevel(root)
    window.geometry("400x200+300+300")
    window.title("Add a new order")

    lab1=Label(window,text="Name")
    lab2=Label(window,text="From")
    lab3=Label(window,text="To")
    lab4=Label(window,text="Delivery type")

    lab1.config(font=("Helvetica", 10,"bold"))
    lab2.config(font=("Helvetica", 10,"bold"))
    lab3.config(font=("Helvetica", 10,"bold"))
    lab4.config(font=("Helvetica", 10,"bold"))

    e1=Entry(window)
    e2=Entry(window)
    e3=Entry(window)
    e4=Entry(window)
    
    lab1.grid(row=0,column=0)
    e1.grid(row=0,column=1)

    lab2.grid(row=1,column=0)
    e2.grid(row=1,column=1)

    lab3.grid(row=2,column=0)
    e3.grid(row=2,column=1)

    lab4.grid(row=3,column=0)
    e4.grid(row=3,column=1)

    b1=Button(window,text="Submit",command=submit,width=12,height=2,bg="#cfc8c8")
    b1.config(font=("Helvetica", 10,"bold"))
    b1.grid(row=4,column=1)
    
def info(): # Contributors 
    window=Toplevel(root)
    window.geometry("800x400+200+200")
    window.title("New")
    window.config(background="#fc9126")
    lab=Label(window,text="\nThis project is developed by -\
    \n\n\nSunshodhan Makkar 11802065 B43\n Akash Kumar Singh \
11802072 B44\nAbhishek Sharma 11802082 B45\nK18GA\nLovely \
Professional University")
    lab.config(font=("Helvetica", 20,"bold"),bg="#fc9126")
    lab.pack(fill=tkinter.X)
    
def close(): # Exit Button
    root.destroy()
    
# Main Menu
b1=Button(root,text="View all orders",width=23,height=2,bg="#cfc8c8",command=complete_db)
b2=Button(root,text="Search an order",width=23,height=2,bg="#cfc8c8",command=search_screen)
b3=Button(root,text="Create/Add an order",width=23,height=2,bg="#cfc8c8",command=add_db)
b4=Button(root,text="Info",width=12,height=2,bg="#cfc8c8",command=info)
b5=Button(root,text="Exit",width=12,height=2,bg="#cfc8c8",command=close)
lab=Label(root,text="Courier Management System",bg="#fc9126",pady=35,width=100)

lab.config(font=("Helvetica", 30,"bold"))   # Text styling
b1.config(font=("Helvetica", 10,"bold"))
b2.config(font=("Helvetica", 10,"bold"))
b3.config(font=("Helvetica", 10,"bold"))
b4.config(font=("Helvetica", 10,"bold"))
b5.config(font=("Helvetica", 10,"bold"))

lab.grid(row=0,column=0,columnspan=2)   # Grid 
b1.grid(row=2,column=0,pady=5,columnspan=2)
b2.grid(row=3,column=0,pady=5,columnspan=2)
b3.grid(row=4,column=0,pady=5,columnspan=2)
b4.grid(row=5,column=0,pady=5,columnspan=2)
b5.grid(row=6,column=1,padx=20)

root.grid_columnconfigure(0, weight=1)

root.mainloop()
conn.commit()
conn.close()
