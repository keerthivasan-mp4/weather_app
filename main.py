<<<<<<< HEAD
#Tkinter is standard GUI library for python
from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from PIL import Image, ImageTk
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.resizable(False, False)
root.configure(bg="#2fa3f0")

# Weather icon label (global reference)
weather_icon_label = Label(root, bg="#2fa3f0")
weather_icon_label.place(x=750, y=100)


##--- Weather func() ---
def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="my_weather_app_2025")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    clock.config(text=local_time.strftime("%I:%M %p"))

    if not API_KEY:
        print("API key not found in environment.")
        return

    # Fetch weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    json_data = response.json()

    if json_data.get("cod") != 200:
        print("API Error:", json_data.get("message"))
        return

    # Extract data
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['main'].lower()

    print(f"[DEBUG] Weather description: {description}")


    # Update info labels
    temperature_value.config(text=f"{temp} °C")
    humidity_value.config(text=f"{humidity}%")
    wind_value.config(text=f"{round(wind * 3.6, 2)} km/h")
    pressure_value.config(text=f"{pressure} hPa")

    # Set background based on weather
    weather_colors = {
        "clear": ("#1E87EF", "white"),
        "rain": ("#4a708b", "white"),
        "clouds": ("#778899", "white"),
        "snow": ("#e0f7fa", "black"),
        "thunderstorm": ("#2f4f4f", "white"),
        "mist": ("#708090", "white"),
    }

    bg_color, fg_color = weather_colors.get(description, ("#ea893a", "white"))
    root.configure(bg=bg_color)

    for widget in [clock, timezone, long_lat, temperature_value, humidity_value, wind_value, pressure_value]:
        widget.config(bg=bg_color, fg=fg_color)

    # Update icon
    icon_files = {
        "clear": "Images/clear.png",
        "rain": "Images/rain.png",
        "clouds": "Images/clouds.png",
        "snow": "Images/snow.png",
        "thunderstorm": "Images/thunderstorm.png",
        "mist": "Images/mist.png"
    }

    icon_path = icon_files.get(description)

    if icon_path and os.path.exists(icon_path):
        img = Image.open(icon_path).resize((100, 100), Image.LANCZOS)
        icon = ImageTk.PhotoImage(img)
        weather_icon_label.config(image=icon)
        weather_icon_label.image = icon
    else:
        weather_icon_label.config(image='')

    # if description == "clear":
    #     img = Image.open("Images/clear.png").resize((100,100), Image.LANCZOS)
    #     icon = ImageTk.PhotoImage(img)
    #     weather_icon_label.config(image=icon)
    #     weather_icon_label.image = icon
    # elif description == "rain":
    #     img = Image.open("Images/rain.png").resize((100,100), Image.LANCZOS)
    #     icon = ImageTk.PhotoImage(img)
    #     weather_icon_label.config(image=icon)
    #     weather_icon_label.image = icon
    # elif description == "snow":
    #     img = Image.open("Images/snow.png").resize((100,100), Image.LANCZOS)
    #     icon = ImageTk.PhotoImage(img)
    #     weather_icon_label.config(image=icon)
    #     weather_icon_label.image = icon
    # elif description == "thunderstorm":
    #     img = Image.open("Images/thunderstorm.png").resize((100,100), Image.LANCZOS)
    #     icon = ImageTk.PhotoImage(img)
    #     weather_icon_label.config(image=icon)
    #     weather_icon_label.image = icon



# --- UI Widgets ---
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#000000")
clock.place(x=30, y=20)

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#ea893a")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#ea893a")
long_lat.place(x=700, y=50)

textfield = Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#55A5F6", border=0, fg="white")
textfield.place(x=300, y=130)
textfield.focus()

search_button = Button(root, text="Search", font=("Helvetica", 12), bg="#2fa3f0", fg="white", command=getweather)
search_button.place(x=580, y=135)

Label(root, text="Temperature:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=120)
Label(root, text="Humidity:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=150)
Label(root, text="Wind Speed:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=180)
Label(root, text="Pressure:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=210)

temperature_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
temperature_value.place(x=160, y=120)

humidity_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
humidity_value.place(x=160, y=150)

wind_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
wind_value.place(x=160, y=180)

pressure_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
pressure_value.place(x=160, y=210)

root.mainloop()
=======
#Tkinter is standard GUI library for python
from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from PIL import Image, ImageTk
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.resizable(False, False)
root.configure(bg="#2fa3f0")

# Weather icon label (global reference)
weather_icon_label = Label(root, bg="#2fa3f0")
weather_icon_label.place(x=750, y=100)


##--- Weather func() ---
def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="my_weather_app_2025")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    clock.config(text=local_time.strftime("%I:%M %p"))

    if not API_KEY:
        print("API key not found in environment.")
        return

    # Fetch weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    json_data = response.json()

    if json_data.get("cod") != 200:
        print("API Error:", json_data.get("message"))
        return

    # Extract data
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['main'].lower()

    # Update info labels
    temperature_value.config(text=f"{temp} °C")
    humidity_value.config(text=f"{humidity}%")
    wind_value.config(text=f"{round(wind * 3.6, 2)} km/h")
    pressure_value.config(text=f"{pressure} hPa")

    # Set background based on weather
    weather_colors = {
        "clear": ("#ea893a", "white"),
        "rain": ("#4a708b", "white"),
        "clouds": ("#778899", "white"),
        "snow": ("#e0f7fa", "black"),
        "thunderstorm": ("#2f4f4f", "white"),
        "mist": ("#708090", "white"),
    }

    bg_color, fg_color = weather_colors.get(description, ("#ea893a", "white"))
    root.configure(bg=bg_color)

    for widget in [clock, timezone, long_lat, temperature_value, humidity_value, wind_value, pressure_value]:
        widget.config(bg=bg_color, fg=fg_color)

    # Update icon
    icon_files = {
        "clear": "images/clear.png",
        "rain": "images/rain.png",
        "clouds": "images/cloud.png",
        "snow": "images/snow.png",
        "thunderstorm": "images/thunderstorm.png",
        "mist": "images/mist.png"
    }

    icon_path = icon_files.get(description)

    if icon_path and os.path.exists(icon_path):
        img = Image.open(icon_path).resize((100, 100), Image.LANCZOS)
        icon = ImageTk.PhotoImage(img)
        weather_icon_label.config(image=icon)
        weather_icon_label.image = icon
    else:
        weather_icon_label.config(image='')


# --- UI Widgets ---
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#ea893a")
clock.place(x=30, y=20)

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#ea893a")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#ea893a")
long_lat.place(x=700, y=50)

textfield = Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#55A5F6", border=0, fg="white")
textfield.place(x=300, y=130)
textfield.focus()

search_button = Button(root, text="Search", font=("Helvetica", 12), bg="#2fa3f0", fg="white", command=getweather)
search_button.place(x=580, y=135)

Label(root, text="Temperature:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=120)
Label(root, text="Humidity:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=150)
Label(root, text="Wind Speed:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=180)
Label(root, text="Pressure:", font=('Helvetica', 11), fg="white", bg="#2fa3f0").place(x=45, y=210)

temperature_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
temperature_value.place(x=160, y=120)

humidity_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
humidity_value.place(x=160, y=150)

wind_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
wind_value.place(x=160, y=180)

pressure_value = Label(root, font=('Helvetica', 11), fg="white", bg="#2fa3f0")
pressure_value.place(x=160, y=210)

root.mainloop()
>>>>>>> 2c9751c532f9156166e02db3f0c5d23cc54c1fa6
