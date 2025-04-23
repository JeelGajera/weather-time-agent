import datetime
from google.adk.agents import Agent
from .utils import fetch_weather_data, fetch_current_time


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    try:
        weather_data = fetch_weather_data(city)
        if weather_data["cod"] != 200:
            return {
                "status": "error",
                "error_message": f"Error fetching weather data: {weather_data['message']}",
            }
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        sunrise = weather_data["sys"]["sunrise"]
        sunset = weather_data["sys"]["sunset"]
        report = (
            f'The current weather in {city} is {weather} with a temperature of {temperature}K, feels like {feels_like}K, '
            f'humidity of {humidity}%, and wind speed of {wind_speed} m/s.'
            f'\nSunrise at {datetime.datetime.fromtimestamp(sunrise).strftime("%Y-%m-%d %H:%M:%S")} '
            f'and sunset at {datetime.datetime.fromtimestamp(sunset).strftime("%Y-%m-%d %H:%M:%S")}.'
        )
        return {"status": "success", "report": report}

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching weather data: {str(e)}",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    try:
        time_info = fetch_current_time(city)
        if time_info["cod"] != 200:
            return {
                "status": "error",
                "error_message": f"Error fetching timezone data: {time_info['error_message']}",
            }
        timezone_offset = time_info["timezone"]
        # Convert UTC time to local time using the timezone offset
        utc_time = datetime.datetime.utcnow()
        local_time = utc_time + datetime.timedelta(seconds=timezone_offset)
        local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
        # Format the local time string
        local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
        return {
            "status": "success",
            "result": f"The current time in {city} is {local_time_str}.",
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching timezone data: {str(e)}",
        }


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
