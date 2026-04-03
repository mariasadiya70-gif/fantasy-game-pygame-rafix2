import requests
import json

class WeatherDashboard:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        complete_url = f"{self.base_url}?q={{city}}&appid={{self.api_key}}&units=metric"
        response = requests.get(complete_url)
        return response.json()

    def display_weather(self, city):
        weather_data = self.get_weather(city)
        if weather_data['cod'] != 200:
            print(f"City {city} not found!")
            return
        main = weather_data['main']
        weather = weather_data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Humidity: {main['humidity']}%")
        print(f"Description: {weather['description']}\n")

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    dashboard = WeatherDashboard(api_key)
    city = input('Enter city name: ')
    dashboard.display_weather(city)