import requests
from openaq import OpenAQ

def Current_Weather():
    key='70f99925cc89d99f50c781fc0765ea06'
    City = input("Enter City:")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}&units=metric"
    response=requests.get(url)
    data=response.json()
    weather=data['weather'][0]['main']
    temp_v=data['main']
    visibility=data['visibility']
    wind=data['wind']
    return {'weather':weather,'temprature':temp_v,'visibility':visibility,'wind':wind}
def AQI():
    City=input("Enter City:")
    key='70f99925cc89d99f50c781fc0765ea06'
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=5&appid={key}"
    response=requests.get(url)
    data=response.json()
    lat,lon=data[0]["lat"],data[0]["lon"]
    url2=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"
    response2=requests.get(url2)
    data2=response2.json()
    print(data2)

def Weather_AQI_Combined():
    return "Combined"

def History():
    return "History"

def Analytics():
    return "Analytics and Insight"