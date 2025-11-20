import Weatherboy
import time

#loop so function runs indefinitely untill stopped by user.
while True:

    # Menu:
    print("=====Weatherboy Terminal System====")
    print("1. Get Current Weather")
    print("2. Get Air Quality Index(AQI)")
    print("3. Weather + AQI Combined Report")
    print("4. View Search History")
    print("5. Analytics and Insight")
    print("6. Exit")
    print("===================================")
    
    #input for above menu:
    inp=int(input("Enter choice:"))

    #logic to check which choice was made:
    if inp==1:
        L=Weatherboy.Current_Weather()
        print(f"Current Weather:{L['weather']}")
        print(f"Actual Current Temprature:{L['temprature']['temp']}")
        print(f"Feels like:{L['temprature']['feels_like']}")
        print(f"Pressure:{L['temprature']['pressure']}")
        print(f"Humidity:{L['temprature']['sea_level']}")
    elif inp==2:
        print(Weatherboy.AQI())
    elif inp==3:
        print(Weatherboy.Weather_AQI_Combined())
    elif inp==4:
        print(Weatherboy.History())
    elif inp==5:
        print(Weatherboy.Analytics())
    elif inp==6:
        print("Thank you for using Weatherboy!")
        time.sleep(1.5)
        break
    else:
        print("wrong input, please give input ranging 1 to 6")
    print()