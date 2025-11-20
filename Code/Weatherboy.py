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
    client=OpenAQ(api_key='3df5c2816c9ddee6d567bdfc5ccd5cf2e1bb1973b2d7bcaf60ea3af59b632189')
    location=client.locations.list()
    client.close()
    print(location)

def Weather_AQI_Combined():
    return "Combined"

def History():
    return "History"

def Analytics():
    return "Analytics and Insight"