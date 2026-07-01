from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox as mesbox
from createdb import find_users_in_database


def users_login():
    auth_users = Tk()
    auth_users .geometry("500x500")

    login_entry = ttk.Entry(auth_users )
    password_entry = ttk.Entry(auth_users , show="*")

    def auth_user_in_account():
        login = login_entry.get()
        password = password_entry.get()
        if (login and password):
            find_users_in_database
            user = (id,login)
            user = find_users_in_database(login,password)
            if user:
                mesbox.showinfo("congratulashion",f"u here {login}")
                
                
            else:
                mesbox.showwarning("warning", "login uncorrect")          
        else:
            mesbox.showwarning("warning","not null sentase")
            login_entry.delete(0,"end")
            password_entry.delete(0,"end")
    
    enter_login = ttk.Label(text="Enter login: ")
    enter_login.grid(row=0,column=0)
    login_entry.grid(row=1, column=0)
    enter_password = ttk.Label(auth_users, text="Enter password: ")
    enter_password.grid(row=2, column=0)
    password_entry.grid(row=3, column=0)
    login_btn = ttk.Button(auth_users, text="log in", command=auth_user_in_account)
    login_btn.grid(row=4, column=0)
    auth_users.bind("<Return>", lambda event: auth_user_in_account)
