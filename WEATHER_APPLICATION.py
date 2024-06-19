
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    location = input("Enter the city name or ZIP code: ")
    
    weather_data = get_weather(api_key, location)
    
    if weather_data['cod'] == 200:
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")
    else:
        print("Error: City not found. Please check the name or ZIP code and try again.")

if __name__ == "_main_":
    main()
