from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    if not video_path or not file_path:
        print("Please provide a video URL and download path.")
        return
    print("Downloading...")
    try:
        # Download video
        mp4 = YouTube(video_path).streams.get_highest_resolution().download()
        video_clip = VideoFileClip(mp4)
        
        # Extract audio
        audio_file = video_clip.audio
        audio_file.write_audiofile('audio.mp3')
        shutil.move('audio.mp3', file_path)
        
        audio_file.close()
        video_clip.close()
        shutil.move(mp4, file_path)
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", fg='blue', font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)

# Entry to accept video URL
url_label = Label(root, text="Enter video URL:")
url_entry = Entry(root, width=40)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# Path to download videos
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)

# Download button
download_button = Button(root, text="Download", command=download)
canvas.create_window(200, 250, window=download_button)

root.mainloop()
