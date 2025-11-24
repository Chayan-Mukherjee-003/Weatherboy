from api_handler import *
from weather_services import *
from AQI import *

def Weather_AQI_Combined(City):
    #for current Weather:
    L=Current_Weather(City)
    Return=[]
    Return.append(f"Current Weather:{L['weather']}")
    Return.append(f"Actual Current Temprature:{L['temprature']['temp']} C")
    Return.append(f"Feels like:{L['temprature']['feels_like']} C")
    Return.append(f"Pressure:{L['temprature']['pressure']}")
    Return.append(f"Humidity:{L['temprature']['humidity']}")
    Return.append(f"Visibility:{L['visibility']}")

    #for AQI:
    Aq=f"Weather quality of the City is {AQI(City)}"
    Return.append(Aq)

    return Return


def Forecast_3hr(city):
    data=API_Call_Forecast()
    List_raw=data['list']
    Return_data=[]
    for i in range(3):
        list=List_raw[i]
        weather=list['weather'][0]['main']
        temp_v=list['main']
        visibility=list['visibility']
        wind=list['wind']
        date=list['dt_txt']
        Return_data.append({'date':date,'weather':weather,'temprature':temp_v,'visibility':visibility,'wind':wind})
    return Return_data