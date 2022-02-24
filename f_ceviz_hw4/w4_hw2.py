# Secure Password Generator
from faulthandler import disable
import random as r
import string as st
import tkinter as tk
from subprocess import check_call

from click import command


lower   = st.ascii_lowercase  # The lowercase letters list
upper   = st.ascii_uppercase  # The uppercase letters list
num     = st.digits
punc    = st.punctuation
all     = upper + num + lower + punc

def random_pasword():
    temp_list   = r.sample(upper, 2) + r.sample(num, 2) + r.sample(punc, 2) + r.sample(all, 4)
    password    = "".join(r.sample(temp_list, 10))
    print("Password :", password)
#tkinter text
    str = ''
    for i in password:
        str += i
    print(str)
    label.config(text=str)

#tkinter 
window = tk.Tk()
window.title("Random Password")
window.geometry("500x300")
key_application = tk.Frame(window, bg="black")
key_application.grid()

label_txt = tk.Label(key_application, 
                    text="Password:", 
                    font="Cambria 15 bold")
label_txt.grid(padx=65, pady=10)

label = tk.Label(key_application, 
                text="Please push the botton to creat a password ",
                font="Cambria 14 bold", 
                bg="cyan")
label.grid(padx=65, pady=30)
#  Generate Password button
button1 = tk.Button(key_application, 
                    text="Generate Password",
                    width=50, 
                    height=5,                     
                    command=random_pasword)

button1.grid(padx=65, pady=40)

window.mainloop()

