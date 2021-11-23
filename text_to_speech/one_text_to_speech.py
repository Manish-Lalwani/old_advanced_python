from gtts import gTTS 

import os

text = "All Operations have been completed successfully, Thank you for using DPA Version 2 by Xcaliber Infotech"

language = 'en'

obj = gTTS(text=text,lang=language,slow=False)
obj.save('thanks_note.mp3')
os.system('mpg321 notification.mp3')
os.system('mpg321 thanks_note.mp3')