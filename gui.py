from tkinter import *
from measurement_units import *

window = Tk()
window.title('Converter')
window.geometry('270x80')

def temperature():
    units = [Celsius(), Fahrenheit(), Kelvin()]
    measurements.config(text='Temperature')
    textbox.delete(0, END)
    result.config(text='-')
    celsius_b()
    fahrenheit_a()

def celsius_b():
    result.config(text='-')
    global before_unit
    before_unit = Celsius()
    before.config(text=before_unit)
    before.menu = Menu(before, tearoff=0)
    before['menu'] = before.menu
    before.menu.add_command(label=Fahrenheit(), command=fahrenheit_b)
    before.menu.add_command(label=Kelvin(), command=kelvin_b)

def fahrenheit_b():
    result.config(text='-')
    global before_unit
    before_unit = Fahrenheit()
    before.config(text=before_unit)
    before.menu = Menu(before, tearoff=0)
    before['menu'] = before.menu
    before.menu.add_command(label=Celsius(), command=celsius_b)
    before.menu.add_command(label=Kelvin(), command=kelvin_b)

def kelvin_b():
    result.config(text='-')
    global before_unit
    before_unit = Kelvin()
    before.config(text=before_unit)
    before.menu = Menu(before, tearoff=0)
    before['menu'] = before.menu
    before.menu.add_command(label=Celsius(), command=celsius_b)
    before.menu.add_command(label=Fahrenheit(), command=fahrenheit_b)

def celsius_a():
    result.config(text='-')
    global after_unit
    after_unit = Celsius()
    after.config(text=after_unit)
    after.menu = Menu(after, tearoff=0)
    after['menu'] = after.menu
    after.menu.add_command(label=Fahrenheit(), command=fahrenheit_a)
    after.menu.add_command(label=Kelvin(), command=kelvin_a)

def fahrenheit_a():
    result.config(text='-')
    global after_unit
    after_unit = Fahrenheit()
    after.config(text=after_unit)
    after.menu = Menu(after, tearoff=0)
    after['menu'] = after.menu
    after.menu.add_command(label=Celsius(), command=celsius_a)
    after.menu.add_command(label=Kelvin(), command=kelvin_a)

def kelvin_a():
    result.config(text='-')
    global after_unit
    after_unit = Kelvin()
    after.config(text=after_unit)
    after.menu = Menu(after, tearoff=0)
    after['menu'] = after.menu
    after.menu.add_command(label=Celsius(), command=celsius_a)
    after.menu.add_command(label=Fahrenheit(), command=fahrenheit_a)
    
def speed():
    units = [MetresPerSecond(), KilometresPerHour(), FeetPerSecond(),
             MilesPerHour(), Knots()]
    measurements.config(text='Speed')
    textbox.delete(0, END)
    result.config(text='-')
    unit_settings(units)

def angle():
    units = [Degrees(), Radians(), Milliradians(), Gradians(), Arcseconds(),
             Arcminutes()]
    measurements.config(text='Angle')
    textbox.delete(0, END)
    result.config(text='-')
    unit_settings(units)

def unit_settings(units, before_index=0, after_index=1):
    units_copy = units[:]
    global before_unit
    before_unit = units_copy.pop(before_index)
    before.config(text=before_unit)
    before.menu = Menu(before, tearoff=0)
    before['menu'] = before.menu
    for unit in units_copy:
        before.menu.add_command(label=unit)

    units_copy = units[:]
    global after_unit
    after_unit = units_copy.pop(after_index)
    after.config(text=after_unit)
    after.menu = Menu(after, tearoff=0)
    after['menu'] = after.menu
    for unit in units_copy:
        after.menu.add_command(label=unit)

def equals_button():
    try:
        number = float(textbox.get())
        if before_unit.name == after_unit.name:
            result.config(text=f'{number}')
        else:
            new_number = after_unit.conversion(before_unit, number)
            result.config(text=f'{new_number:.3f}')
    except ValueError:
        result.config(text='-')
    
measure_types = {'Temperature': temperature, 'Speed': speed, 'Angle': angle}
measurements = Menubutton(window, text='Temperature')
measurements.menu = Menu(measurements, tearoff=0)
measurements['menu'] = measurements.menu
for key, value in measure_types.items():
    measurements.menu.add_command(label=key, command=value)
measurements.grid(column=0, row=0)

textbox = Entry(window)
result = Label(window, text='-')
equals = Button(window, text=' = ', command=equals_button)
textbox.grid(column=0, row=1)
result.grid(column=2, row=1)
equals.grid(column=1, row=1)

before = Menubutton(window)
before_unit = None
after = Menubutton(window)
after_unit = None
before.grid(column=0, row=2)
after.grid(column=2, row=2)

temperature()

window.mainloop()
