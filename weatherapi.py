import tkinter as tk
import requests
from tkinter import messagebox

def open_weather_app(root):

    def get_weather():
        api_key = "267ba5a73dba403285b214952231412"  # Replace with your WeatherAPI.com API key
        city = city_entry.get()
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

        try:
            response = requests.get(url)
            weather_data = response.json()

            if "error" in weather_data:
                messagebox.showerror("Error", weather_data["error"]["message"])
            else:
                weather_desc = weather_data["current"]["condition"]["text"]
                temperature = weather_data["current"]["temp_c"]
                humidity = weather_data["current"]["humidity"]

                info_text = f"Weather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
                weather_display.config(text=info_text)
        except requests.ConnectionError:
            messagebox.showerror("Error", "Please check your internet connection!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        
    weather_window = tk.Toplevel(root)
    weather_window.title("Weather App")
    weather_window.geometry("300x200")
    weather_window.minsize(300, 200)

    city_label = tk.Label(weather_window, text="Enter city:")
    city_entry = tk.Entry(weather_window, width=20)
    get_weather_button = tk.Button(weather_window, text="Get Weather", command=get_weather)
    weather_display = tk.Label(weather_window, text="", justify=tk.LEFT)

    city_label.pack()
    city_entry.pack()
    get_weather_button.pack()
    weather_display.pack()
