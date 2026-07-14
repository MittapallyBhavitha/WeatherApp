import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    unit = unit_var.get()

    if unit == "C":
        units = "metric"
        symbol = "°C"
    else:
        units = "imperial"
        symbol = "°F"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        weather = (
            f"Temperature: {data['main']['temp']}{symbol}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Condition: {data['weather'][0]['description'].title()}\n"
            f"Wind Speed: {data['wind']['speed']}"
        )

        weather_label.config(text=weather)

    except:
        messagebox.showerror("Error", "Unable to fetch weather.")

# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("350x320")

tk.Label(root, text="Enter City:").pack(pady=5)

city_entry = tk.Entry(root, width=25)
city_entry.pack()

unit_var = tk.StringVar(value="C")

tk.Radiobutton(root, text="Celsius", variable=unit_var, value="C").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="F").pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_label = tk.Label(root, text="", justify="left")
weather_label.pack(pady=10)

root.mainloop()