import requests
import json


key="70f99925cc89d99f50c781fc0765ea06"

def API_Call_Current_Weather(City):
    if City=='':
        City = input("Enter City:")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}&units=metric"
    response=requests.get(url)
    data=response.json()
    return data

def API_Call_AQI(City):
    if City=='':
        City = input("Enter City:")
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=5&appid={key}"
    response=requests.get(url)
    data=response.json()
    lat,lon=data[0]["lat"],data[0]["lon"]
    url2=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"
    response2=requests.get(url2)
    data2=response2.json()
    return data2

def API_Call_Forecast(city):
    if city=='':
        city = input("Enter City:")
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=metric"
    response=requests.get(url)
    data=response.json()
    return data