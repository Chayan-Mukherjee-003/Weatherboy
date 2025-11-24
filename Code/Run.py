import weather_services
import utilities
import AQI
import time

#loop so function runs indefinitely untill stopped by user.
while True:

    # Menu:
    print("=====Weatherboy Terminal System====")
    print("1. Get Current Weather")
    print("2. Get Air Quality Index(AQI)")
    print("3. Weather + AQI Combined Report")
    print("4. Forecast for 3 hrs")
    print("5. Exit")
    print("===================================")
    
    #input for above menu:
    inp=int(input("Enter choice:"))


    #logic to check which choice was made:
    if inp==1:
        L=weather_services.Current_Weather('')
        print(f"Current Weather:{L['weather']}")
        print(f"Actual Current Temprature:{L['temprature']['temp']} C")
        print(f"Feels like:{L['temprature']['feels_like']} C")
        print(f"Pressure:{L['temprature']['pressure']} hPa")
        print(f"Humidity:{L['temprature']['humidity']} %")
        print(f"Visibility:{L['visibility']} meters")
    elif inp==2:
        print(f"Weather quality of the City is {AQI.AQI('')}")
    elif inp==3:
        city=input("Enter City Name:")
        L=utilities.Weather_AQI_Combined(city)
        for i in L:
            print(i)
    elif inp==4:
        Result=utilities.Forecast_3hr('')
        for i in Result:
            print("===================================")
            print(f"Time:{i['date']}")
            print(f"Current Weather:{i['weather']}")
            print(f"Actual Current Temprature:{i['temprature']['temp']} C")
            print(f"Feels like:{i['temprature']['feels_like']} C")
            print(f"Pressure:{i['temprature']['pressure']} hPa")
            print(f"Humidity:{i['temprature']['humidity']} %")
            print(f"Visibility:{i['visibility']} meters")
            print("===================================")
    elif inp==5:
        print("Thank you for using Weatherboy!")
        time.sleep(1.5)
        break
    else:
        print("wrong input, please give input ranging 1 to 6")
    print()
    time.sleep(2)