from text_to_speech import speak
import speech_recognition as sr
from weather import get_weather
from browser_control import search_browser
from wikipedia_search import search_wikipedia

def take_command():
    recognizer = sr.Recognizer()
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

if __name__ == "__main__":
    speak("How can I help you, sir?")
    while True:
        try:
            print("Taking command...")
            query = take_command().lower()
            print(f"Command received: {query}")
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = search_wikipedia(query)
                speak("According to Wikipedia")
                speak(results)
            elif 'weather' in query:
                speak('Which city?')
                city = take_command().lower()
                print(f"City received: {city}")
                weather_info = get_weather(city)
                speak(weather_info)

            elif 'search' in query:
                speak('What do you want to search for?')
                search_query = take_command().lower()
                speak(f'Searching for {search_query}')
                search_browser(search_query)

            elif 'exit' in query:
                speak("Goodbye!")
                break
        except Exception as e:
            print(f"Error in main loop: {e}")

