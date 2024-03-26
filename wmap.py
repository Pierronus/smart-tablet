import tkinter as tk
from tkinter import ttk
from tkinter import *

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    print(current_value.get())


def slider_changed(event):
    get_current_value()


# label for the slider
slider_label = ttk.Label(
    root,
    text='Slider:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = Scale(
    root,
    from_=0,
    to=254,
    orient='horizontal',  # vertical
    command=slider_changed,
    showvalue=0,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)


root.mainloop()