import requests

key="70f99925cc89d99f50c781fc0765ea06"

#API call for current weather
def API_Call_Current_Weather(City):
    if City=='': #checks if city input has been specified or not
        City = input("Enter City:")
    while True:#loops so that city cant be invalid(incase of typos)
        url=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}&units=metric" #api call link using f-strings
        response=requests.get(url) #calls the raw data from url
        data=response.json() #formats raw data into url
        if data['cod']=='404': #for invalid cities, the data has a 'cod':404 key value pair. uses it to check for invalid city
            print("Invalid City name, please try different name")
            City=input("Enter City:")
        else: #returns valid data if city is covered in API
            return data

def API_Call_AQI(City):
    if City=='':
        City = input("Enter City:") 
    while True:
        url=f"http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=5&appid={key}" #following 4 lines convert city name to latitude and longitude
        response=requests.get(url)
        data=response.json()
        lat,lon=data[0]["lat"],data[0]["lon"]
        url2=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}" #gets actual AQI results for given latitude and longitude
        response2=requests.get(url2)
        data2=response2.json()
        if data['cod']=='404':
            print("Invalid City name, please try different name")
            City=input("Enter City:")
        else:
            return data2
    

def API_Call_Forecast(city):
    if city=='':
        city = input("Enter City:")
    while True:
        url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=metric" #gets forecast data for 5 days, 3hrs per day (9 AM, 12 noon and 3 PM)
        response=requests.get(url)
        data=response.json()
        print(data['cod'])
        if data['cod']=='404':
            print("Invalid City name, please try different name")
            city=input("Enter City:")
        else:
            return data

