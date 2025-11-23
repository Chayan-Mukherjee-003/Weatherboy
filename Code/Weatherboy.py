import requests

def Current_Weather(City):
    if City=='':
        City = input("Enter City:")
    key='70f99925cc89d99f50c781fc0765ea06'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}&units=metric"
    response=requests.get(url)
    data=response.json()
    weather=data['weather'][0]['main']
    temp_v=data['main']
    visibility=data['visibility']
    wind=data['wind']
    return {'weather':weather,'temprature':temp_v,'visibility':visibility,'wind':wind}

def AQI(City):
    if City=='':
        City = input("Enter City:")
    key='70f99925cc89d99f50c781fc0765ea06'
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=5&appid={key}"
    response=requests.get(url)
    data=response.json()
    lat,lon=data[0]["lat"],data[0]["lon"]
    url2=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"
    response2=requests.get(url2)
    data2=response2.json()

    so2=data2['list'][0]['components']['so2']
    no2=data2['list'][0]['components']['no2']
    pm10=data2['list'][0]['components']['pm10']
    pm2_5=data2['list'][0]['components']['pm2_5']
    o3=data2['list'][0]['components']['o3']
    co=data2['list'][0]['components']['co']
    so2_v,no2_v,pm10_v,pm2_5_v,o3_v,co_v=0,0,0,0,0,0
    
    classes=[[(0,20),(20,80),(80,250),(250,350)],
             [(0,40),(40,70),(70,150),(150,200)],
             [(0,20),(20,50),(50,100),(100,200)],
             [(0,10),(10,25),(25,50),(50,75)],
             [(0,60),(60,100),(100,140),(140,180)],
             [(0,4400),(4400,9400),(9400,12400),(12400,15400)]]    
    
    #value check for so2

    #idea for optimization: make a small function with the indexes as inputs. should clean up the clutter below. 
    if classes[0][0][0]<=so2<classes[0][0][1]:
        so2_v=1
    elif classes[0][1][0]<=so2<classes[0][1][1]:
        so2_v=2
    elif classes[0][2][0]<=so2<classes[0][2][1]:
        so2_v=3
    elif classes[0][3][0]<=so2<classes[0][3][1]:
        so2_v=4
    elif so2>=classes[0][3][1]:
        so2_v=5

    #same logic as so2 value check with modified list index to check for the other variables
    if classes[1][0][0]<=no2<classes[1][0][1]:
        no2_v=1
    elif classes[1][1][0]<=no2<classes[1][1][1]:
        no2_v=2
    elif classes[1][2][0]<=no2<classes[1][2][1]:
        no2_v=3
    elif classes[1][3][0]<=no2<classes[1][3][1]:
        no2_v=4
    elif no2>=classes[1][3][1]:
        no2_v=5
    
    if classes[2][0][0]<=pm10<classes[2][0][1]:
        pm10_v=1
    elif classes[2][1][0]<=pm10<classes[2][1][1]:
        pm10_v=2
    elif classes[2][2][0]<=pm10<classes[2][2][1]:
        pm10_v=3
    elif classes[2][3][0]<=pm10<classes[2][3][1]:
        pm10_v=4
    elif pm10>=classes[2][3][1]:
        pm10_v=5

    if classes[3][0][0]<=pm2_5<classes[3][0][1]:
        pm2_5_v=1
    elif classes[3][1][0]<=pm2_5<classes[3][1][1]:
        pm2_5_v=2
    elif classes[3][2][0]<=pm2_5<classes[3][2][1]:
        pm2_5_v=3
    elif classes[3][3][0]<=pm2_5<classes[3][3][1]:
        pm2_5_v=4
    elif pm2_5>=classes[3][3][1]:
        pm2_5_v=5

    if classes[4][0][0]<=o3<classes[4][0][1]:
        o3_v=1
    elif classes[4][1][0]<=o3<classes[4][1][1]:
        o3_v=2
    elif classes[4][2][0]<=o3<classes[4][2][1]:
        o3_v=3
    elif classes[4][3][0]<=o3<classes[4][3][1]:
        o3_v=4
    elif o3>=classes[4][3][1]:
        o3_v=5

    if classes[5][0][0]<=co<classes[5][0][1]:
        co_v=1
    elif classes[5][1][0]<=co<classes[5][1][1]:
        co_v=2
    elif classes[5][2][0]<=co<classes[5][2][1]:
        co_v=3
    elif classes[5][3][0]<=co<classes[5][3][1]:
        co_v=4
    elif co>=classes[5][3][1]:
        co_v=5
    
    vL=[so2_v,no2_v,pm10_v,pm2_5_v,o3_v,co_v]
    AQI=''
    check=max(vL)
    if check==1:
        AQI='Good'
    elif check==2:
        AQI='Fair'
    elif check==3:
        AQI='Moderate'
    elif check==4:
        AQI='Poor'
    elif check==5:
        AQI='Very Poor'

    return AQI

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

def History(): #implement using CSV or not at all, seems rudementary to implement. Check later
    return "History"

def Forecast(city):
    #maybe i should add this block of code(150 to 155) in a seperate function like 'API_Call()' or something, ive called it thrice already
    if city=='':
        city = input("Enter City:")
    key='70f99925cc89d99f50c781fc0765ea06'
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"
    response=requests.get(url)
    data=response.json()
    return data #working now, forgot the 'f' instead of f string