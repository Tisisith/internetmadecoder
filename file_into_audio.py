from gtts import gTTS
import os

text = open('speech.txt','r').read()

language="en"
output= gTTS(text=text,lang=language,slow=True)
output.save('hindi.mp3')
os.system("afplay hindi.mp3")