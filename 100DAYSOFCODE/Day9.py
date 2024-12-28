import requests

api_key='18801b3d598d93968d727c48ca03c6d7'

user_input=input("Enter City: ")

weather_api=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_api.json()['cod'] == '404':
    print("No City Found")
else:
    weather=weather_api.json()['weather'][0]['main']
    temp=weather_api.json()['main']['temp']
    humidity=weather_api.json()['main']['humidity']
    pressure=weather_api.json()['main']["pressure"]

    print(f"The Weather in {user_input} is: {weather}")

    print(f"The Temperature in {user_input} is: {temp}°C")
    
    print(f"The Humidity in {user_input} is: {humidity}%")

    print(f"The Pressure in {user_input} is: {pressure} hPa")




















