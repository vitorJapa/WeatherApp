import tkinter as tk
import requests
import time

API_KEY = "c370d69f68acd9995dfdf3ad1c626825"
Base_URL = "HTTP://api.openweathermap.org/data/2.5/weather"

def get_weather(canvas):
    city = textfield.get()
    request_url = f"{Base_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        print("city:", city)
        print("response ok")
        weather = data['weather'][0]['description']
        country = data['sys']['country']
        tempeture = round(data["main"]["temp"] - 273.15, 2)
        city = data['name']
        min_temp = round(data["main"]["temp_min"] - 273.15, 2)
        max_temp = round(data["main"]["temp_max"] - 273.15, 2)
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunrise'] + data['timezone']))
        sunset = time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunset'] + data['timezone'] ))
        final_info = weather + '\n' + str(tempeture) + "ºC"
        final_data = '\n' + "City: " + city + "\n" + "Country: " + country + '\n' + "Min temp: " + str(min_temp) + "ºC" + '\n' + "Max temp: " + str(max_temp) + "ºC" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind speed: " + str(wind) + "\n" + "Sunrise Local Time: " + str(sunrise) + " AM" + "\n" + "Sunset Local Time: " + str(sunset) + ' PM'
        label1.config(text = final_info)
        label2.config(text = final_data)
    if response.status_code == 404:
        data = response.json()
        print("city:",city)
        msg = data['message']
        print(msg)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas,justify='center', font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()