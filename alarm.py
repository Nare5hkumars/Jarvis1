import datetime
import time
import pyttsx3
import webbrowser
import speech_recognition as sr


def set_alarm(alarm_time, song_url):
    engine = pyttsx3.init()
    engine.say(f"Alarm set for {alarm_time}")
    engine.runAndWait()
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            engine.say("Wake up! It's time to start your day!")
            engine.runAndWait()
            webbrowser.open(song_url)
            break
        time.sleep(30)  # Check every 30 seconds

def get_alarm_time():
    engine = pyttsx3.init()
    engine.say("Please tell me the alarm time in HH:MM format.")
    engine.runAndWait()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for alarm time...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        alarm_time = recognizer.recognize_google(audio)
        print(f"Alarm time set for: {alarm_time}")
        return alarm_time
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None
