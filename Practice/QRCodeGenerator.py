##pip install pypng
#########################
from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate_qr_code():
    link_name = name_entry.get()
    link_url = link_entry.get()
    filename = link_name + ".png"
    
    url = pyqrcode.create(link_url)
    url.png(filename, scale=6)
    img = ImageTk.PhotoImage(Image.open(filename))    
    img_label = Label(root, image=img)
    img_label.image = img
    canvas.create_window(200, 400, window=img_label)

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_Label = Label(root, text='QR Code Generator', fg='lightblue', font=('Arial', 20))
canvas.create_window(200, 50, window=app_Label) 

name_Label = Label(root, text='Link Name')
link_Label = Label(root, text='Link')
canvas.create_window(200, 100, window=name_Label)
canvas.create_window(200, 160, window=link_Label)   

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(text='Generate QR Code', command=lambda: generate_qr_code())
canvas.create_window(200, 220, window=button)

root.mainloop()
