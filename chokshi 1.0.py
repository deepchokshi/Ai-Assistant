# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:29:11 2020

@author: Deep Chokshi
"""


#Creating AI assistat (Chokshi)
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    date=datetime.datetime.now().date()
    speak("Today's date is")
    speak(date)

def wishme():
    speak("Welcome Back, Deep")
    date()
    time()
    
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("Good Morning Sir!")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    
    speak("Chokshi is at your service. Please tell me how can I help you")



def Takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Lisining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("REcognizing...")
        query = r.recognize_google(audio, language="en-US")
        print (query)
    except Exception as e:
        print (e)
        print ("Say it again....")
        return "None"
    return query

Takecommand()