from datetime import datetime
import pyttsx3

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_current_date():
    today = datetime.today()
    current_date = today.strftime("%B %d, %Y")
    return current_date

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
