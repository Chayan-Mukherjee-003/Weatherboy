from api_handler import *


def AQI(City):
    data2=API_Call_AQI(City) #gets raw data from api_handler

    #following 6 line isolate the unique pollutant data
    so2=data2['list'][0]['components']['so2']
    no2=data2['list'][0]['components']['no2']
    pm10=data2['list'][0]['components']['pm10']
    pm2_5=data2['list'][0]['components']['pm2_5']
    o3=data2['list'][0]['components']['o3']
    co=data2['list'][0]['components']['co']
    so2_v,no2_v,pm10_v,pm2_5_v,o3_v,co_v=0,0,0,0,0,0
    
    #predefined classes extracted from API website
    classes=[[(0,20),(20,80),(80,250),(250,350)],
             [(0,40),(40,70),(70,150),(150,200)],
             [(0,20),(20,50),(50,100),(100,200)],
             [(0,10),(10,25),(25,50),(50,75)],
             [(0,60),(60,100),(100,140),(140,180)],
             [(0,4400),(4400,9400),(9400,12400),(12400,15400)]]    
    
    #value check function defenition
    def val_check(i,var):
        if classes[i][0][0]<=var<classes[i][0][1]:
            var_v=1
        elif classes[i][1][0]<=var<classes[i][1][1]:
            var_v=2
        elif classes[i][2][0]<=var<classes[i][2][1]:
            var_v=3
        elif classes[i][3][0]<=var<classes[i][3][1]:
            var_v=4
        elif var>=classes[i][3][1]:
            var_v=5
        return var_v
    
    #setting values using value check function
    so2_v=val_check(0,so2)
    no2_v=val_check(1,no2)
    pm10_v=val_check(2,pm10)
    pm2_5_v=val_check(3,pm2_5)
    o3_v=val_check(4,o3)
    co_v=val_check(5,co)
    
    vL=[so2_v,no2_v,pm10_v,pm2_5_v,o3_v,co_v]

    AQI=''
    check=max(vL)

    #checks the maximum values of the polutants and assigns AQI accordingly
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
