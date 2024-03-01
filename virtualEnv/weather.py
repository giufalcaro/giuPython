import os
from pprint import pprint

import requests
from dotenv import load_dotenv

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API key}&units=metric

load_dotenv()


def getCurrentWeather():
    print("....")
    city = input("enter a city name: ")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&appid={os.getenv('API_KEY')}&q={city}"

    watherData = requests.get(request_url).json()

    if not watherData["cod"] == 200:
        print("city not found")
        return

    print(
        f"\nCurrent weather for {watherData['name']}: the temp is {watherData['main']['temp']}"
    )
    print(f"\nFeels like {watherData['main']['feels_like']}")


if __name__ == "__main__":
    getCurrentWeather()
