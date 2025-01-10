import requests
from tkinter import *

def get_weather():
    city = city_entry.get()
    api_key = "Use your own Api"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            result_label.config(text=f"Error: {data['message']}", fg="red")
        else:
            weather = data["weather"][0]["main"]
            temp = data["main"]["temp"]
            result_label.config(
                text=f"Weather: {weather}\nTemperature: {temp}°C", fg="green"
            )
    except Exception as e:
        result_label.config(text="Unable to fetch data. Check your connection.", fg="red")
root = Tk()
root.title("Weather Dashboard")

Label(root, text="Enter City:", font=("Arial", 14)).pack(pady=10)
city_entry = Entry(root, font=("Arial", 14), width=20)
city_entry.pack(pady=5)

Button(root, text="Get Weather", font=("Arial", 14), command=get_weather).pack(pady=10)
result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.geometry("300x200")
root.mainloop()


