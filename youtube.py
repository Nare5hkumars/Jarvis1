import pywhatkit
import pyttsx3

def search_youtube(query):
    engine = pyttsx3.init()
    engine.say(f"Searching YouTube for {query}")
    engine.runAndWait()
    pywhatkit.playonyt(query)
