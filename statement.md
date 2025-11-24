# Weatherboy - Project Statement

## Problem Statement

In modern cities, access to real time weather conditions and air quality data is essential for safety, travel planning and health awareness. Although many applications exist that achieve similar results, sometimes users simply need quick data retrieval without navigating through multiple screens or interfaces. A lightweight terminal based program that fetches weather and AQI data can serve as straightforward utility for learning purposes or basic usage. This project aims to implement such a system using Python and OpenWeatherAQ API.

## Scope of the Project

This project aims to develop a simple command-line based Weather and Air Quality Information system using Python. It allows the user to input a City name and retrieve current weather details, air pollution levels and short term forecasts using OpenWeatherMap's publicly available APIs.

The goal is not to replace already existing Apps but to build a small scale simple rendition of those apps aimed at users who wish to learn how the backend of these apps function and to demonstrate practical usage of API calls as well as data extraction in Python via a small-scale project.

## Inclusions (What the system does)

1. **Current Weather Details**
   - Gives current weather condition
   - Provides feels-like temprature, humidity, pressure and visibiltiy.

2. **Air Quality Index Retrieval**
   - Retrieves pollutant levels such as SO2 and NO2
   - Uses predefined thresholds provided by the API website to classify the levels into set categories such as Good, Fair, Moderate, Poor and Very Poor

3. **Combined Weather + AQI Report**
   - Combines the Current Weather Details and Air Quality Results into one message for a single city

4. **3-Hour Forecast**
   - Displays Short term forecast entries for various times of the day (Multiples of 3, i.e., 15:00, 18:00, etc)
   - Includes temprature, humidity, pressure, visibilty and weather condition

5. **Text Based User Interface**
   - Menu driven terminal interface
   - User selects option using numerical indexing
   - Programs runs in a loop until the user chooses to exit

## Target Users

- **Students**: Practicing Python, API Handling, or simple terminal application devlopment
- **Beginners in Programming**: Learning modular code structure and Function Based design
- **Users who prefer Terminal tools**: Those comfortable with text based utilities
- **Devlopers**: Those looking for a minimal example of integrating with a REST API

## High-Level Features

1. **Weather Retrieval via API Calls**: Fetches Real time weather data
2. **AQI Calculations Based on Thresholds**: Categorizes air quality using pollutant values
3. **Combined Report Output**: Display multiple data types together
4. **Short term Forecast Display**: Shows upcoming forecast entries
5. **Reusable Code Structure**: Weather and AQI logic grouped in two seperate Modules
6. **No External Dependencies except 'requests' and 'time' library**: 
7. **Cross-platform Compatibility**: Works on Windows, Mac, and Linux systems
8. **User-friendly Interface**: Simple menu system for easy navigation