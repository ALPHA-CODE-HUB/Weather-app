from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        humidity = json['main']['humidity']
        pressure = json['main']['pressure']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        weather_desp = json['weather'][0]['description']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather, weather_desp,humidity,pressure)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        temp_lbl.config(bg='blue')

        loacation_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img["file"] = 'weather_icons\\{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        pressure_lbl['text']='Pressure:- {}'.format(weather[8])
        humadity_lbl['text']='Humidity:- {}'.format(weather[7])
        weather_lbl['text'] = weather[5]
        weather_des_lbl['text'] = weather[6]
    else:
        messagebox.showerror('Error', 'Cannot find city {} '.format(city))




app = Tk()
app.title("Weather app")
app.configure(bg='#f0dcda')
app.geometry('700x350')


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, width=40)
city_entry.insert(0, "Enter Search Loaction")
city_entry.pack()

imge = PhotoImage(file='img1.png')
search_btn = Button(app, text='Search Weather', command=search, pady=10, bg='white')
search_btn.config(image=imge, padx=10)
search_btn.config(compound='right')
search_btn.pack()

loacation_lbl = Label(app, text='', bg='#f0dcda', font=('Bold', 20), )
loacation_lbl.pack()
img = PhotoImage(file='')
Image = Label(app, image=img, pady=15, bg='#f0dcda')
Image.pack()

temp_lbl = Label(app, text='', bg='#f0dcda')
temp_lbl.pack()

pressure_lbl=Label(app,text='',bg='#f0dcda')
pressure_lbl.pack()

humadity_lbl=Label(app,text='',bg='#f0dcda')
humadity_lbl.pack()

weather_lbl = Label(app, text='', bg='#f0dcda')
weather_lbl.pack()
weather_des_lbl = Label(app, text='', bg='#f0dcda')
weather_des_lbl.pack()

app.mainloop()
