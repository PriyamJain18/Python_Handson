# install -> pip install bcrypt
import bcrypt
from tkinter import *

#password = b"thisismypassword"
#hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
#below has is generated for the above password using bcrypt
def validate_password(pwd):
    hash = b'$2b$12$c4cTDjIpjO7X1JcNGOD01uHpEXZJL0OCcQQfE79arWkhcuu6.cVcu'
    entered_password = pwd.encode('utf-8')
    if bcrypt.checkpw(entered_password, hash):
        print("Login Successful")
    else:
        print("Login Failed, check your password")


root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack(pady=20)

button = Button(root, text="Validate", command= lambda: validate_password(password_entry.get()))
button.pack(pady=10)

root.mainloop()