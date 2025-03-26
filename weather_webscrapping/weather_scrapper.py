import requests

def get_weather(city):
    # Open-Meteo API for Poland
    url = "https://api.open-meteo.com/v1/forecast?latitude=0&longitude=0&current_weather=true"
    
    # Get latitude & longitude from Open-Meteo geocoding
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response or not geo_response["results"]:
        print("❌ Invalid city name. Try again.")
        return

    latitude = geo_response["results"][0]["latitude"]
    longitude = geo_response["results"][0]["longitude"]

    # Fetch weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url).json()
    
    # Extract weather details
    weather = weather_response["current_weather"]
    
    print(f"\n📍 Location: {city}")
    print(f"🌡️ Temperature: {weather['temperature']}°C")
    print(f"💨 Wind Speed: {weather['windspeed']} km/h")
    print(f"☁️ Weather Code: {weather['weathercode']}\n")

# Ask for a Polish city
city_name = input("Enter a city name (e.g., Warsaw, Kraków, Gdańsk): ")
get_weather(city_name)