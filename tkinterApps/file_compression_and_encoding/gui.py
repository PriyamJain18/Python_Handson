import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from compressmodule import compress, decompress  

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    return file_name

def compression(i, o):
    if(i and o):
        compress(i, o)
    else:
        tk.messagebox.showinfo("Error", "Please enter both input and output file names.")

def decompression(i, o):
    if(i and o):
        decompress(i, o)
    else:
        tk.messagebox.showinfo("Error", "Please enter both input and output file names.")

def checkbox_action():
    global compressedfile  
    compressedfile.delete(0, tk.END)
    if var.get() and outputfile.get():
        cfile = outputfile.get()
        compressedfile.insert(0,cfile)
    elif not var.get():
        pass
    else:
        messagebox.showinfo("Error", "Please enter the compressed file name above.")

# Create the main window
window = tk.Tk()
window.title("File Compression and Encoding Tool")
window.geometry('600x400')

# Create Frame
frame = tk.Frame(window,  background='lightblue', padx=10, pady=10)
frame.grid(row=0, column=0)

# Create input fields and labels to get name of the file to be compressed and the name of the output file
inputfile = tk.Entry(frame)
inputfile_label = tk.Label(frame, text="Name of the file to be compressed") 
outputfile = tk.Entry(frame)  
outputfile_label = tk.Label(frame, text="Compressed File Name")   

# Place the widgets in the window
inputfile.grid(row=0, column=1)
inputfile_label.grid(row=0, column=0)
outputfile.grid(row=1, column=1)
outputfile_label.grid(row=1, column=0)

#Widgets for decompression
var = tk.BooleanVar()
compressedfile = tk.Entry(frame)
compressedfile_label = tk.Label(frame, text="Name of the compressed file")
compressedfile_checkbox = tk.Checkbutton(frame, text="Is the compressed file same as mentioned above?", variable=var, command=checkbox_action)
decompressfile = tk.Entry(frame)
decompressfile_label = tk.Label(frame, text="Decompressed File Name")

# Place the widgets in the window
compressedfile.grid(row=3, column=1)
compressedfile_label.grid(row=3, column=0)
compressedfile_checkbox.grid(row=3, column=2)
decompressfile.grid(row=4, column=1)
decompressfile_label.grid(row=4, column=0)


# Create buttons to trigger compression and decompression
button = tk.Button(frame, text="Compress", command=lambda: compression(inputfile.get(), outputfile.get()))
button.grid(row=2, column=1)
button2 = tk.Button(frame, text="Decompress", command=lambda: decompression(compressedfile.get(), decompressfile.get()))
button2.grid(row=5, column=1)   


# Compression and Decompression using file dialog
frame1 = tk.Frame(window,  background='lightgreen', padx=10, pady=10)
frame1.grid(row=6, column=0)

button3 = tk.Button(frame1, text="Compress File from Computer", command=lambda: compression(open_file(), 'compressedFile.txt'))
button3.grid(row=6, column=0)

button4 = tk.Button(frame1, text="Decompress File from Computer", command=lambda: decompression(open_file(), 'decompressedFile.txt'))
button4.grid(row=7, column=0)

window.mainloop()