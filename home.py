import tkinter as tk
from tkinter import ttk
from tkinter import *
from sdk import *
from time import *
from PIL import *

root = Tk()

root.geometry('1920x1080')
root.configure(background='#7FFFD4')
root.title('Netatmo')

label_temperature = Label(root, text=str(home.get_hc_data("Temperature")))
label_temperature.place(x=0, y=141)
label_humidity = Label(root, text=str(home.get_hc_data("Humidity")))
label_humidity.place(x=50, y=141)
label_pressure = Label(root, text=str(home.get_hc_data("Pressure")))
label_pressure.place(x=100, y=141)
label_noise = Label(root, text=str(home.get_hc_data("Noise")))
label_noise.place(x=150, y=141)
label_co2 = Label(root, text=str(home.get_hc_data("CO2")))
label_co2.place(x=200, y=141)
label_health_idx = Label(root, text=str(home.get_hc_data("health_idx")))
label_health_idx.place(x=250, y=141)

def update_data(scope):
    data = home.get_hc_data(scope)
    if scope == "Temperature":
        label_temperature.configure(text=data)
        label_temperature.text=data
    if scope == "CO2":
        label_co2.configure(text=data)
        label_co2.text=data
    if scope == "Noise":
        label_noise.configure(text=data)
        label_noise.text=data
    if scope == "health_idx":
        label_health_idx.configure(text=data)
        label_health_idx.text=data
    if scope == "Humidity":
        label_humidity.configure(text=data)
        label_humidity.text=data
    if scope == "Pressure":
        label_pressure.configure(text=data)
        label_pressure.text=data
        
def Refresher():
    for i in ("Temperature", "CO2","Noise","health_idx","Humidity","Pressure"):
        update_data(i)
    root.after(15000, Refresher)

Refresher()
root.mainloop()
