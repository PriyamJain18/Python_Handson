from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox  

def buttonClicked():
    if not entry.get().strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    text = entry.get()
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False )
    speech.save("textToSpeech.mp3")
    os.system("start textToSpeech.mp3")

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(100, 100, window=entry)

button = Button(text="Start", command=buttonClicked, bg='brown', fg='white')
canvas.create_window(100, 130, window=button)

root.mainloop()