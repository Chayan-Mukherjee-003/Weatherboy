from api_handler import *

def Current_Weather(City):
    data=API_Call_Current_Weather(City)
    weather=data['weather'][0]['main']
    temp_v=data['main']
    visibility=data['visibility']
    wind=data['wind']
    return {'weather':weather,'temprature':temp_v,'visibility':visibility,'wind':wind}