import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return ""

def process_command(command):
    if 'Wikipedia' in command:
        speak("Searching Wikipedia...")
        command = command.replace("Wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I can only search Wikipedia for now.")
    return True

def main():
    speak("Hello, I am JARVIS. How can I help you today?")
    while True:
        command = listen()
        if not process_command(command):
            break

if __name__ == "__main__":
    main()
