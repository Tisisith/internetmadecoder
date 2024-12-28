from gtts import gTTS
import os
from tkinter import *
root = Tk()
def text_to_speech():
    text = entry.get()
    gtts = gTTS(text=text,lang='en',slow=False)
    gtts.save('user_text.mp3')
    os.system('afplay user_text.mp3')
              


canvas = Canvas(root,width=400,height=300)
canvas.pack()
entry = Entry(root)
canvas.create_window(200,100,window=entry)

button = Button(root,text="Start converting",command=text_to_speech)
canvas.create_window(200,130,window=button)

root.mainloop()