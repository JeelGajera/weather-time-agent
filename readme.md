# Weather-Time Agent

The Weather-Time Agent is a simple agent application that uses the OpenWeatherMap API and Google Agent Development Kit (ADK) to provide weather and time-related information. This agent can be used to fetch current weather conditions and time for a specified location.

## Features

- Fetch current weather information using OpenWeatherMap API.
- Retrieve the current time for a specified location.
- Built using the Google Agent Development Kit (ADK) for easy integration.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7 or higher**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. **Google Agent Development Kit (ADK)**: Follow the instructions on the [Google ADK documentation](https://google.github.io/adk-docs/) to set up the ADK environment.
2. **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate an API key.

## Setup Instructions

1. Install the required dependencies:
    ```bash
    pip install google-adk
    ```

2. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```env
    OPEN_WEATHER_API_KEY=your_openweathermap_api_key
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=your_google_api_key
    ```

## How to Use

1. Invoke the agent using your google-adk `adk web` command.
    ```bash
    adk web
    ```

2. Open your web browser and navigate to the local server (usually `http://localhost:8080`).
3. Use the agent by typing or speaking your queries in the chat interface.
4. Ask questions like:
    - "What's the weather in Ahmedabad?"
    - "What time is it in Tokyo?"

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/)
- [Google Agent Development Kit](https://google.github.io/adk-docs/)