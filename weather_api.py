import requests
from config import API_KEY   # ✅ IMPORT REAL KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("❌ API request failed:", e)
        return {}