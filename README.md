# Weather Application

A simple desktop weather application built with Python and Tkinter that allows users to search for current weather conditions in cities around the world.

## Overview

This Weather Application uses the OpenWeatherMap API to fetch real-time weather data for any city. The application displays:

- City name and country
- Current temperature (in both Celsius and Fahrenheit)
- Weather icon representing current conditions
- Weather description
- Humidity percentage
- Atmospheric pressure

## Features

- User-friendly graphical interface built with Tkinter
- Real-time weather data from OpenWeatherMap
- Visual weather icons
- Temperature in both Celsius and Fahrenheit
- Detailed weather information including pressure and humidity
- Error handling for invalid city names

## Prerequisites

Before running this application, you'll need:

1. Python 3.x installed on your system
2. An internet connection
3. An API key from OpenWeatherMap (a free key is already included in the config file)

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:
   ```
   pip install requests
   ```
   (Tkinter comes bundled with Python installations)

3. Ensure you have the following files in your project directory:
   - weather_app.py (main application code)
   - config.ini (contains API key)
   - img1.png (search button image)
   - weather_icons/ (directory containing weather icon images)

## Setting up the Weather Icons

The application requires weather icon images for displaying different weather conditions. You'll need to:

1. Create a folder named `weather_icons` in the project directory
2. Download the weather icons from OpenWeatherMap's website or use your own
3. Name each icon according to its icon code (e.g., 01d.png, 02d.png, etc.)

## How to Use

1. Run the application:
   ```
   python weather_app.py
   ```
2. Enter a city name in the search field
3. Click the "Search Weather" button
4. View the weather information displayed on the screen

## API Configuration

The application uses OpenWeatherMap API to fetch weather data. The API key is stored in `config.ini`. If you want to use your own API key:

1. Register at [OpenWeatherMap](https://openweathermap.org/) to get your free API key
2. Update the `config.ini` file with your key:
   ```
   [api_key]
   key=YOUR_API_KEY_HERE
   ```

## Error Handling

If the application cannot find weather data for a city (due to misspelling, non-existent city, or API issues), it will display an error message.



## Future Improvements

Potential enhancements for future versions:
- Weather forecast for upcoming days
- Search history
- Geolocation to automatically detect user's city
- Additional weather metrics (wind speed, visibility, etc.)
- Customizable themes and units



## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons from [OpenWeatherMap](https://openweathermap.org/) icon set
