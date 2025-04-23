import requests
import os


def fetch_weather_data(location: str) -> dict:
    """
    Fetch weather data from OpenWeatherMap API.

    Args:
        location (str): The location for which to fetch the weather data.

    Returns:
        dict: Weather data for the specified location.
    """
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Error fetching weather data: {response.status_code}, message: {response.text}")


def fetch_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    else:
        raise Exception(
            f"Error fetching timezone data: {response.status_code}, message: {response.text}")
