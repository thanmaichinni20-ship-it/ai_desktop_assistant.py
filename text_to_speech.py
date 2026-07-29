import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 80)
    engine.say(text)
    engine.runAndWait()