import requests
from time import gmtime, localtime
from time import strftime
import datetime
from datetime import timedelta

api_key = '???????????????'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

"""
delta = timedelta(
     seconds = weather_data.json()['timezone']
)

conversion_sunrise = datetime.timedelta(seconds=(weather_data.json()['sys']['sunrise']))
converted_sunrise = str(conversion_sunrise)
conversion_sunset = datetime.timedelta(seconds=(weather_data.json()['sys']['sunset']))
converted_sunset = str(conversion_sunset)

timelist_sunrise = [weather_data.json()['timezone'], converted_sunrise]
mysum_sunrise = datetime.timedelta()
for i in timelist_sunrise:
    (h, m, s) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    mysum_sunrise += d

timelist_sunset = [weather_data.json()['timezone'], converted_sunset]
mysum_sunset = datetime.timedelta()
for i in timelist_sunset:
    (h, m, s) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    mysum_sunset += d
"""


#print(weather_data.json())


if weather_data.json()['cod'] == '404':
   print("No City Found")
else:
   weather = weather_data.json()['weather'][0]['main']
   temp = round(weather_data.json()['main']['temp'])
   wind = weather_data.json()['wind']['speed']
   humidity = weather_data.json()['main']['humidity']


   print(f"The weather in {user_input} is: {weather}")
   print(f"Temperature in {user_input} is: {temp}℃")
   print(f"Windspeed is: {wind}")
   print(f"Humidity is at {humidity} %")
   #print(f"Sunrise is at {mysum_sunrise} local time")
   #print(f"Sunset is at {mysum_sunset} local time")

   f = open("haut.txt", "a", encoding='utf-8')
   f.write(f"The weather in {user_input} is: {weather}" + "\n")
   f.write(f"Temperature in {user_input} is: {temp}℃"  + "\n")
   f.write(f"Windspeed is: {wind}" + "\n")
   f.write(f"Humidity is at {humidity} %" + "\n")
   f.write(""  + "\n")
   f.close()
