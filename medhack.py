import sys
import re
import os.path
import os
import playsound
import time
import datetime

import speech_recognition as sr
from gtts import *

# med_name = str

# total_med = int

# day_dose = int

def Response(text):
    "speaks audio passed as argument"
    print(text)
    file = gTTS(text = text, lang = "en")
    filename = 'temp.mp3'
    file.save(filename)

    playsound.playsound(filename)
        
    os.remove(filename)



def myCommand():
    #"listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = ""
        print('Done')
    try:
        command = r.recognize_google(audio).lower()
       
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def name(command):
    if 'The name is' in command:
        drug = ('The name is(.*)', command)
        if drug:
            name_drug = drug
            Response('ok')  
            
def total(command):
    if 'The total amount is' in command:
        reg_ex = re.search('The total amount is(.*)', command)
        if reg_ex:
            total_drug = reg_ex.group(1) 
            Response('ok')            
            
Response('Hi User, welcome today i am so pleased to have you here today, please feel free to tell me about your medications. Thanks.')

text = myCommand() 


if 'hello' in text:
    Response('The pleasure is mine')
    
Response('What is the name of your medication')


myCommand()
name()

    
Response('what is the total amount of your medication')

myCommand()
total(myCommand)
# def med(command):
#     if int in command:
#         Response('ok')


        
if int in text:
    Response('ok')
    
Response('what is the daily dosage of your medication')


