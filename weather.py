import requests

def weather():
    city = "Andhra Pradesh"
    url = f"https://wttr.in/{city}?format=%t+%C"
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return "Weather service unavailable"