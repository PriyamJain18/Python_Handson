#pip install pytube
#pip install moviepy

from moviepy import VideoFileClip
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    if(not video_path):
        path_label.config(text="Please enter a valid YouTube URL")
        return
    mp4 = YouTube(video_path).streams.get_highest_resolution().download(file_path)
    video_clip = VideoFileClip(mp4)

    #code for mp3
    audio_file = video_clip
    audio_file.write_audiofile(mp4.replace(".mp4", ".mp3")) 
    audio_file.close()
    shutil.move(mp4.replace(".mp4", ".mp3"), file_path) 

    #code for mp4
    video_clip.close()
    shutil.move(mp4, file_path)
    path_label.config(text="Download complete!")

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=500, height=500)
canvas.pack()

#app label
app_Label = Label(root, text="Video DownLoader", fg="blue", font=("Arial", 20))
canvas.create_window(250, 50, window=app_Label)

#entry to accept video url
url_entry = Entry(root)
url_label = Label(root, text="Enter Video URL")
canvas.create_window(250, 100, window=url_label)
canvas.create_window(250, 130, window=url_entry)

#path where you want to download videos
path_label = Label(root, text="Select Path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(250, 170, window=path_label)
canvas.create_window(250, 200, window=path_button)  

#download button
download_button = Button(root, text="Download", command=download_video)
canvas.create_window(250, 250, window=download_button)

root.mainloop()