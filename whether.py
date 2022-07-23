from re import L
from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
from tkinter.font import BOLD
import requests

url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = 'weather.key'
file_a = ConfigParser()      # To read the api key which we have
file_a.read(api_file)
api_key = file_a['api_key']['key']

def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        json_file = final.json()     # Refer json file on the website openwheather to put name, sys country, main temp
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file['main']['temp']
        c_temperature = k_temperature - 273.15   # Temperature in celsius
        weather_display = json_file['weather'][0]['main']
        result = (city, country_name, c_temperature,weather_display)
        return result

    else:
        return None


def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0], weather[1])  # Two for city and country
        temperature_entry['text'] = '{:.2f} C'.format(weather[2])         # :.2f for two decimal points
        weather_entry['text'] = weather[3]

    else:
        messagebox.showerror('Error','Please enter the valid cityname')





# MAKING TKINTER WINDOW
root = Tk()                  # Make tkinker variable root and giving it detais like title, background colour, size
root.title("Whether App")
root.config(background="black")
root.geometry("700x400")


# MAKING ENTRY BOX
search_city = StringVar()
enter_city = Entry(root, textvariable=search_city,fg="blue", font=("Arial",30,"bold"))
enter_city.pack()            # .pack allow to put all this on tkinter window


# MAKING SEARCH BUTTON
search_button = Button(root, text='Search', width=10, bg="red",fg="white", font=("Arial", 15, "bold"), command=print_weather)
search_button.pack()


# OUTPUT LOCATION, TEMPERATURE, WEATHER 
location_entry = Label(root, text='',font=("Arial",35, "bold"), bg="black")
location_entry.pack()

temperature_entry = Label(root, text='',font=("Arial", 35, "bold"), bg="black")
temperature_entry.pack()

weather_entry = Label(root, text='', font=("Arial", 35, "bold"), bg="lightgreen")
weather_entry.pack()





root.mainloop()              # Last line of code that will allow to show output window