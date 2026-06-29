from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox as messbox
from createdb import add_users_into_database

root = Tk()
root.geometry("500x500")
login_entry = ttk.Entry(root)
password_entry = ttk.Entry(root, show="*")
def add_users():
    try:
        login = login_entry.get()
        password = password_entry.get()
        add_users_into_database(login,password)
        login_entry.delete(0,"end")
        password_entry.delete(0,"end")
        messbox.showinfo("sucessfuly",f"hello {login}!\n you register")
    except Exception as ex:
        messbox.showerror("Error!", f"Error 404\n{ex})")


button = ttk.Button(root,text="add", command=add_users)
login_entry.grid(row=0, column=0,pady=5)
password_entry.grid(row=1, column=0, pady=5)
button.grid(row=2, column=0,pady=5)
root.mainloop()