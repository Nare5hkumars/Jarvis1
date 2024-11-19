import requests

def get_weather(city):
    api_key = "a1f7ee7176458ea5f8061e40617b1e9e"  # Your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            temperature = main["temp"]
            weather_desc = data["weather"][0]["description"]
            return f"Temperature: {temperature}°C\nDescription: {weather_desc}"
        else:
            return "City Not Found"
    except Exception as e:
        print(f"Error in get_weather function: {e}")
        return "Error retrieving weather data"
