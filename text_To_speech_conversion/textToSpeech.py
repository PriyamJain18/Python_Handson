from gtts import gTTS
import os

text= open('demo.txt', 'r').read()

#google speech language codes: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
output = gTTS(text=text, lang='en', slow=False)
output.save("output.mp3")

os.system("start output.mp3")  # For Windows. Use "afplay" for MacOS or "xdg-open" for Linux. 
