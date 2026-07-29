import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       audio = r.listen(source)
    try:
       voice_data = r.recognize_google(audio)
       print(voice_data)
       return voice_data
    except sr.UnknownValueError:
       print("error")
       return None
    except sr.RequestError:
       print("Request Error")
       return None



