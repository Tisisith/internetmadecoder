from tkinter import *
from pytube import Youtube
from tkinter import filedialog
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading....")
    mp4 = Youtube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    #code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    shutil.move('audio.mp3',file_path)
    audio_file.close()
    video_clip.close()
    shutil.move(mp4,file_path)
    print("Download complete")


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)



root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400,height=300)
canvas.pack()

#app label
app_label = Label(root,text="Video downloader",fg='blue',font=("Arial",20))
canvas.create_window(200,220, window=app_label)

#entry to accept video url
url_label = Label(root,text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200,80, window=url_label)
canvas.create_window(200,100, window=url_entry)

#path to download videos
path_label = Label(root,text="Select path to download")
path_button = Button(root,text="Select",command=get_path)
canvas.create_window(200,150, window=path_label)
canvas.create_window(200,170, window=path_button)

#download button

download_button = Button(root,text="Download",command=download)
canvas.create_window(200,250, window=path_button)

root.mainloop()