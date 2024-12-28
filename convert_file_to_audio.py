from gtts import gTTS
import os
text = "Now, being without you is all a big mistake, instead of getting it easier it's the hardest thing to take."
output= gTTS(text=text,lang="en",slow=False)
output.save('output.mp3')
os.system("afplay output.mp3")