import webbrowser
import pyttsx3
import time

def open_colab():
    engine = pyttsx3.init()
    engine.say("Opening Google Colab")
    engine.runAndWait()
    webbrowser.open("https://colab.research.google.com/")
    time.sleep(5)  # Wait for the browser to open

def run_colab_file(file_name):
    engine = pyttsx3.init()
    engine.say(f"Running {file_name} in Google Colab")
    engine.runAndWait()
    # Assuming the file is already uploaded to Google Drive and accessible in Colab
    colab_url = f"https://colab.research.google.com/drive/{file_name}"
    webbrowser.open(colab_url)
