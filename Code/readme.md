# Password Strength Checker & Generator

A Python-based application to check weather and Air Quality

## Features

- **Current Weather Details**: Calls an API and gets current Weather Details
- **Air Quality**: Calls a similar API to get Air Quality and rates it on a scale (Good>Fair>Moderate>Poor>Very_Poor)
- **3hr forecast**: Displays the temprature and other details for 3 times of the day(9 AM, 12 noon and 3 PM)

## Requirements

- Python 3.x
- requests library

## Installation

1. Download the project files
2. Ensure Python 3.x is installed on your system
3. Install requests library

## How to Run

```bash
python Terminal.py
```

## Usage

### Menu Options

1. **Check Current Temprature**
   - Enter any city name
   - Get Current Temprature, What it feels like, Pressure, Humidity and Visibility values

2. **Check Air Quality**
   - Enter any city name
   - Get the current air quality in 5 classes, Good>Fair>Moderate>Poor>Very_Poor

3. **Exit**
   - Close the application


## Project Structure

```
password-checker/
│
├── Run.py                # Main application file with GUI
├── AQI.py                # Air Quality related Code
├── weather_services.py   # Current Weather Code
├── utilities.py          # Combined function + 3 hr forecast
└── README.md             # Project documentation
```

## Python Concepts Used

- Functions
- Dictionaries
- Loops (for, while)
- Conditionals (if-elif-else)
- Error Handling (try-except)
- User input/output
- Lists and iteration
- String manipulation (f strings)
