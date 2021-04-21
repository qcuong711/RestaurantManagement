import tkinter, time, base64, imaplib, smtplib
import os
import tkinter as tk
from imaplib import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mbox
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mysql',
                             db='projecttt',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# chuc nang login
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=openmainwindow).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command = register).pack()

    main_screen.mainloop()

# ket thuc chuc nang login
def openmainwindow():
    login_screen.destroy()
    delete_login_success()
    main_screen.destroy()
    mainframe()


def on_closing():
    if mbox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def onInfo():
    mbox.showinfo("Restaurant Managerment", "Version: 1.0")

# chuc nang them vao manager moi
def mninsert():
    def insm():
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "insert into manager(m_id, m_name, salary) values(%s, %s, %s)"
        val = (entry1.get(), entry2.get(), entry3.get())
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()
    inswindow = Tk()
    inswindow.geometry("250x170")
    inswindow.title("Please insert the information!")

    label1 = Label(inswindow, text="Enter ID")
    label1.place(x=20, y=10)
    entry1 = Entry(inswindow)
    entry1.place(x=90, y=10)
    label2 = Label(inswindow, text="Enter name")
    label2.place(x=20, y=50)
    entry2 = Entry(inswindow)
    entry2.place(x=90, y=50)
    label3 = Label(inswindow, text="Enter salary")
    label3.place(x=20, y=90)
    entry3 = Entry(inswindow)
    entry3.place(x=90, y=90)

    Buttonm1 = Button(inswindow, text="Add", command = lambda:insm())
    Buttonm1.place(x=110, y=130)

    inswindow.mainloop()

# chuc nang edit thong tin manager
def mnedit():
    def editm():
        dele = tree.selection()
        tree.delete(dele)
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "update manager set m_id=%s, m_name=%s, salary=%s where m_id=%s"
        val = (entry1.get(), entry2.get(), entry3.get(), item[0])
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    editwindow = Tk()
    editwindow.geometry("250x170")
    editwindow.title("Please edit the information!")

    label1 = Label(editwindow, text="Update ID")
    label1.place(x=20, y=10)
    entry1 = Entry(editwindow)
    entry1.place(x=110, y=10)
    label2 = Label(editwindow, text="Update name")
    label2.place(x=20, y=50)
    entry2 = Entry(editwindow)
    entry2.place(x=110, y=50)
    label3 = Label(editwindow, text="Update salary")
    label3.place(x=20, y=90)
    entry3 = Entry(editwindow)
    entry3.place(x=110, y=90)

    Buttonm1 = Button(editwindow, text="Edit", command = lambda:editm())
    Buttonm1.place(x=110, y=130)

    for x in tree.selection():
        item = tree.item(x, 'values')
        entry1.insert(tk.END, item[0])
        entry2.insert(tk.END, item[1])
        entry3.insert(tk.END, item[2])

    editwindow.mainloop()

# chuc nang xoa manager
def delmn():
    for x in tree.selection():
        item = tree.item(x, "values")
    dele = tree.selection()
    tree.delete(dele)
    cursor = connection.cursor()
    cmd = "delete from manager where m_id=%s"
    val = (item[0])
    cursor.execute(cmd, val)
    connection.commit()
    cursor.close()

# cua so qua li manager
def managerwindow():
    mnwindow = Tk()
    mnwindow.geometry("600x400")
    mnwindow.title("Manager List")

    scrollbar = Scrollbar(mnwindow)
    scrollbar.pack(side = RIGHT, fill = Y)

    global tree
    tree = ttk.Treeview(mnwindow, yscrollcommand=scrollbar.set)

    tree["show"]= "headings"
    tree["columns"]=("one","two","three")
    tree.column("one", width=100, minwidth=100, stretch=tk.NO)
    tree.column("two", width=300, minwidth=300,stretch=tk.NO)
    tree.column("three", width=185, minwidth=185, stretch=tk.NO)

    tree.heading("one", text="ID",anchor=tk.W)
    tree.heading("two", text="Name",anchor=tk.W)
    tree.heading("three", text="Salary",anchor=tk.W)

    mycursor = connection.cursor()
    mycursor.execute("select * from manager")
    myresult = mycursor.fetchall()

    for row in myresult:
        lst = list(row.values())
        print(lst)
        tree.insert("", "end", values=lst)

    scrollbar.config( command = tree.yview )
    tree.pack(side=tk.TOP,fill=tk.X)

    Buttonm1 = Button(mnwindow, text="Add Manager", width = 15, height = 2, command = mninsert)
    Buttonm1.place(x=50, y=280)
    Buttonm2 = Button(mnwindow, text="Edit Information", width = 15, height = 2, command = mnedit)
    Buttonm2.place(x=250, y=280)
    Buttonm3 = Button(mnwindow, text="Fired Manager", width = 15, height = 2, command = delmn)
    Buttonm3.place(x=450, y=280)

# chuc nang them vao employee moi
def eminsert():
    def insem():
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()))
        cursor = connection.cursor()
        cmd = "insert into employee(e_id, e_name, m_id, hire_date, job, salary) values (%s, %s, %s, %s, %s, %s)"
        val = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get())
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    einswindow = Tk()
    einswindow.geometry("280x300")
    einswindow.title("Please insert the information!")

    label1 = Label(einswindow, text="Enter ID")
    label1.place(x=20, y=10)
    entry1 = Entry(einswindow)
    entry1.place(x=130, y=10)
    label2 = Label(einswindow, text="Enter name")
    label2.place(x=20, y=50)
    entry2 = Entry(einswindow)
    entry2.place(x=130, y=50)
    label3 = Label(einswindow, text="Enter manager's ID")
    label3.place(x=20, y=90)
    entry3 = Entry(einswindow)
    entry3.place(x=130, y=90)
    label4 = Label(einswindow, text="Enter hire date")
    label4.place(x=20, y=130)
    entry4 = Entry(einswindow)
    entry4.place(x=130, y=130)
    label5 = Label(einswindow, text="Enter job")
    label5.place(x=20, y=170)
    entry5 = Entry(einswindow)
    entry5.place(x=130, y=170)
    label6 = Label(einswindow, text="Enter salary")
    label6.place(x=20, y=210)
    entry6 = Entry(einswindow)
    entry6.place(x=130, y=210)

    Buttone1 = Button(einswindow, text="Add", command = lambda:insem())
    Buttone1.place(x=110, y=250)

    einswindow.mainloop()

# chuc nang edit thong tin employee
def emedit():
    def editem():
        edit = tree.selection()
        tree.delete(edit)
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()))
        cursor = connection.cursor()
        cmd = "update employee set e_id=%s, e_name=%s, m_id=%s, hire_date=%s, job=%s, salary=%s where e_id=%s"
        val = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), item[0])
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    emeditwindow = Tk()
    emeditwindow.geometry("280x300")
    emeditwindow.title("Please edit the information!")

    label1 = Label(emeditwindow, text="Edit ID")
    label1.place(x=20, y=10)
    entry1 = Entry(emeditwindow)
    entry1.place(x=130, y=10)
    label2 = Label(emeditwindow, text="Edit name")
    label2.place(x=20, y=50)
    entry2 = Entry(emeditwindow)
    entry2.place(x=130, y=50)
    label3 = Label(emeditwindow, text="Edit manager's ID")
    label3.place(x=20, y=90)
    entry3 = Entry(emeditwindow)
    entry3.place(x=130, y=90)
    label4 = Label(emeditwindow, text="Edit hire date")
    label4.place(x=20, y=130)
    entry4 = Entry(emeditwindow)
    entry4.place(x=130, y=130)
    label5 = Label(emeditwindow, text="Edit job")
    label5.place(x=20, y=170)
    entry5 = Entry(emeditwindow)
    entry5.place(x=130, y=170)
    label6 = Label(emeditwindow, text="Edit salary")
    label6.place(x=20, y=210)
    entry6 = Entry(emeditwindow)
    entry6.place(x=130, y=210)

    Buttonm1 = Button(emeditwindow, text="Edit", command = lambda:editem())
    Buttonm1.place(x=110, y=250)

    for x in tree.selection():
        item = tree.item(x, 'values')
        entry1.insert(tk.END, item[0])
        entry2.insert(tk.END, item[1])
        entry3.insert(tk.END, item[2])
        entry4.insert(tk.END, item[3])
        entry5.insert(tk.END, item[4])
        entry6.insert(tk.END, item[5])

    emeditwindow.mainloop()

# chuc nang xoa employee
def delem():
    for x in tree.selection():
        item = tree.item(x, "values")
    dele = tree.selection()
    tree.delete(dele)
    cursor = connection.cursor()
    cmd = "delete from employee where e_id=%s"
    val = (item[0])
    cursor.execute(cmd, val)
    connection.commit()
    cursor.close()

# cua so qua li employee
def employeewindow():
    emwindow = Tk()
    emwindow.geometry("600x400")
    emwindow.title("Employee List")

    scrollbar = Scrollbar(emwindow)
    scrollbar.pack(side = RIGHT, fill = Y)

    global tree
    tree = ttk.Treeview(emwindow, yscrollcommand=scrollbar.set)

    tree["show"]= "headings"
    tree["columns"]=("one","two","three","four","five","six")
    tree.column("one", width=50, minwidth=50, stretch=tk.NO)
    tree.column("two", width=150, minwidth=150,stretch=tk.NO)
    tree.column("three", width=75, minwidth=75, stretch=tk.NO)
    tree.column("four", width=100, minwidth=100, stretch=tk.NO)
    tree.column("five", width=125, minwidth=125,stretch=tk.NO)
    tree.column("six", width=85, minwidth=85, stretch=tk.NO)

    tree.heading("one", text="ID",anchor=tk.W)
    tree.heading("two", text="Name",anchor=tk.W)
    tree.heading("three", text="Manager",anchor=tk.W)
    tree.heading("four", text="Hire date",anchor=tk.W)
    tree.heading("five", text="Job",anchor=tk.W)
    tree.heading("six", text="Salary",anchor=tk.W)

    mycursor = connection.cursor()
    mycursor.execute("select * from employee")
    myresult = mycursor.fetchall()

    for row in myresult:
        lst = list(row.values())
        print(lst)
        tree.insert("", "end", values=lst)

    scrollbar.config( command = tree.yview )
    tree.pack(side=tk.TOP,fill=tk.X)

    Buttonm1 = Button(emwindow, text="Add Employee", width = 15, height = 2, command = eminsert)
    Buttonm1.place(x=50, y=280)
    Buttonm2 = Button(emwindow, text="Edit Information", width = 15, height = 2, command = emedit)
    Buttonm2.place(x=250, y=280)
    Buttonm3 = Button(emwindow, text="Fired Employee", width = 15, height = 2, command = delem)
    Buttonm3.place(x=450, y=280)

# chuc nang them vao drink moi
def dinsert():
    def ind():
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "insert into drinks(d_id, d_name, d_price) values(%s, %s, %s)"
        val = (entry1.get(), entry2.get(), entry3.get())
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    insdwindow = Tk()
    insdwindow.geometry("250x170")
    insdwindow.title("Please insert the information!")

    label1 = Label(insdwindow, text="Enter ID")
    label1.place(x=20, y=10)
    entry1 = Entry(insdwindow)
    entry1.place(x=90, y=10)
    label2 = Label(insdwindow, text="Enter name")
    label2.place(x=20, y=50)
    entry2 = Entry(insdwindow)
    entry2.place(x=90, y=50)
    label3 = Label(insdwindow, text="Enter price")
    label3.place(x=20, y=90)
    entry3 = Entry(insdwindow)
    entry3.place(x=90, y=90)

    Buttonm1 = Button(insdwindow, text="Add", command = lambda:ind())
    Buttonm1.place(x=110, y=130)

    insdwindow.mainloop()

# chuc nang edit thong tin drinks
def dedit():
    def editd():
        dele = tree.selection()
        tree.delete(dele)
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "update drinks set d_id=%s, d_name=%s, d_price=%s where d_id=%s"
        val = (entry1.get(), entry2.get(), entry3.get(), item[0])
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    editdwindow = Tk()
    editdwindow.geometry("250x170")
    editdwindow.title("Please edit the information!")

    label1 = Label(editdwindow, text="Update ID")
    label1.place(x=20, y=10)
    entry1 = Entry(editdwindow)
    entry1.place(x=110, y=10)
    label2 = Label(editdwindow, text="Update name")
    label2.place(x=20, y=50)
    entry2 = Entry(editdwindow)
    entry2.place(x=110, y=50)
    label3 = Label(editdwindow, text="Update salary")
    label3.place(x=20, y=90)
    entry3 = Entry(editdwindow)
    entry3.place(x=110, y=90)

    Buttonm1 = Button(editdwindow, text="Edit", command = lambda:editd())
    Buttonm1.place(x=110, y=130)

    for x in tree.selection():
        item = tree.item(x, 'values')
        entry1.insert(tk.END, item[0])
        entry2.insert(tk.END, item[1])
        entry3.insert(tk.END, item[2])

    editdwindow.mainloop()

# chuc nang xoa drinks
def deld():
    for x in tree.selection():
        item = tree.item(x, "values")
    dele = tree.selection()
    tree.delete(dele)
    cursor = connection.cursor()
    cmd = "delete from drinks where d_id=%s"
    val = (item[0])
    cursor.execute(cmd, val)
    connection.commit()
    cursor.close()

# cua so qua li drinks
def drinkswindow():
    dwindow = Tk()
    dwindow.geometry("600x400")
    dwindow.title("Drinks List")

    scrollbar = Scrollbar(dwindow)
    scrollbar.pack(side = RIGHT, fill = Y)

    global tree
    tree = ttk.Treeview(dwindow, yscrollcommand=scrollbar.set)

    tree["show"]= "headings"
    tree["columns"]=("one","two","three")
    tree.column("one", width=100, minwidth=100, stretch=tk.NO)
    tree.column("two", width=300, minwidth=300,stretch=tk.NO)
    tree.column("three", width=185, minwidth=185, stretch=tk.NO)

    tree.heading("one", text="ID",anchor=tk.W)
    tree.heading("two", text="Name",anchor=tk.W)
    tree.heading("three", text="Price",anchor=tk.W)

    mycursor = connection.cursor()
    mycursor.execute("select * from drinks")
    myresult = mycursor.fetchall()

    for row in myresult:
        lst = list(row.values())
        print(lst)
        tree.insert("", "end", values=lst)

    scrollbar.config( command = tree.yview )
    tree.pack(side=tk.TOP,fill=tk.X)

    Buttonm1 = Button(dwindow, text="Add Drinks", width = 15, height = 2, command = dinsert)
    Buttonm1.place(x=50, y=280)
    Buttonm2 = Button(dwindow, text="Edit Information", width = 15, height = 2, command = dedit)
    Buttonm2.place(x=250, y=280)
    Buttonm3 = Button(dwindow, text="Delete Drinks", width = 15, height = 2, command = deld)
    Buttonm3.place(x=450, y=280)

# chuc nang them vao food moi
def finsert():
    def inf():
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "insert into foods(f_id, f_name, f_price) values(%s, %s, %s)"
        val = (entry1.get(), entry2.get(), entry3.get())
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    insfwindow = Tk()
    insfwindow.geometry("250x170")
    insfwindow.title("Please insert the information!")

    label1 = Label(insfwindow, text="Enter ID")
    label1.place(x=20, y=10)
    entry1 = Entry(insfwindow)
    entry1.place(x=90, y=10)
    label2 = Label(insfwindow, text="Enter name")
    label2.place(x=20, y=50)
    entry2 = Entry(insfwindow)
    entry2.place(x=90, y=50)
    label3 = Label(insfwindow, text="Enter price")
    label3.place(x=20, y=90)
    entry3 = Entry(insfwindow)
    entry3.place(x=90, y=90)

    Buttonm1 = Button(insfwindow, text="Add", command = lambda:inf())
    Buttonm1.place(x=110, y=130)

    insfwindow.mainloop()

# chuc nang edit thong tin foods
def fedit():
    def editf():
        dele = tree.selection()
        tree.delete(dele)
        tree.insert("", "end", values=(entry1.get(), entry2.get(), entry3.get()))
        cursor = connection.cursor()
        cmd = "update foods set f_id=%s, f_name=%s, f_price=%s where f_id=%s"
        val = (entry1.get(), entry2.get(), entry3.get(), item[0])
        cursor.execute(cmd, val)
        connection.commit()
        cursor.close()

    editfwindow = Tk()
    editfwindow.geometry("250x170")
    editfwindow.title("Please edit the information!")

    label1 = Label(editfwindow, text="Update ID")
    label1.place(x=20, y=10)
    entry1 = Entry(editfwindow)
    entry1.place(x=110, y=10)
    label2 = Label(editfwindow, text="Update name")
    label2.place(x=20, y=50)
    entry2 = Entry(editfwindow)
    entry2.place(x=110, y=50)
    label3 = Label(editfwindow, text="Update salary")
    label3.place(x=20, y=90)
    entry3 = Entry(editfwindow)
    entry3.place(x=110, y=90)

    Buttonm1 = Button(editfwindow, text="Edit", command = lambda:editf())
    Buttonm1.place(x=110, y=130)

    for x in tree.selection():
        item = tree.item(x, 'values')
        entry1.insert(tk.END, item[0])
        entry2.insert(tk.END, item[1])
        entry3.insert(tk.END, item[2])

    editfwindow.mainloop()

# chuc nang xoa foods
def delf():
    for x in tree.selection():
        item = tree.item(x, "values")
    dele = tree.selection()
    tree.delete(dele)
    cursor = connection.cursor()
    cmd = "delete from foods where f_id=%s"
    val = (item[0])
    cursor.execute(cmd, val)
    connection.commit()
    cursor.close()

# cua so qua li foods
def foodswindow():
    fwindow = Tk()
    fwindow.geometry("600x400")
    fwindow.title("Foods List")

    scrollbar = Scrollbar(fwindow)
    scrollbar.pack(side = RIGHT, fill = Y)

    global tree
    tree = ttk.Treeview(fwindow, yscrollcommand=scrollbar.set)

    tree["show"]= "headings"
    tree["columns"]=("one","two","three")
    tree.column("one", width=100, minwidth=100, stretch=tk.NO)
    tree.column("two", width=300, minwidth=300,stretch=tk.NO)
    tree.column("three", width=185, minwidth=185, stretch=tk.NO)

    tree.heading("one", text="ID",anchor=tk.W)
    tree.heading("two", text="Name",anchor=tk.W)
    tree.heading("three", text="Price",anchor=tk.W)

    mycursor = connection.cursor()
    mycursor.execute("select * from foods")
    myresult = mycursor.fetchall()

    for row in myresult:
        lst = list(row.values())
        print(lst)
        tree.insert("", "end", values=lst)

    scrollbar.config( command = tree.yview )
    tree.pack(side=tk.TOP,fill=tk.X)

    Buttonm1 = Button(fwindow, text="Add Foods", width = 15, height = 2, command = finsert)
    Buttonm1.place(x=50, y=280)
    Buttonm2 = Button(fwindow, text="Edit Information", width = 15, height = 2, command = fedit)
    Buttonm2.place(x=250, y=280)
    Buttonm3 = Button(fwindow, text="Delete Foods", width = 15, height = 2, command = delf)
    Buttonm3.place(x=450, y=280)

#cua so chinh
def mainframe():
    global window
    window = Tk()
    window.geometry("700x500")
    window.maxsize(width = 700, height = 500)
    window.minsize(width = 700, height = 500)
    window.title("Restaurant Management Application")
    window.configure(bg = "aqua")

    menu = Menu(window)
    new_item1 = Menu(menu)
    new_item2 = Menu(menu)
    menu.add_cascade(label='Option', menu=new_item1)
    menu.add_cascade(label='About', menu=new_item2)
    new_item1.add_command(label='Config')
    new_item1.add_command(label='Quit', command = on_closing)
    new_item2.add_command(label="About Us", command = onInfo)
    window.config(menu=menu)

    label = tk.Label(window, text = "RESTAURANT MANAGEMENT", font = ("Arial", 30), borderwidth = 10,relief = "groove", bg = "yellowgreen").pack(pady = 50)
    label2 = tk.Label(window, text = "Please select a table:", font = ("Arial", 15), borderwidth = 2,relief = "solid", bg = "darkorange").pack(pady = 20)

    aButton = Button(window, text="Manager", width = 15, height = 3, command = managerwindow)
    aButton.place(x=150, y=270)
    bButton = Button(window, text="Employee", width = 15, height = 3, command = employeewindow)
    bButton.place(x=450, y=270)
    cButton = Button(window, text="Drinks", width = 15, height = 3, command = drinkswindow)
    cButton.place(x=150, y=375)
    dButton = Button(window, text="Foods", width = 15, height = 3, command = foodswindow)
    dButton.place(x=450, y=375)

    window.mainloop()

mainframe()
#main_account_screen()
