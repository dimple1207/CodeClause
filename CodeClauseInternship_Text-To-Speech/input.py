import pyttsx3
import tkinter as tk

window = tk.Tk()
creative_label = tk.Label(window, text="🌈 Welcome to the Creative Text-to-Speech text_speech! 🌟")
creative_label.pack()

def convert_to_speech():
    answer = entry.get()
    text_speech.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")  # Use a female voice (adjust the voice ID if needed)
    text_speech.say(answer)
    text_speech.runAndWait()

# Initializing text-to-speech engine
text_speech = pyttsx3.init()

# Creating a Tkinter window

window.title("Text to Speech by Dimple")

# Creating a label and entry for user input
label = tk.Label(window, text="Enter text:")
label.pack()

entry = tk.Entry(window, width=150) 
entry.pack()

# Creating a button to trigger text-to-speech conversion
button = tk.Button(window, text="Convert to Speech", command=convert_to_speech)
button.pack()


# Closing message
closing_label = tk.Label(window, text="Made with ❤ by Dimple")
closing_label.pack()

# Runing the Tkinter event loop
window.mainloop()

