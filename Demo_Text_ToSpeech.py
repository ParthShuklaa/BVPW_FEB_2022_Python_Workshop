from gtts import gTTS
import os
myText = "I Hope You are learning Python "

myobj = gTTS(myText,lang='en',slow= True)
myobj.save("Message1.mp3")
os.system("Message1.mp3")
"""
Step1: Import gtts package using Python package OPtion 
Step2: Import gTTS from gtts along with os
Step3: Calling COnstructor of gTTS() with Default values 
Step4: sAVING fILE AS MP3
Step5: calling Mp3 File 

"""