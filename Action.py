import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    if not data:
        response = "I did not hear anything. Please try again."
        text_to_speech.text_to_speech(response)
        return response
    
    user_data = data.lower().strip()
    
    try:
        if "what is your name" in user_data:
            response = "My name is AI assistant"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "hello" in user_data or "hye" in user_data:
            response = "Hey sir, how can I help you?"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "good morning" in user_data:
            response = "Good morning! How can I assist you?"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "time now" in user_data or "what is the time" in user_data:
            current_time = datetime.datetime.now()
            response = f"Current time is {current_time.hour} hours and {current_time.minute} minutes"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "shutdown" in user_data:
            response = "Okay, shutting down"
            text_to_speech.text_to_speech(response)
            return "ok mam"
            
        elif "play music" in user_data or "playmusic" in user_data:
            webbrowser.open_new_tab("https://www.gaana.com/")
            response = "Opening Gaana music service for you"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "youtube" in user_data:
            webbrowser.open_new_tab("https://www.youtube.com/")
            response = "Opening YouTube for you"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "open google" in user_data or "google" in user_data:
            webbrowser.open_new_tab("https://www.google.com/")
            response = "Opening Google for you"
            text_to_speech.text_to_speech(response)
            return response
            
        elif "weather" in user_data:
            try:
                weather_info = weather.weather()
                if weather_info:
                    response = f"The weather is: {weather_info}"
                    text_to_speech.text_to_speech(response)
                    return response
                else:
                    response = "Unable to fetch weather information"
                    text_to_speech.text_to_speech(response)
                    return response
            except Exception as e:
                response = "Unable to fetch weather information"
                text_to_speech.text_to_speech(response)
                return response
        else:
            response = "I did not understand that. Please try again."
            text_to_speech.text_to_speech(response)
            return response
            
    except Exception as e:
        print(f"Error in Action: {str(e)}")
        response = "An error occurred. Please try again."
        text_to_speech.text_to_speech(response)
        return response














