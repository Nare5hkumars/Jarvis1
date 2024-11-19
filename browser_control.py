import webbrowser
import pyautogui

def search_browser(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    pyautogui.sleep(5)  # Give the browser some time to open
    pyautogui.write(query)
    pyautogui.press('enter')

