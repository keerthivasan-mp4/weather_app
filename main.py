#Tkinter is standard GUI library for python
from tkinter import * 
from tkinter import Tk #tk is a class from tkinter module, represents the main app window

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from PIL import Image, ImageTk

import requests

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

def getweather():
    city=textfield.get()

    geolocator = Nominatim(user_agent="my_weather_app_2025_yourname")

    location = geolocator.geocode(city)

    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result) 

    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api =  f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid=696cdbab64ba5147f64c2302c154e86a"


    json_data = requests.get(api).json()
    print(json_data)
    #current
    temp = json_data['current']['temp']
    temperature_label = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
    temperature_label.place(x=150, y=120)

    temperature_label.config(text=f"{temp} °C")





#icon
image_icon=PhotoImage(file="Images-20250513T121650Z-1-001/Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Rounded Rectangle 1.png")
Label(root,image=Round_box, bg="#57adff").place(x=30,y=110)

#label
label1 = Label(root,text="Temperature", font=('Helvetica',11), fg="white", bg="#203243")
label1.place(x=45,y=120)

label2 = Label(root,text="Humidity", font=('Helvetica',11), fg="white", bg="#203243")
label2.place(x=45,y=140)

label3 = Label(root,text="wind speed", font=('Helvetica',11), fg="white", bg="#203243")
label3.place(x=45,y=160)

label4 = Label(root,text="Air Quality", font=('Helvetica',11), fg="white", bg="#203243")
label4.place(x=45,y=180)

#search box
search_image = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Rounded Rectangle 3.png")
myimage= Label(image = search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Layer 7.png")
weatherimage = Label(root, image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield = Entry(root, justify='center', width=15, font=('poppins',25,'bold'), bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0,cursor="hand2", bg="#203243", command=getweather)
myimage_icon.place(x=648,y=125)

#bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images-20250513T121650Z-1-001/Images/Rounded Rectangle 2 copy.png")
Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)

Label(frame, image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame, image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame, image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame, image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame, image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame, image=secondbox,bg="#212120").place(x=800,y=30)

#clock
clock = Label(root, font=("Helvetica",30  ,'bold'),fg="white", bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20), fg="white", bg="#57adff")
timezone.place(x=700,y=20)

long_lat = Label(root, font=("Helvetica",10), fg="white", bg="#57adff")
long_lat.place(x=700,y=50)


root.mainloop()