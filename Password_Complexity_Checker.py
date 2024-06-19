import tkinter as tk
import re
def check_password_strength():
    password = password_entry.get()
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    numbers = re.compile(r'[0-9]')
    special_chars = re.compile(r'[!@#$%^&*()_+]')
    min_length = 8
    if len(password) < min_length:
        strength_label.config(text= "password is too short.Minimum length should be 8 characters".format(min_length),fg="red")
        return
    if not lower_case.search(password):
        strength_label.config(text="password must contain at least one lowercase letter",fg="red")
        return
    if not upper_case.search(password):
        strength_label.config(text="password must contain at least one uppercase letter",fg="red")
        return
    if not numbers.search(password):
        strength_label.config(text="password must contain at least one number",fg="red")
        return
    strength_label.config(text="password is strength",fg="green")
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("500x500")

password_label = tk.Label(root, text="Enter your password")
password_label.pack()
password_entry = tk.Entry(root,show = "*")
password_entry.pack()

strength_label = tk.Label(root,text="",fg="black")
strength_label.pack()

check_button = tk.Button(root,text="Check Strength",command=check_password_strength)
check_button.pack()



root.mainloop()




