import requests

def fetch_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

def main():
    print("Weather Fetcher")
    city = input("Enter the city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    weather = fetch_weather(city, api_key)
    if isinstance(weather, dict):
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print(weather)

if __name__ == "__main__":
    main()